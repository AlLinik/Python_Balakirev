""" Вводятся три целых числа в одну строку через пробел. Сформируйте список lst, 
хранящий эти значения в порядке их ввода. Результат выведите на экран, используя команду: print(lst)"""


print(list(map(int, input().split())))

print([int(x) for x in input().split()])

print([i for i in map(int, input().split())])
