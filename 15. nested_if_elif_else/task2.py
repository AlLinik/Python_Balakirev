"""Вводятся три целых числа в одну строку через пробел.
Необходимо определить наименьшее среди них и вывести его на экран.
Реализовать программу, используя условный оператор, без использования функции min."""

a, b, c = map(int, input().split())
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)


a, b, c = map(int, input().split())

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)


a, b, c = map(int, input().split())
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
print(a)


a, b, c = map(int, input().split())
if a > b:
    a = b
if a > c:
    a = c
print(a)


# Линейная интерполяция
a, b, c = map(int, input().split())
a += (b - a) * (a > b)
a += (c - a) * (a > c)
print(a)


print(sorted(map(int, input().split()))[0])

print(sorted([int(x) for x in list(input().split())])[0])

print(min(list(map(int,input().split()))))