"""Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3", если введенное число кратно 3,
а иначе присвоить строку "не кратно 3". Реализовать программу с использованием тернарного оператора.
Переменную msg отобразить на экране."""

print("кратно 3" if int(input()) % 3 == 0 else "не кратно 3")

print(['не ', ''][int(input()) % 3 == 0] + 'кратно 3')

print(f'{"не " * (1 if int(input()) % 3 > 0 else 0)}кратно 3')

print(['кратно 3', 'не кратно 3'][int(input()) % 3 > 0])

print(('не кратно 3', 'кратно 3')[not int(input()) % 3])
