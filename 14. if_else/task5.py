"""Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7.
Вывести на экран ДА, если это так и НЕТ - в противном случае."""


print('ДА' if input()[-1] == '7' else 'НЕТ')

print(['НЕТ', 'ДА'][input()[-1] == '7'])

print('ДА' if int(input()) % 10 == 7 else 'НЕТ')

print('ДА') if input().endswith('7') else print('НЕТ')

print('ДА' if (a := int(input())) % 10 == 7 else 'НЕТ')
