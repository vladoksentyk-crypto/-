# Точка входу: гра "Алхімік". Запуск: python main.py

from config import GOAL_GOLD, MAX_DAYS, START_INGREDIENTS
from crafting import crafting_menu
from daily import end_day, give_ingredients, start_new_day
from display import show_help, show_recipes, show_status
from endings import show_ending
from exceptions import GameError, InvalidChoiceError
from game_state import new_game
from input_utils import ask_number, read_key
from inventory_menu import inventory_menu


def intro(game):
    """Вступ і стартовий набір інгредієнтів."""
    print("=" * 70)
    print("                         АЛХІМІК")
    print("=" * 70)
    print(f"Ти починаєш кар'єру алхіміка. Мета: {GOAL_GOLD} золота за {MAX_DAYS} днів.")
    received, _ = give_ingredients(game, START_INGREDIENTS)
    print("Стартовий набір: " + ", ".join(received))


def handle_key(game, key):
    """Виконує дію за натиснутою клавішею."""
    if key == "i":
        inventory_menu(game)
    elif key == "c":
        crafting_menu(game)
    elif key == "r":
        show_recipes(game)
    elif key == "e":
        end_day(game)
    elif key == "h":
        show_help()
    elif key == "q":
        if ask_number("Точно вийти? 1 - так, 0 - ні: ", 0, 1) == 1:
            game["ending"] = "quit"
    else:
        raise InvalidChoiceError(f"Клавіша '{key}' не використовується. Натисни H для допомоги.")


def game_loop(game):
    """Головний цикл: показує стан, чекає клавішу, виконує дію - поки не настане фінал."""
    while game["ending"] is None:
        show_status(game)
        key = read_key()
        try:
            handle_key(game, key)
        except GameError as error:
            print(f"[!] {error}")
        except ValueError as error:
            print(f"[!] Внутрішня помилка даних: {error}")


def main():
    try:
        game = new_game()
        intro(game)
        start_new_day(game)
        game_loop(game)
        show_ending(game)
    except KeyboardInterrupt:
        print("\nГру перервано. До зустрічі!")
    except EOFError:
        print("\nВведення завершено.")
    except Exception as error:
        print(f"\n[КРИТИЧНА ПОМИЛКА] {type(error).__name__}: {error}")
    finally:
        print("Дякуємо за гру!")


if __name__ == "__main__":
    main()
