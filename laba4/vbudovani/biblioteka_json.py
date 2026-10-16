import os
import json


def run_json_demo():
    os.makedirs("output", exist_ok=True)
    path = "output/data.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"ok": True, "tags": ["lab", "python"]}, f, ensure_ascii=False, indent=2)
    return f"[json] Дані збережено у файл: {path}"
