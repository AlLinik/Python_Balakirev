"""Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел.
Необходимо определить количество двоек и вывести это значение на экран."""


print(input().split().count('2'))

print(list(map(int, input().split())).count(2))

print(input().count('2'))

print(sum(char == '2' for char in input().split()))

