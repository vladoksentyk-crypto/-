# Робота зі слотами інвентаря. Слот - це None (порожній) або словник {"name": ..., "count": ...}.
# Одні й ті самі функції працюють і для зілль, і для інгредієнтів - відрізняється тільки max_stack.

from exceptions import InventoryFullError, ItemNotFoundError


def create_inventory(size):
    """Створює порожній інвентар на size слотів."""
    try:
        return [None] * int(size)
    except (TypeError, ValueError):
        raise ValueError("Розмір інвентаря має бути числом")


def used_slots(slots):
    """Скільки слотів зайнято."""
    return sum(1 for slot in slots if slot is not None)


def count_item(slots, name):
    """Скільки всього штук предмета name у всіх слотах."""
    try:
        return sum(slot["count"] for slot in slots if slot is not None and slot["name"] == name)
    except (KeyError, TypeError) as error:
        raise ValueError(f"Пошкоджений слот інвентаря: {error}")


def free_space(slots, name, max_stack):
    """Скільки ще штук предмета name поміститься в інвентар."""
    try:
        space = 0
        for slot in slots:
            if slot is None:
                space += max_stack
            elif slot["name"] == name:
                space += max_stack - slot["count"]
        return space
    except (KeyError, TypeError) as error:
        raise ValueError(f"Пошкоджений слот інвентаря: {error}")


def add_item(slots, name, amount, max_stack):
    """Додає предмет: спочатку дозаповнює наявні стаки, потім займає порожні слоти.
    Якщо місця не вистачає - нічого не змінює і кидає InventoryFullError."""
    try:
        if amount <= 0:
            raise ValueError("Кількість має бути додатною")
        if free_space(slots, name, max_stack) < amount:
            raise InventoryFullError(name)

        left = amount
        for slot in slots:
            if left == 0:
                break
            if slot is not None and slot["name"] == name and slot["count"] < max_stack:
                put = min(max_stack - slot["count"], left)
                slot["count"] += put
                left -= put

        for index, slot in enumerate(slots):
            if left == 0:
                break
            if slot is None:
                put = min(max_stack, left)
                slots[index] = {"name": name, "count": put}
                left -= put
    except (KeyError, TypeError) as error:
        raise ValueError(f"Пошкоджений слот інвентаря: {error}")


def remove_item(slots, name, amount):
    """Забирає amount штук предмета (спочатку з найменших стаків, щоб звільняти слоти)."""
    try:
        if count_item(slots, name) < amount:
            raise ItemNotFoundError(f"Недостатньо предметів: {name} (потрібно {amount})")

        indexes = [i for i, slot in enumerate(slots) if slot is not None and slot["name"] == name]
        indexes.sort(key=lambda i: slots[i]["count"])

        left = amount
        for index in indexes:
            if left == 0:
                break
            take = min(slots[index]["count"], left)
            slots[index]["count"] -= take
            left -= take
            if slots[index]["count"] == 0:
                slots[index] = None
    except (KeyError, TypeError) as error:
        raise ValueError(f"Пошкоджений слот інвентаря: {error}")


def get_slot(slots, number):
    """Повертає слот за номером (з 1). Якщо номер неправильний або слот порожній - помилка."""
    try:
        slot = slots[number - 1]
        if number < 1 or slot is None:
            raise ItemNotFoundError(f"Слот {number} порожній")
        return slot
    except IndexError:
        raise ItemNotFoundError(f"Слота {number} не існує")
