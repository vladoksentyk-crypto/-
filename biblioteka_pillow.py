import os
from PIL import Image, ImageDraw


def run_pillow_demo():
    os.makedirs("output", exist_ok=True)
    img = Image.new("RGB", (200, 100), "navy")
    ImageDraw.Draw(img).text((20, 40), "Hello PIL", fill="white")

    path = "output/image_pillow.png"
    img.save(path)
    return f"[pillow] Зображення створено і збережено: {path}"
