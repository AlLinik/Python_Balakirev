"""Напишите программу, которая принимает на вход два вещественных числа в одну строку через пробел
и выводит на экран их сумму."""

# ВАРИАНТ 1

a, b = map(float, input().split())
print(a + b)

# ВАРИАНТ 2

print(sum(map(float, input().split())))