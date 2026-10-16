import os


def run_os_demo():
    files = os.listdir(".")
    return f"[os] Файлів і папок у поточній директорії: {len(files)}"
