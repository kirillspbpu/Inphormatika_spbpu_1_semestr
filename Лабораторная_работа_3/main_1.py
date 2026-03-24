
def find_item_index(items_list, item_to_find): # функция котроя примимает аргумент: список товара и товар, ищем
    for index, item in enumerate(items_list):      # идем по списку с идексами
        if item == item_to_find: # если мы нашли нужный товар возвращаем индекс первого вхождения
            return index
    return None  # если не нашли, возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:   # перебираем товары для поиска
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:       # если товар найден
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:         # если товар не найден
        print(f"Товар '{find_item}' не найден в списке.")