import requests


def run_requests_demo():
    req = requests.Request("GET", "https://example.com/search", params={"q": "python", "page": 2})
    url = req.prepare().url
    return f"[requests] Сформовано URL-адресу: {url}"
