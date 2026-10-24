# Меню інвентаря: перегляд і викидання зайвого.

from config import INGREDIENT_SLOTS, POTION_SLOTS
from display import show_inventory
from exceptions import ItemNotFoundError
from input_utils import ask_number
from inventory import get_slot, remove_item


def discard_item(game, inventory_key, size):
    """Викидає предмет із інвентаря inventory_key ('potions' або 'ingredients')."""
    try:
        number = ask_number(f"Номер слота (1-{size}, 0 - скасувати): ", 0, size)
        if number == 0:
            return
        slot = get_slot(game[inventory_key], number)
        amount = ask_number(f"Скільки викинути (1-{slot['count']}): ", 1, slot["count"])
        name = slot["name"]
        remove_item(game[inventory_key], name, amount)
        print(f"Викинуто: {name} x{amount}")
    except ItemNotFoundError as error:
        print(f"[!] {error}")


def inventory_menu(game):
    """Показує інвентар і дозволяє викидати предмети."""
    while True:
        show_inventory(game)
        print("\n1 - викинути інгредієнт | 2 - викинути зілля | 0 - назад")
        choice = ask_number("Твій вибір: ", 0, 2)
        if choice == 0:
            return
        if choice == 1:
            discard_item(game, "ingredients", INGREDIENT_SLOTS)
        else:
            discard_item(game, "potions", POTION_SLOTS)
