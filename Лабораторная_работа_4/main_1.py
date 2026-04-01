
import json  # Импортируем  json чтобы работать с JSON форматом

def task() -> float:  # Объявляем функцию task, которая возвращает число с плавающей точкой
    name = "input.json"  # Задаем имя файла из которого будем читать данные
    with open(name) as file:  # Открываем файл  file - это файловый объект
        json_data = json.load(file)  # Загружаем содержимое файла в переменную json_data, преобразуя JSON в Python объект (список словарей)
    sum_v = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_v, 3)  # возврощаем переменную
print(task())

# Создаем список произведений score * weight для каждого элемента, затем суммируем все значения
# item["score"] - берем значение "score"
# item["weight"] - берем значение "weight"
# [item["score"] * item["weight"] for item in json_data] - генератор списка
