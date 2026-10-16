from colorama import Fore, Style, init


def run_colorama_demo():
    init()
    print(Fore.GREEN + "[colorama] Цей текст зелений" + Style.RESET_ALL)
    return "[colorama] Кольоровий текст виведено в консоль"
