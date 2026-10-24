# Продаж зілля наприкінці дня.

from data_potions import POTION_BY_NAME
from exceptions import ItemNotFoundError
from input_utils import ask_number
from inventory import get_slot, remove_item


def potion_price(game, name):
    """Ціна одного зілля сьогодні = базова ціна x ринковий коефіцієнт дня."""
    try:
        return max(1, round(POTION_BY_NAME[name]["price"] * game["market"]))
    except KeyError as error:
        raise ValueError(f"Невідоме зілля або немає поля: {error}")


def sell_potion(game, slot_number, amount):
    """Продає amount зілль зі слота. Повертає (назва, виручка)."""
    slot = get_slot(game["potions"], slot_number)
    name = slot["name"]
    income = potion_price(game, name) * amount
    remove_item(game["potions"], name, amount)
    game["gold"] += income
    game["earned"] += income
    return name, income


def sell_all(game):
    """Продає всі зілля. Повертає загальну виручку."""
    total = 0
    for number in range(1, len(game["potions"]) + 1):
        slot = game["potions"][number - 1]
        if slot is not None:
            _, income = sell_potion(game, number, slot["count"])
            total += income
    return total


def sell_menu(game):
    """Меню продажу: продати слот, продати все або піти."""
    print("\n=== ПРОДАЖ ЗІЛЛЯ ===")
    print(f"Ринковий коефіцієнт сьогодні: x{game['market']}")
    while True:
        if all(slot is None for slot in game["potions"]):
            print("У тебе немає зілля на продаж.")
            return

        for number, slot in enumerate(game["potions"], 1):
            if slot is not None:
                price = potion_price(game, slot["name"])
                print(f"{number:>2}. {slot['name']} x{slot['count']}  - {price} за штуку")

        raw = input("Номер слота, A - продати все, 0 - завершити продаж: ").strip().lower()
        try:
            if raw == "0":
                return
            if raw in ("a", "ф"):
                print(f"Продано все зілля, виручка: {sell_all(game)} золота.")
                return
            slot_number = int(raw)
            slot = get_slot(game["potions"], slot_number)
            amount = ask_number(f"Скільки продати (1-{slot['count']}): ", 1, slot["count"])
            name, income = sell_potion(game, slot_number, amount)
            print(f"Продано {name} x{amount} за {income} золота.")
        except ValueError:
            print("[!] Введи номер слота, літеру A або 0.")
        except ItemNotFoundError as error:
            print(f"[!] {error}")
