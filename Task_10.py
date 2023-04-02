# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Введите количество монеток: "))
one = 0
zero = 0
for i in range(n):
    coin = int(input("Введите значение 1 или 0: "))
    if coin == 0:
        zero += 1
    else:
        one += 1
if zero < one:
    print(zero)
else:
    print(one)

    