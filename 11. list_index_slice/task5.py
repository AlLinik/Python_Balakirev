"""Имеется список с оценками студента: m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
Необходимо с помощью срезов выбрать элементы с 3-го по 7-й (включительно) и вывести их на экран в обратном порядке."""

print(([2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4][2:7])[::-1])

print(list(reversed([2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4][2:7])))

print([2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4][6:1:-1])