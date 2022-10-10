"""Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True".
Реализовать это с помощью тернарного условного оператора. Результат отобразить на экране."""

print('True' if int(input()) == 1 else 'False')

print(True if int(input()) else False)

print(bool(int(input())))

print(int(input()) == 1)

print(False if '0' in input() else True)
