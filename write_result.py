import json


def write_item_to_file(item):
    with open('makeup.json', 'w', encoding='utf-8') as file:
        json.dump(item, file, ensure_ascii=False, indent=4)