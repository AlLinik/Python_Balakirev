'''Напишите программу ввода двух строк (каждая вводится с новой строки)
и их объединения в одну строку через пробел. Результат выведите на экран.'''

print(f'{input()} {input()}')

print(input(), input())

print(input(), input(), sep=' ')

print(*[input() for i in range(2)])

print((lambda a, b, c: a + b + c)(a=input(), b=' ', c=input(' ')))
