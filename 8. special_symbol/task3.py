""" Вводится строка со словами, разделенными пробелом.
Необходимо первый пробел заменить на одинарную кавычку, а все остальные - на двойные.
Результирующую строку отобразить на экране."""


print(input().replace(' ', '\'', 1).replace(' ', '\"'))

print('"'.join(input().split()).replace('"', "'", 1))

print('\"'.join(input().replace(' ','\'',1).split()))

