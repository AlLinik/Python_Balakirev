"""Допишите текст программы для нахождения минимального значения из пяти введенных целых чисел
с выводом результата в консоль с помощью функции print."""


# ВАРИАНТ 1
print(min(map(int, input().split())))

# ВАРИАНТ 2
print(min([int(i) for i in input().split()]))
