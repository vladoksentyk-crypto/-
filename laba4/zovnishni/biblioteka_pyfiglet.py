import pyfiglet


def run_pyfiglet_demo():
    banner = pyfiglet.figlet_format("Lab")
    print(banner)
    return "[pyfiglet] Текстовий банер виведено вище"
