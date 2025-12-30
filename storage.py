import json
import os
from datetime import datetime

DATA_PATH = "data/sessions.json"

os.makedirs("data", exist_ok=True)

def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_session(session):
    data = load_data()
    data.append(session)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
