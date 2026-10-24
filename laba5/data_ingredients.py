# Пул інгредієнтів: 10 категорій x 20 властивостей = 200 різних інгредієнтів.

BASES = [
    "Корінь", "Лист", "Гриб", "Квітка", "Ягода",
    "Мох", "Кора", "Насіння", "Пелюстка", "Кристал",
]

MODIFIERS = [
    "дракона", "тіні", "місяця", "сонця", "грому",
    "льоду", "вогню", "лісу", "болота", "туману",
    "вітру", "зорі", "русалки", "привида", "гнома",
    "фенікса", "вовка", "ворона", "змії", "єдинорога",
]


def build_ingredients():
    """Створює список з 200 інгредієнтів і перевіряє, що їх достатньо і вони унікальні."""
    try:
        ingredients = [
            {"name": f"{base} {modifier}", "category": base}
            for base in BASES
            for modifier in MODIFIERS
        ]
        names = {item["name"] for item in ingredients}
        if len(ingredients) < 200 or len(names) != len(ingredients):
            raise ValueError("Пул має містити щонайменше 200 унікальних інгредієнтів")
        return ingredients
    except TypeError as error:
        raise ValueError(f"Помилка в даних інгредієнтів: {error}")


INGREDIENTS = build_ingredients()
CATEGORY_BY_NAME = {item["name"]: item["category"] for item in INGREDIENTS}
