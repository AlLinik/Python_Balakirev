# ВАРИАНТ 1

x, y = map(int, input().split())
print(3 * x + 5 * y )

# ВАРИАНТ 2

print((lambda b, g: b + g + 2 * b + 4 * g)(*map(int, input().split())))

# ВАРИАНТ 3

print((lambda x, y: x * 3 + y * 5)(*map(int, input().split())))