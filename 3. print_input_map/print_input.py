# ВАРИАНТ 1
print(2 * (float(input()) + float(input())))

# ВАРИАНТ 2
print(sum(float(input()) for _ in range(2)) * 2)

# ВАРИАНТ 3
print((lambda x, y: (x + y) * 2)(*[float(input()) for _ in range(2)]))