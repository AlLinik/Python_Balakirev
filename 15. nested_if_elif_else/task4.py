""""Вводится порядковый номер дня недели (1, 2, ..., 7).
Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье).
Программу реализовать с использованием операторов if-elif."""

a = input()
if a == '1':
    print('понедельник')
elif a == '2':
    print('вторник')
elif a == '3':
    print('среда')
elif a == '4':
    print('четверг')
elif a == '5':
    print('пятница')
elif a == '6':
    print('суббота')
elif a == '7':
    print('воскресенье')


tag = int(input())
sp = ['', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
if 0 < tag < 8:
    print(sp[tag])
elif 8 < tag < 0:
    print('Ввод неверный')


d1 = int(input())
print(['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'][d1-1])

print(', понедельник, вторник, среда, четверг, пятница, суббота, воскресенье'.split(', ')[int(input())])

print(('понедельник','вторник','среда','четверг','пятница','суббота','воскресенье')[int(input())-1])

week = {1: 'понедельник',
       2: 'вторник',
       3: 'среда',
       4: 'четверг',
       5: 'пятница',
       6: 'суббота',
       7: 'воскресенье'}
day = int(input())
print(week[day])

