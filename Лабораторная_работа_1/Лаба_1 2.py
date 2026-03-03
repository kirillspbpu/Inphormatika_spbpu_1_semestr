a_mb = 1.44
a_b = a_mb * 1024 * 1024 # нашли сколоко битов в 1,44 Мб
number_list = 100
number_srt_str = 50
number_sim_str = 25
ves_sim = 4

ves_stro = ves_sim * number_sim_str # Нашли сколько б в одной строке
ves_stron = ves_stro * number_srt_str # Нашли сколько б в одной странице
ves_book = ves_stron * number_list # Нашли сколько б в одной книге
book = a_b // ves_book # Нашли сколько целых книг влезает в количесво б
print("Количество книг, помещающихся на дискету:", int(book))
