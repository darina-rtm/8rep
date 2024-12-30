# Пример кортежа с оценками
grades = (5, 5, 5, 4, 3, 5, 2, 5)  # замените на свой кортеж

# Подсчитываем количество пятерок в начале кортежа
count_of_fives = grades.index(next((grade for grade in grades if grade != 5), None))

# Если все элементы 5, то index() вернет длину всего кортежа
if count_of_fives == len(grades):
    count_of_fives = len(grades)

print("Количество учеников с оценкой '5':", count_of_fives)
