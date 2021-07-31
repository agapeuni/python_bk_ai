from sympy import Derivative, symbols
x = symbols('x')
fx = 2 * x ** 2 + 4 * x + 7

fprime = Derivative(fx, x).doit() 
n = fprime.subs({x: 3})

print("fx에서 x = 3 에서의 순간변화율(미분계수는) ", n , "입니다")