"""Вводится два вещественных числа, каждое с новой строки.
Необходимо с помощью тернарного условного оператора
наибольшее значение присвоить переменной d и вывести ее на экран."""

a, b = float(input()), float(input())
print(a if a > b else b)

print(a if (a := float(input())) > (b := float(input())) else b)

[a := float(input()), b := float(input()), d := [a if a > b else b], print(*d)]

print(max(float(input()), float(input())))

print(d := (a if (a := float(input())) > (b := float(input())) else b))

print((d := max([float(input()) for i in range(2)])))

(lambda a, b: print(a if a > b else b))(float(input()), float(input()))

