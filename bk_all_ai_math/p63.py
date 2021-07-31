from sympy import *
x = Symbol('x')
y1 = expand((x + 2) * (x - 4))
print(y1)

y2 = factor(x**2 - 2*x - 8)
print(y2)


y1 = expand((x + 3) * (x + 4))
print(y1)

y2 = factor(x**2 + 7*x + 12)
print(y2)
