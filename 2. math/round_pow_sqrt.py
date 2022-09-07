import math

a, b = map(int, input().split())
c = math.sqrt(pow(a, 2) + pow(b, 2))   # c = (a ** 2 + b ** 2) ** 0.5
print(round(c, 2))
