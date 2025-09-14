import json
import re

def load_memory(file_path="data/memory.json"):
    with open(file_path, "r") as f:
        data = json.load()
        
    flat_data = []
    for item in data:
        if isinstance(item, list):
            flat_data.extend(item)
        else:
            flat_data.append(item)
    return flat_data

def preprocess(text):
    text = text.lower().strip()
    text = re.sub("r[^a-z0-9\s]", "", text)
    return text        