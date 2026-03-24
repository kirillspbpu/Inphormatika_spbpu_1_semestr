def find_common_participants(group1, group2, separator=','):  # принимает две строки и разделитель
    list1 = group1.split(separator)  # разбиваем первую и вторую строки
    list2 = group2.split(separator)
    set1 = set(list1)  # преобразуем обе строки в множество
    set2 = set(list2)
    common_set = set1.intersection(set2)  # затем находим пересечение методом
    common_list = sorted(list(common_set))  # сортируем результат функцией

    return common_list  # возвращаем функцию
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:", participants)