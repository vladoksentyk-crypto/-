# Пул зілль: 5 типів x 10 ефектів = 50 різних зілль.
# Рецепт: два інгредієнти певних КАТЕГОРІЙ (підійде будь-який інгредієнт цієї категорії).

import random

from data_ingredients import BASES

PREFIXES = ["Еліксир", "Зілля", "Настоянка", "Відвар", "Тонік"]

EFFECTS = [
    "лікування", "сили", "швидкості", "невидимості", "мудрості",
    "удачі", "відваги", "захисту", "пам'яті", "зору",
]


def build_potions():
    """Створює 50 зілль. random.Random(7) дає однакові рецепти й ціни при кожному запуску."""
    try:
        rng = random.Random(7)
        # усі пари категорій (включно з двома однаковими): 55 унікальних комбінацій
        pairs = [(a, b) for i, a in enumerate(BASES) for b in BASES[i:]]
        rng.shuffle(pairs)
        names = [f"{prefix} {effect}" for prefix in PREFIXES for effect in EFFECTS]

        potions = []
        for name, (cat_a, cat_b) in zip(names, pairs):
            potions.append({
                "name": name,
                "price": rng.randint(35, 140),
                "recipe": [cat_a, cat_b],
            })
        if len(potions) < 50:
            raise ValueError("Пул має містити щонайменше 50 зілль")
        return potions
    except TypeError as error:
        raise ValueError(f"Помилка в даних зілль: {error}")


POTIONS = build_potions()
POTION_BY_NAME = {potion["name"]: potion for potion in POTIONS}
