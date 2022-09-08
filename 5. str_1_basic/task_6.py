"""С клавиатуры вводятся две буквы (в одну строку через пробел).
Вывести на экран следующую строку: "Коды: <буква1> = <код буквы1>, <буква2> = <код буквы2>"""

a, b = map(str, input().split())
print(f'Коды: {a} = {ord(a)}, {b} = {ord(b)}')

print('Коды:', ', '.join([f'{i} = {ord(i)}' for i in input().split()]))

(lambda x, y: print(f'Коды: {x} = {ord(x)}, {y} = {ord(y)}'))(*input().split())

[print(f"Коды: {a} = {ord(a)}, {b} = {ord(b)}") for [a,b] in [input().split()]]


