from sympy import *
x = Symbol('x')
y = Symbol('y')

eq1 = 3 * x + y - 2
eq2 = x - 2 * y -3

print(solve((eq1, eq2), dict=True))
