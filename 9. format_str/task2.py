"""Вводятся: габариты изделия (целые числа): ширина, глубина, высота - в одну строчку через пробел.
С помощью метода format, используя ключи в качестве имен переменных,
сформировать строку: "Габариты: <ширина> x <глубина> x <высота>".
Результат вывести на экран."""


print('Габариты: {0} x {1} x {2}'.format(*map(str, input().split())))

print("Габариты: {} x {} x {}".format(*input().split()))

print(f"Габариты: {input().replace(' ', ' x ')}")

