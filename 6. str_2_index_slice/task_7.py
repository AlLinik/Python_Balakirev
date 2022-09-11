"""Вводятся два слова (через пробел в одной строке). Длина первого слова меньше второго.
Необходимо обрезать второе слово до длины первого и отобразить обрезанное слово на экране."""

a, b = map(str, input().split());
print(b[:len(a)])

a, b = input().split()
print(b[:len(a)])

[print(b[:len(a)]) for a, b in [input().split()]]

[print(c, end='') for a, c in zip(*input().split())]

print(*[j[1][: len(j[0])] for j in [[i for i in input().split()]]])

print(*[x[1][:len(x[0])] for x in [input().split(' ')]])

