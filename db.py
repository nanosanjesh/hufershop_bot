import json
from pathlib import Path

BASE_DIR = Path(__file__).parent / 'data'
BASE_DIR.mkdir(exist_ok=True)

USERS_FILE = BASE_DIR / 'users.json'
PRODUCTS_FILE = BASE_DIR / 'products.json'
CARTS_FILE = BASE_DIR / 'carts.json'

def load_json(path):
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
