from sympy import *
x = Symbol('x')
y = Symbol('y')

eq1 = 2 * x + y - 2
eq2 = x - y + 1

print(solve((eq1, eq2), dict=True))
