
# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input("введите число, которое нельзя превосходить: "))

for i in range(n):
    while 2**i <= n:
        print(2**i)
        break

