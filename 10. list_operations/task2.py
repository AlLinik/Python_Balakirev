"""Вводятся названия городов в одну строчку через пробел.
На основе этой строки формируется список с помощью команды: cities = input().split()

Необходимо проверить, присутствует ли в этом списке город "Москва".
Вывести на экран True, если присутствует и False - в противном случае.
Решить эту задачу следует без использования условного оператора."""

print(True if 'Москва' in map(str, input().split()) else False)

print('Москва' in input().split())

print("Москва" in list(map(str, input().split())))

print(True if 'Москва' in [i for i in map(str,input().split())] else False)

print('Москва' in input())