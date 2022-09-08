""" Напишите программу ввода двух слов через пробел.
Сформируйте новую строку, продублировав первое слово дважды,
а второе - трижды (все слова в результирующей строке должны идти через пробел).
Результат выведите на экран. """

a, b = map(str, input().split())
print(a + ' ' + a + ' ' + b + ' ' + b + ' ' + b)  # print((a + ' ') * 2 + (b + ' ') * 3)

a, b = input().split()
print(a, a, b, b, b)

a = input().split()
print(a[0], a[0], a[1], a[1], a[1])

s = input().split()
print((s[0] + ' ') * 2, (s[1] + ' ') * 3, sep='')

a, b = input().split()
print(' '.join([a] * 2 + [b] * 3))

(lambda a, b: print(*[a] * 2, *[b] * 3))(*input().split())

(lambda x: print((x[0] + ' ') * 2, ((x[1] + ' ') * 3).rstrip(), sep=''))(input().split())
