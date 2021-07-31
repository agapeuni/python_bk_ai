from sympy import symbols

def avg(a,b):
    m = max(a, b)
    n = min(a, b)
 
    x = symbols('x')
    fx = 2 * x ** 2 + 4 * x + 7
    fb = fx.subs(x, m)
    fa = fx.subs(x, n)

    result = (fb - fa) / (b - a)
    return result

print(avg(0, 2))   

