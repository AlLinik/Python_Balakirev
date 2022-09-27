"""Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом.
Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел."""

a, b, c = input().split(), input().split(), input().split()
print(a[-1], b[-1], c[-1])

print(input().split()[-1], input().split()[-1], input().split()[-1])

print(*[input().split()[-1] for _ in range(3)])

print(*list(zip(*[input().split() for _ in range(3)]))[3])

[print(input().split()[-1], end=' ') for _ in range(3)]

print(*[input().split().pop() for x in range(3)])