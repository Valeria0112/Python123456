# TODO решите задачу
import json

def task() -> float:
    with open('input.json') as json_file:
        data = json.load(json_file)
    total_product = 0
    for item in data:
        score = item.get('score')
        weight = item.get('weight')
        product = score * weight
        total_product += product
    return round(total_product, 3)


print(task())
