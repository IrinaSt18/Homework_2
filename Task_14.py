# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
number = int(input("Введите число: "))
count = 1
while count < number:
    print(count)
    count = count*2