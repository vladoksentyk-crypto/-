# Усе, що гра показує на екрані (крім меню, які мають власну логіку).

from config import (GOAL_GOLD, INGREDIENT_SLOTS, MAX_DAYS, POTION_SLOTS, RENT_PER_DAY)
from crafting import can_craft
from data_potions import POTIONS
from inventory import used_slots


def show_status(game):
    """Рядок стану над меню."""
    try:
        print("\n" + "=" * 70)
        print(f" ДЕНЬ {game['day']} з {MAX_DAYS} | Золото: {game['gold']} / {GOAL_GOLD} "
              f"| Оренда: {RENT_PER_DAY}/день | Ринок: x{game['market']}")
        print(f" Зілля: {used_slots(game['potions'])}/{POTION_SLOTS} слотів "
              f"| Інгредієнти: {used_slots(game['ingredients'])}/{INGREDIENT_SLOTS} слотів")
        print("-" * 70)
        print(" [I] Інвентар  [C] Варити  [R] Рецепти  [E] Кінець дня  [H] Допомога  [Q] Вихід")
    except KeyError as error:
        print(f"[!] Не вдалося показати стан гри: немає поля {error}")


def show_slots(title, slots):
    """Показує всі слоти одного інвентаря."""
    try:
        print(f"\n--- {title} ({used_slots(slots)}/{len(slots)}) ---")
        for number, slot in enumerate(slots, 1):
            if slot is None:
                print(f"{number:>2}. ---")
            else:
                print(f"{number:>2}. {slot['name']} x{slot['count']}")
    except (KeyError, TypeError) as error:
        print(f"[!] Не вдалося показати інвентар: {error}")


def show_inventory(game):
    """Обидва інвентарі: зілля та інгредієнти."""
    show_slots("ІНВЕНТАР ЗІЛЛЯ", game["potions"])
    show_slots("ІНВЕНТАР ІНГРЕДІЄНТІВ", game["ingredients"])


def show_recipes(game):
    """Книга рецептів: усі 50 зілль, позначено ті, що можна зварити зараз."""
    print("\n=== КНИГА РЕЦЕПТІВ ===")
    for number, potion in enumerate(POTIONS, 1):
        mark = "  <- можна зварити" if can_craft(game, potion) else ""
        recipe_text = " + ".join(potion["recipe"])
        print(f"{number:>2}. {potion['name']}  [{recipe_text}]  ціна {potion['price']}{mark}")


def show_help():
    """Правила гри."""
    print(f"""
=== ДОПОМОГА ===
Ти алхімік. Мета: назбирати {GOAL_GOLD} золота за {MAX_DAYS} днів.
Щодня ти отримуєш інгредієнти, варишь з них зілля, а ввечері продаєш.
Кожен день треба платити {RENT_PER_DAY} золота за оренду - не заплатиш, програєш.

Клавіші:
  I - інвентар (там можна викинути зайве)
  C - варити зілля (рецепт: два інгредієнти потрібних категорій)
  R - книга рецептів
  E - закінчити день: продаж зілля, оренда, новий день
  H - ця допомога,  Q - вихід

Інвентар зілль: {POTION_SLOTS} слотів, у слоті до 10 однакових зілль.
Інвентар інгредієнтів: {INGREDIENT_SLOTS} слотів, у слоті до 25 однакових інгредієнтів.
Ціни на ринку щодня трохи змінюються.""")
