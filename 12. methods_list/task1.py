"""Вводится строка из целых чисел через пробел.
Если первое число не равно последнему, то нужно добавить значение True, а иначе - значение False.
Результирующий список lst вывести на экран командой: print(*lst)
Реализовать задачу без использования условных операторов."""

lst = list(map(int, input().split()))
print(*(lst + [lst[0] != lst[-1]]))

a = list(map(int, input().split()))
a.append([False, True][a[0] != a[-1]])
print(*a)

lst = input().split()
lst.append(lst[0] != lst[-1])
print(*lst)

[print(*i, i[0] != i[-1]) for i in [input().split()]]

(lambda s: print(*s, s[0] != s[-1]))(*[input().split()])

(lambda lst: print(*lst, lst[0] != lst[-1]))(input().split())

(lambda lst: print(*lst + [lst[0] != lst[-1]]))(list(map(int, input().split())))

