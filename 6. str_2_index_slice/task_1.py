"""Напишите программу ввода строки и отображения на экране ее первого и последнего символа в виде одной строки."""


a = input(); print(a[0] + a[-1])

(lambda l: print(''.join((l[0], l[-1]))))(input())

print((x := input())[0] + x[-1])

print(*[f'{x[0]}{x[-1]}' for x in [input()]])

print((value:= input())[0] + value[-1])