# ВАРИАНТ 1

import math
n, k = map(int, input().split())
print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))

# ВАРИАНТ 2

from math import factorial

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))

# ВАРИАНТ 3

from math import factorial as f

n, k = map(int, input().split())
print(f(n) // (f(k) * f(n - k)))

