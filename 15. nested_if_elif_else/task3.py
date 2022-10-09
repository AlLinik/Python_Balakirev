"""Вводится вес боксера-любителя (в кг, в виде вещественного числа).
Известно, что вес таков, что боксер может быть отнесен к одной из весовых категорий:

1) легкий вес – до 60 кг (включительно);
2) первый полусредний вес – до 64 кг (включительно);
3) полусредний вес – до 69 кг (включительно);
4) остальные - более 69 кг.

Вывести на экран номер категории, в которой будет выступать боксер."""

a = float(input())
if a <= 60:
    print(1)
elif 60 < a <= 64:
    print(2)
elif 64 < a <= 69:
    print(3)
else:
    print(4)

x = float(input())
print(1 if x <= 60 else 2 if x <= 64 else 3 if x <= 69 else 4)

l = [0, 60, 64, 69]
a = float(input())
l.append(a)
l.sort()
print(l.index(a))

print(*[sorted([0, 60, 64, 69, x]).index(x) for x in [float(input())]])

a = float(input())
print([1, 2, 3, 4][(a > 60) + (a > 64) + (a > 69)])

weight = float(input())
print(1 + (60 <= weight) + (64 <= weight) + (69 <= weight))

w = float(input())
print((3 * (w > 69) or 2 * (w > 64) or (w > 60) or 0) + 1)

