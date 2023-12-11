# Определить суммарную стоимость билетов мужчин на борту в возрастном интервале медиана ± 5 позиций
# Вариант 2 ИСТбд-23

import csv
# Считываем файл
file = open("titanic.csv", "r")
reader = list(csv.reader(file))

fare_counter = 0  # суммарная стоимость билетов
age_list = []  # список с возрастами

# Добавляем в список все значения возраста мужчин
for i in reader:
    if i[4] == "male" and i[5] != "" and i[5] != " ":
        age_list.append(float(i[5]))

# Сортируем список по возрастанию
sorted_age_list = sorted(age_list)

# Если список нечетный, то берем среднее из списка и вводим перменную для индекса
if len(sorted_age_list) % 2 != 0:
    median_age = sorted_age_list[((len(sorted_age_list) + 1) // 2)]
    index_median_age = (len(sorted_age_list) + 1) // 2

# Если список четный, то считаем среднее между двумя серединными элементами,
# добавляем его в список и вводим перменную для индекса
else:
    median_age = (sorted_age_list[(len(sorted_age_list) + 1) // 2] + sorted_age_list[(len(sorted_age_list) + 2) // 2]) / 2
    sorted_age_list.insert(((len(sorted_age_list) + 1) // 2), median_age)
    index_median_age = ((len(sorted_age_list) + 1) // 2)

# Вывод медианного возраста
print(f"Медианный возраст мужчин на борту: {median_age}")

# Берем срез значений из списка +- 5 позиций, считая от индекса медианного возраста
median_age_list = sorted_age_list[index_median_age - 5: index_median_age + 6]

# Вывод списка +- 5 позиций от медианного возраста
print("Список возрастов +- 5 позиций от медианного возраста", end = ": ")
print(*median_age_list, sep=", ")

# Если возраст в списке возрастов +- 5 позиций от медианного возраста,
# то прибавляем стоимость билета к переменной
for i in reader:
    if i[4] == "male" and i[5] != "" and i[5] != " ":
        if float(i[5]) in median_age_list:
            fare_counter += float(i[9])

# Вывод суммарной стоимость билетов
print(f"Суммарная стоимость билетов всех мужчин, возраст которых отличается от медианного не более чем на 5 позиций: {fare_counter}")
