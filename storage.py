import json
import os

DATA_FILE = "transactions.json"


def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_transactions(transactions):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            transactions,
            file,
            indent=4,
            ensure_ascii=False
        )