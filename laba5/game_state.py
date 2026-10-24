# Створення нової гри. Увесь стан зберігається в одному словнику game.

from config import INGREDIENT_SLOTS, POTION_SLOTS, START_GOLD
from inventory import create_inventory


def new_game():
    """Повертає початковий стан гри."""
    try:
        return {
            "day": 0,
            "gold": START_GOLD,
            "market": 1.0,
            "potions": create_inventory(POTION_SLOTS),
            "ingredients": create_inventory(INGREDIENT_SLOTS),
            "crafted": 0,
            "earned": 0,
            "ending": None,
        }
    except ValueError as error:
        raise RuntimeError(f"Не вдалося створити нову гру: {error}")
