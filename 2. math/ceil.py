"""В летний лагерь нужно отвести n детей и m вожатых с помощью автобусов.
Максимальная вместимость каждого автобуса 20 человек.
Допишите программу для вычисления минимального числа автобусов, необходимых для перевозки детей вместе с вожатыми.
Результат выведите в консоль в виде целого числа."""

from math import ceil

n, m = map(int, input().split())
print(ceil((n + m) / 20))
