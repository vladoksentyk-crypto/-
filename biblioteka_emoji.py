import emoji


def run_emoji_demo():
    text = emoji.emojize("Python is :thumbs_up: and :snake:")
    return f"[emoji] {text}"
