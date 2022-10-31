"""Вводятся оценки студента (целые числа от 2 до 5) в одну строчку через пробел.
На основе введенной строки формируется список командой: marks = list(map(int, input().split()))

Необходимо вычислить средний балл и вывести его на экран с точностью до десятых (один знак после запятой)."""


lst = list(map(int, input().split()))
print(round((sum(lst) / len(lst)), 1))

print(round(__import__('numpy').average(list(map(int, input().split()))), 1))

print(round((lambda x: sum(x) / len(x))([*map(int, input().split())]), 1))

print((lambda s: round(sum(s)/len(s), 1))([*map(int, input().split())]))

print(round(sum(nums := [int(i) for i in input().split()]) / len(nums), 1))