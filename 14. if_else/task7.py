"""Вводится список городов в одну строку через пробел.
Если в этом списке присутствует город Москва, то удалить его.
Вывести на экран результирующий список в виде строки с городами через пробел."""


lst = list(map(str, input().split()))
for i in lst:
    if 'Москва' in lst:
        lst.remove('Москва')
print(*lst)


lst = input().split()
if 'Москва' in lst:
    lst.remove('Москва')
print(*lst)

print(input().replace('Москва ', ''))

print(*[i for i in input().split() if i != 'Москва'])

print(input().replace('Москва', ' ').replace('  ', '').strip())