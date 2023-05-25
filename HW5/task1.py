# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

a = int(input("Введите число a: "))
b = int(input("Введите его степень: "))


def degree (a, b):
    if a == 0:
        return a
    if a == 1:
        return 1
    if b == 0:
        return 1
    if a != 1:
        return (a * degree (a, b - 1))
    
print (degree(a, b))
    
            
