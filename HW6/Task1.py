# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1 = int(input("Введите первый элемент списка: "))
n = int(input("Введите количество элементов в списке: "))
d = int(input("Введите разницу элементов: "))
numbers = []

for i in range (1, n+1):    
    val = a1 + (i-1) * d
    numbers.append(val)
    i += 1

print(numbers)