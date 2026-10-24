# Введення від гравця: читання клавіш і безпечне введення чисел.

import sys

from config import USE_INSTANT_KEYS
from exceptions import InvalidChoiceError

try:
    import msvcrt  # є тільки у Windows
except ImportError:
    msvcrt = None

# Якщо увімкнена українська розкладка, клавіші I, C, R, E, H, Q дають інші літери.
# Цей словник перетворює їх назад, щоб гра працювала в обох розкладках.
LAYOUT_MAP = {"ш": "i", "с": "c", "к": "r", "у": "e", "р": "h", "й": "q", "ф": "a"}


def read_key():
    """Читає одну клавішу. Якщо консоль підтримує - без Enter, інакше - літера + Enter."""
    try:
        if USE_INSTANT_KEYS and msvcrt is not None and sys.stdin.isatty():
            key = msvcrt.getwch()
            if key in ("\x00", "\xe0"):      # службова клавіша (стрілки тощо)
                msvcrt.getwch()
                return ""
            if key == "\x03":                # Ctrl+C
                raise KeyboardInterrupt
        else:
            key = input("> ").strip()[:1]
        key = key.lower()
        return LAYOUT_MAP.get(key, key)
    except EOFError:
        return "q"


def ask_number(prompt, minimum, maximum):
    """Питає число в діапазоні [minimum, maximum], поки гравець не введе правильно."""
    while True:
        try:
            number = int(input(prompt).strip())
            if number < minimum or number > maximum:
                raise InvalidChoiceError(f"Введіть число від {minimum} до {maximum}")
            return number
        except ValueError:
            print("[!] Потрібно ввести ціле число.")
        except InvalidChoiceError as error:
            print(f"[!] {error}")


def wait_enter():
    """Пауза, щоб гравець встиг прочитати текст."""
    try:
        input("\nНатисни Enter, щоб продовжити...")
    except EOFError:
        pass
