# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

min_range = int(input("Введите нижний предел диапазона проверки: "))
max_range = int(input("Введите верхний предел диапазона проверки: "))

from random  import randint
numbers = [randint (-20, 20) for i in range (10)]
print(numbers)
indexes_result = []

for i in range (len(numbers)):
    if min_range <= numbers[i] <= max_range:
        indexes_result.append(i)
    i += 1
print(indexes_result)




