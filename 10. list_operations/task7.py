"""Вводится число новых подписчиков канала по дням в одну строку через пробел.
На основе введенной строки необходимо сформировать список lst из целых чисел.
Требуется отсортировать элементы этого списка по убыванию и результат вывести на экран командой: print(*lst)"""

print(*(sorted(list(map(int, input().split())), reverse=True)))

print(*sorted(input().split(), key=int, reverse=True))

print(*sorted(input().split(), key=int)[::-1])

