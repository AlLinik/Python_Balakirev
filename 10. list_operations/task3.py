"""Вводятся названия городов в одну строчку через пробел.
На основе этой строки формируется список с помощью команды: cities = input().split()

Необходимо вывести значение последнего элемента этого списка на экран."""


print(input().split()[-1])

print([i for i in map(str, input().split())][-1])

print(input().split().pop())