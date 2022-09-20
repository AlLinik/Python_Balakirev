""" Вводятся: два целых числа в одну строку через пробел.
С помощью F-строки отобразить их по возрастанию в одну строку через пробел.
Результат вывести на экран.
P. S. Реализовать программу без использования условных операторов. Подумайте, как это можно сделать."""

print(*sorted(map(str, input().split())))

print(*sorted(input().split()))

print(*sorted(input().split(), key=int))

print(*sorted(list(map(int,input().split()))))

print("{0} {1}".format(*sorted(input().split())))


