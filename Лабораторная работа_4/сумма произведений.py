# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    product_of_number = [i["score"]*i["weight"] for i in json_data]
    summ = sum(product_of_number)
    summ = round(summ, ndigits=3)
    return summ

print(task())
