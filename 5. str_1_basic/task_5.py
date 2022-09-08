"""Написать программу ввода двух слов (через пробел в одну строчку).
Определить булевы значения для оператора in проверки вхождения первого слова во второе.
А также для операторов ==, >, <.
Все булевы значения объединить в одну строку через пробел и вывести на экран."""

a, b = map(str, input().split())
print(a in b, a == b, a > b, a < b)

a, b = input().split(); print(a in b, a == b, a > b, a < b)

a, b = map(str, input().split())
print(bool(b == a), bool(a in b), bool(a > b), bool(a < b))

(lambda x, y: print(x in y, x == y, x > y, x < y))(*input().split())

[print(a in b, a == b, a > b, a < b) for a, b in [input().split()]]
