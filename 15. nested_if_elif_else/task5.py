"""Вводится порядковый номер месяца (1, 2, ..., 12).
Вывести на экран количество дней в этом месяце. Принять, что год не является високосным.
Реализовать через условный оператор, в котором следует использовать не более трех ветвей (блоков).

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31"""


a = int(input())
if 1 <= a <= 12:
    if a == 2:
        print(28)
    elif a in (1, 3, 5, 7, 8, 10, 12):
        print(31)
    else:
        print(30)

n = int(input())
if n == 2: print(28)
elif n in [4, 6, 9, 11]: print(30)
else: print(31)

year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
num = int(input())
if 1 <= num <= 12:
    print(year[num - 1])
else:
    print('Введите число от 1 до 12')

d1 = int(input())
print([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][d1 - 1])

print([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][int(input())])

print(__import__("calendar").monthrange(2022, int(int(input())))[1])

if (num := int(input())) == 2:
    print(28)
else:
    print(30 + (num // 8 + num) % 2)
