"""Вводится слово. Проверить, что в этом слове присутствуют все три буквы: t, h и o (в произвольном порядке).
Реализовать программу с помощью одного условного оператора.
Если проверка проходит, вывести ДА, иначе - НЕТ."""


a = input(); print('ДА' if 't' in a and 'h' in a and 'o' in a else 'НЕТ')

print('ДА' if {'t', 'h', 'o'} <= set(input()) else 'НЕТ')

print(('НЕТ', 'ДА')[set(input()).issuperset(set('tho'))])

print(['НЕТ', 'ДА'][{'t', 'h', 'o'}.issubset(input().lower())])

print('ДА' if set('hot') < set(input()) else 'НЕТ')

