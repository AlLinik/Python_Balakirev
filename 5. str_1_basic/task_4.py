"""Написать программу ввода строки и формирования новой строчки вида:
"Строка: <введенная строка>. Длина: <длина строки>".
Результат сформированной строки вывести на экран."""

a = input()
print('Строка: ' + a + '. ' + 'Длина: ' + str(len(a)))

[print("Строка: " + s + ". Длина: " + str(len(s))) for s in [input()]]

print("Строка: ", s := input(), ". Длина: ", len(s), sep="")

(lambda x: print(f'Строка: {x}. Длина: {len(x)}'))(input())
