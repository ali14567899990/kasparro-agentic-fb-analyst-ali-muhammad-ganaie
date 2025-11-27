import os
import json

def ensure_dirs(paths):
    for p in paths:
        os.makedirs(p, exist_ok=True)

def save_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def timestamped_log(path, data):
    save_json(data, path)
