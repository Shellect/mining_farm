import json


def load_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return sorted(data, key=lambda x: x['sender'], reverse=False)
