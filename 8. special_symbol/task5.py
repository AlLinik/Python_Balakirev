""" Вводится слово. Необходимо сформировать новую строку,
где введенное слово будет заключено в двойные кавычки.
Результат выведите на экран."""

print(f'"{input()}"')

print('"' + input() + '"')

print(input().join('""'))

print('"','"', sep=input())

print("\"" + input() + "\"")