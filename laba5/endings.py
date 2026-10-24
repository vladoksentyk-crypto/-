# Оренда, умови перемоги/поразки і фінальні тексти.

from config import GOAL_GOLD, MAX_DAYS, RENT_PER_DAY


def pay_rent(game):
    """Сплачує оренду. Якщо золота не вистачає - гра програна (ending = lose_rent)."""
    try:
        if game["gold"] < RENT_PER_DAY:
            game["ending"] = "lose_rent"
            return False
        game["gold"] -= RENT_PER_DAY
        print(f"Ти заплатив {RENT_PER_DAY} золота за оренду лабораторії. Лишилось: {game['gold']}.")
        return True
    except KeyError as error:
        raise ValueError(f"У стані гри немає поля {error}")


def check_end_conditions(game):
    """Перевіряє, чи гра закінчилась перемогою або поразкою за часом."""
    try:
        if game["gold"] >= GOAL_GOLD:
            game["ending"] = "win"
        elif game["day"] >= MAX_DAYS:
            game["ending"] = "lose_time"
    except KeyError as error:
        raise ValueError(f"У стані гри немає поля {error}")


def show_ending(game):
    """Друкує фінал гри та підсумкову статистику."""
    try:
        texts = {
            "win": (
                "ПЕРЕМОГА!\n"
                f"Ти назбирав {game['gold']} золота, і про твої еліксири дізнався сам король.\n"
                "Королівська гільдія призначає тебе придворним алхіміком. Слава і достаток тобі гарантовані!"
            ),
            "lose_rent": (
                "ПОРАЗКА.\n"
                "У тебе не вистачило золота на оренду. Господар виставив твої котли за двері,\n"
                "а лабораторію віддав іншому алхіміку. Доведеться шукати нове місце..."
            ),
            "lose_time": (
                f"ПОРАЗКА.\nМинуло {MAX_DAYS} днів, але ти не назбирав {GOAL_GOLD} золота.\n"
                "Гільдія відмовила тобі в посаді придворного алхіміка. Спробуй ще раз!"
            ),
            "quit": "Ти вирішив піти з гри. До зустрічі, алхіміку!",
        }
        print("\n" + "=" * 60)
        print(texts.get(game["ending"], "Гру завершено."))
        print("=" * 60)
        print(f"Днів прожито: {game['day']}  |  Зілля зварено: {game['crafted']}  |  "
              f"Зароблено на продажах: {game['earned']}  |  Золота в кінці: {game['gold']}")
    except KeyError as error:
        print(f"[!] Не вдалося показати фінал: немає поля {error}")
