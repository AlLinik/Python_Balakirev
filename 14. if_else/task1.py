"""Вводятся два вещественных числа в одну строку через пробел.
Вывести на экран наибольшее из чисел.
Задачу решить с помощью условного оператора."""

a, b = map(float, input().split())
print(a if a > b else b)

a, b = map(float, input().split())
if a < b:
    a, b = b, a
print(a)

print(max(float(i) for i in input().split()))

print(max(input().split(), key=float))

a, b = [float(i) for i in input().split()]
print((a, b)[b > a])

a = list(map(float, input().split()))
print(a[0] if a[0] > a[1] else a[1])

(lambda x, y: print(x if x > y else y))(*map(float, input().split()))
