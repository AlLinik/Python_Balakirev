"""Вводятся три целых положительных числа в одну строку через пробел.
Убедиться, что первые два числа - это катеты прямоугольного треугольника, а третье - его гипотенуза.
(Подсказка: проверка делается по теореме Пифагора c**2 = a**2 + b**2).
Если проверка проходит (истинна), то вывести на экран ДА, иначе - НЕТ."""


a, b, c = map(int, input().split())
print('ДА' if (a ** 2 + b ** 2 == c ** 2) else 'НЕТ')

print(('НЕТ', 'ДА')[int(*[a ** 2 + b ** 2 == c ** 2 for a, b, c in [map(int, input().split())]])])

(lambda a, b, c: print(['НЕТ', 'ДА'][a ** 2 + b ** 2 == c ** 2]))(*map(int, input().split()))

print((lambda a, b, c: ['ДА', 'НЕТ'][c * c != a * a + b * b])(*map(int, input().split())))
