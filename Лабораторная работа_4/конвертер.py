# TODO импортировать необходимые модули
import json
import csv
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        with open(OUTPUT_FILENAME, 'w') as new_file:
            for row in reader:
                conclusion = json.dump(row, new_file, indent=4, ensure_ascii=False)
                list.append(conclusion)
        return list
          # Чтение данных
      # TODO считать содержимое csv файла

      # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
