import os


class Const:
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    TARGET_PROJECT_ID = "2318959463"

    KEYS_PATH = os.path.join(CURRENT_DIR, "keys.txt")
    INFO_PATH = os.path.join(CURRENT_DIR, "info.json")
