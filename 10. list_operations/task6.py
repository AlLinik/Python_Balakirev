"""Вводится число новых подписчиков канала по дням в одну строку через пробел.
На основе введенной строки необходимо сформировать список из целых чисел.
Затем, вывести на экран максимальное, минимальное и суммарное значения этого списка через пробел."""

lst = [i for i in map(int, input().split())]
print(max(lst), min(lst), sum(lst))

print(*[f'{max(x)} {min(x)} {sum(x)}' for x in [list(map(int, input().split()))]])

(lambda x: print(max(x), min(x), sum(x)))(list(map(int, input().split())))

print(max(l := list(map(int, input().split()))), min(l), sum(l))

print(*[f(a) for f, a in zip([max, min, sum], [list(map(int, input().split()))]*3)])