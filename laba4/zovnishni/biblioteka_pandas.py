import os
import pandas as pd


def run_pandas_demo():
    os.makedirs("output", exist_ok=True)
    df = pd.DataFrame({"name": ["Ann", "Bob", "Kate"], "age": [21, 25, 19]})
    df = df.sort_values("age")

    path = "output/table_pandas.csv"
    df.to_csv(path, index=False)
    return f"[pandas] Таблицю відсортовано за віком і збережено: {path}"
