"""Вводится шестизначное число. Определить, является ли оно счастливым.
(Счастливым называют такое шестизначное число,
в котором сумма его первых трех цифр равна сумме его последних трех цифр.).
Вывести ДА, если счастливое и НЕТ - в противном случае."""


n = list(map(int, input()))
print('ДА' if sum(n[0:3]) == sum(n[3:]) else 'НЕТ')


n = [int(i) for i in input()]
print(['НЕТ', 'ДА'][sum(n[:3]) == sum(n[3:])])


i = [int(i) for i in input()]
print("ДА" if sum(i[:int(len(i) / 2)]) == sum(i[int(len(i) / 2):]) else "НЕТ")


n = int(input())
if (n % 10 + n % 100 // 10 + n % 1000 // 100) == (n // 100000 + n // 10000 % 10 + n // 1000 % 10):
    print("ДА")
else:
    print("НЕТ")


num = input()
print('ДА' if sum(map(int, list(num[:3]))) == sum(map(int, list(num[3:]))) else 'НЕТ')