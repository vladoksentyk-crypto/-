import numpy as np


def run_numpy_demo():
    arr = np.array([3, 7, 1, 9, 5])
    return f"[numpy] Середнє: {arr.mean()}, максимум: {arr.max()}, відхилення: {arr.std():.2f}"
