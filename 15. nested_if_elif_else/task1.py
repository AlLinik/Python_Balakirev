"""Имеется следующее меню:

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

В программе вводится целое число от 1 до 6.
Нужно вывести пункт меню, связанный с этим числом.
Реализовать программу с использованием операторов if-elif"""

m = int(input())
if 0 < m <= 6:
    if m == 1:
        print('1. Введение в Python')
    elif m == 2:
        print('2. Строки и списки')
    elif m == 3:
        print('3. Условные операторы')
    elif m == 4:
        print('4. Циклы')
    elif m == 5:
        print('5. Словари, кортежи и множества')
    elif m == 6:
        print('6. Выход')