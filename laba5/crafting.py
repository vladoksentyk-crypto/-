# Варіння зілля: підбір інгредієнтів, перевірка, саме варіння і меню.

from config import POTION_STACK
from data_ingredients import CATEGORY_BY_NAME
from data_potions import POTIONS
from exceptions import InventoryFullError, NotEnoughIngredientsError
from input_utils import ask_number
from inventory import add_item, free_space, remove_item


def pick_ingredients(ingredient_slots, recipe):
    """Підбирає конкретні інгредієнти під категорії рецепта. Нічого не списує.
    Якщо категорії не знайшлося - NotEnoughIngredientsError."""
    try:
        available = {}
        for slot in ingredient_slots:
            if slot is not None:
                available[slot["name"]] = available.get(slot["name"], 0) + slot["count"]

        chosen = []
        for category in recipe:
            candidates = [
                name for name, count in available.items()
                if count > 0 and CATEGORY_BY_NAME[name] == category
            ]
            if not candidates:
                raise NotEnoughIngredientsError(f"Бракує інгредієнта категорії «{category}»")
            name = min(candidates, key=lambda n: available[n])   # беремо з меншого стаку
            available[name] -= 1
            chosen.append(name)
        return chosen
    except KeyError as error:
        raise ValueError(f"Невідомий інгредієнт: {error}")


def can_craft(game, potion):
    """True, якщо інгредієнтів вистачає на це зілля."""
    try:
        pick_ingredients(game["ingredients"], potion["recipe"])
        return True
    except NotEnoughIngredientsError:
        return False


def craft_potion(game, potion):
    """Варить одне зілля: перевіряє місце, списує інгредієнти, додає зілля в інвентар."""
    try:
        if free_space(game["potions"], potion["name"], POTION_STACK) < 1:
            raise InventoryFullError("Інвентар зілль заповнений - спочатку продай або викинь зілля")

        used = pick_ingredients(game["ingredients"], potion["recipe"])
        for name in used:
            remove_item(game["ingredients"], name, 1)
        add_item(game["potions"], potion["name"], 1, POTION_STACK)
        game["crafted"] += 1
        return used
    except KeyError as error:
        raise ValueError(f"У стані гри немає поля {error}")


def crafting_menu(game):
    """Меню варіння: показує тільки ті зілля, на які зараз вистачає інгредієнтів."""
    while True:
        craftable = [potion for potion in POTIONS if can_craft(game, potion)]
        print("\n=== ВАРІННЯ ЗІЛЛЯ ===")
        if not craftable:
            print("З твоїх інгредієнтів зараз не можна зварити жодного зілля.")
            print("Натисни R, щоб подивитись рецепти.")
            return

        for number, potion in enumerate(craftable, 1):
            recipe_text = " + ".join(potion["recipe"])
            print(f"{number:>2}. {potion['name']}  [{recipe_text}]  базова ціна {potion['price']}")

        choice = ask_number("Номер зілля (0 - назад): ", 0, len(craftable))
        if choice == 0:
            return

        potion = craftable[choice - 1]
        try:
            used = craft_potion(game, potion)
            print(f"\nЗварено: {potion['name']}! Витрачено: {', '.join(used)}")
        except (InventoryFullError, NotEnoughIngredientsError) as error:
            print(f"[!] {error}")
