"""Вводятся три строчки стихотворения (каждая с новой строки).
Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом).
Результирующий список lst вывести на экран командой: print(lst)"""

print([input().split()] + [input().split()] + [input().split()])

print([input().split() for _ in 'i' * 3])

print([input().split() for i in range(3)])
