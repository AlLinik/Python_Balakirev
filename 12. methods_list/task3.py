"""Вводится строка с номером телефона в формате: +7(xxx)xxx-xx-xx
Необходимо преобразовать ее в список lst
(посимвольно, то есть, элементами списка будут являться отдельные символы строки).
Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. Отобразить полученный список на экране командой:
print("".join(lst))"""

lst = []
for i in input():
    lst.append(i)
lst.remove('+')
lst.remove('-')
lst.remove('-')
lst[0] = '8'
print("".join(lst))

print(input().replace('+7', '8').replace('-', ''))

print(''.join(list(input().replace('-', '').replace('+7', '8'))))

print('8' + input()[2:].replace('-', ''))

print('8' + "".join(list(input())[2::]).replace('-', ''))

print(''.join(['8'] + [i for i in input() if i.isdigit() or i != '-'][2:]))

print(*[input().replace('-', '').replace('7', '8', 1)[1:]])
