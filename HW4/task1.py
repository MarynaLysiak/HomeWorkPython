# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого списка: "))
m = int(input("Введите количество элементов второго списка: "))

from random import randint
numbers1 = [randint(0, 10) for i in range (n)]
numbers2 = [randint(0, 10) for i in range (m)]

print (numbers1)
print (numbers2)



numbers_res = []
for i in numbers1: 
    for j in numbers2:
        if i == j:
            numbers_res.append(i)

numbers_res.sort()
res = set(numbers_res)

print (res)
            
