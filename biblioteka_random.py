import random


def run_random_demo():
    pick = random.sample(["a", "b", "c", "d"], 2)
    return f"[random] Випадково обрано: {pick}"
