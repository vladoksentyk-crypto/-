import os
import seaborn as sns
import matplotlib.pyplot as plt


def run_seaborn_demo():
    os.makedirs("output", exist_ok=True)
    sns.set_theme(style="dark")
    data = [5, 7, 7, 8, 9, 10, 10, 10, 11, 12]

    plt.figure(figsize=(4, 2))
    sns.histplot(data, color="purple", kde=True)

    path = "output/chart_seaborn.png"
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return f"[seaborn] Статистичну діаграму збережено за шляхом: {path}"
