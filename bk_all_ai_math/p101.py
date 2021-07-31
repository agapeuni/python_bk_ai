from sympy import Limit, S, Symbol

x = Symbol('x')
a = Limit(1/x, x, S.Infinity).doit()
print(a)

b = Limit(1/x, x, 0).doit()   
print(b)

c = Limit(1/x, x, 0, dir='-').doit()  # 좌극한 값 구하기 
print(c)