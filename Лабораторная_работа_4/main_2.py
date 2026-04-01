import csv  # Импортируем для работы с CSV
import json  # Импортируем для работы с JSON
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None: # Открываем CSV файл
    with open(INPUT_FILENAME) as file_csv: # Считываем все строки, превращаем в словаь
        rows = [row for row in csv.DictReader(file_csv)]
    with open(OUTPUT_FILENAME, "w") as file_json: # Записываем данные в JSON форма
        json.dump(rows, file_json, indent=4)         # indent=4 добавляет отступы
if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:  # Построчно выводим содержимое файла
            print(line, end="")  # end="" убирает лишний перевод строки