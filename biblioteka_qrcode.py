import os
import qrcode


def run_qrcode_demo():
    os.makedirs("output", exist_ok=True)
    path = "output/qr_code.png"
    qrcode.make("https://example.com").save(path)
    return f"[qrcode] QR-код збережено за шляхом: {path}"
