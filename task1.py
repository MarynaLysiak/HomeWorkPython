# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a = input ("Введите трехзначное число: ")
a = int(a)
if a > 999 or a < 100: 
    print("Вы ввели не трехзначное число") 
else:
    print (a % 10 + (a % 100 // 10) + a // 100)
