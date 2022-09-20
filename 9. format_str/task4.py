"""Вводится адрес (каждое значение с новой строки) в формате:
   город, улица, номер дома (целое число), номер квартиры (целое число).
Сформировать строку по шаблону:
   "г. <город>, ул. <улица>, д. <номер дома>, кв. <номер квартиры>", используя F-строку.
Результат вывести на экран."""

print(f'г. {input()}, ул. {input()}, д. {input()}, кв. {input()}')

print(', '.join([s+' '+input() for s in ['г.', 'ул.', 'д.', 'кв.']]))

print(*[f'г. {x[0]}, ул. {x[1]}, д. {x[2]}, кв. {x[3]}' for x in [[input() for _ in range(4)]]])

print('г. {}, ул. {}, д. {}, кв. {}'.format(*(input() for _ in range(4))))

[print(i, input(), end='') for i in ('г.', ', ул.', ', д.', ', кв.')]

