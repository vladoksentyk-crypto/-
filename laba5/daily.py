# Ігровий день: початок (нові інгредієнти) і кінець (продаж, оренда, перевірка фіналу).

import random
from collections import Counter

from config import DAILY_INGREDIENTS, INGREDIENT_STACK
from data_ingredients import INGREDIENTS
from endings import check_end_conditions, pay_rent
from exceptions import InventoryFullError
from inventory import add_item
from market import sell_menu


def give_ingredients(game, amount):
    """Видає amount випадкових інгредієнтів. Повертає (отримані, ті що не вмістились)."""
    received = []
    lost = []
    for _ in range(amount):
        ingredient = random.choice(INGREDIENTS)
        try:
            add_item(game["ingredients"], ingredient["name"], 1, INGREDIENT_STACK)
            received.append(ingredient["name"])
        except InventoryFullError as error:
            lost.append(str(error))
    return received, lost


def start_new_day(game):
    """Починає новий день: нова ціна ринку + щоденні інгредієнти."""
    try:
        game["day"] += 1
        game["market"] = round(random.uniform(0.8, 1.2), 2)
        received, lost = give_ingredients(game, DAILY_INGREDIENTS)

        print(f"\n*** Починається день {game['day']} ***")
        print("Ти отримав інгредієнти:")
        for name, count in Counter(received).items():
            print(f"  + {name} x{count}")
        if lost:
            print("[!] Не вмістилось (інвентар заповнений): " + ", ".join(lost))
    except KeyError as error:
        raise ValueError(f"У стані гри немає поля {error}")


def end_day(game):
    """Кінець дня: продаж зілля -> оренда -> перевірка перемоги/поразки -> новий день."""
    print("\n*** Кінець дня ***")
    sell_menu(game)
    if not pay_rent(game):
        return
    check_end_conditions(game)
    if game["ending"] is None:
        start_new_day(game)
