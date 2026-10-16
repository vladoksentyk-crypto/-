from datetime import datetime


def run_datetime_demo():
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return f"[datetime] Поточний час: {now}"
