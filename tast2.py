# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *

x = int(input("Задуманное Петей число x: "))
y = int(input("Задуманное Петей число y: "))
print(f'Петя дает подсказку - сумма числе {x+y}, произведение {x*y}')

for i in range(1000):
    for j in range(1000):
        if i+j == x+y and i*j == x*y:
            q = i
            w = j
print(f'Катя отгадала числа - {q} и {w}')





