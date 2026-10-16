from tabulate import tabulate


def run_tabulate_demo():
    rows = [["Apple", 3], ["Pear", 5]]
    table = tabulate(rows, headers=["Fruit", "Qty"], tablefmt="grid")
    return f"[tabulate] Таблиця:\n{table}"
