'''
Короче надо написать функцию add(n), которая принимает число, при обращении 
к ней без вызова будет возвращать число, а при множественном вызове будет 
суммировать числа, чекай пример ниже броще, братец.

add(1)(2)(3) # 6
add(1)(2)(3)(4); # 10
add(1)(2)(3)(4)(5) # 15

addTwo = add(2)
addTwo # 2
addTwo + 5 # 7
addTwo(3) # 5
addTwo(3)(5) # 10
'''
from functools import total_ordering

def add(n):
    @total_ordering
    class Number():
        def __init__(self, n, parent=None, total=None):
            self.parent = parent
            self.total = total
            self.number = n

        def __call__(self, *args, **kwds):
            if self.parent is None:
                return Number(self.number+int(args[0]), parent=self)
            return Number(self.number + int(args[0]))

        def __int__(self):
            return self.number
        
        def __str__(self):
            return str(self.number)

        def __add__(self, other):
            return self.number + other
        
        def __eq__(self, value):
            return int(self) == int(value)
        
        def __lt__(self, other):
            return int(self) < int(other)
        
    return Number(n)

a = add(5)
assert not (a == 6)
assert a == 5
b = a(a)
assert not (b == 9)
assert b == 10
c = a(6)
assert not (c == 10)
assert c == 11
d = c(0)
assert not (d == 10)
assert d == 11
e = add(7) # 7
assert e == 7
assert not (e == 6)
f = e(3)
assert not (f == 9)
assert f == 10
g = c(2) # 13
assert not (g == 12)
assert g == 13
h = g(a)
assert h == 18
assert not (h == 17)
i = d(c)
assert i == 22
assert not (i == 21)
j = i(7)
assert not (j == 28)
assert j == 29
k = e + 0
assert not (k == 6)
assert k == 7
l = g(e)

a = add(4)
assert a == 4
assert not (a == 3)
b = a(7)
assert b == 11
assert not (b == 12)
c = b(6)
assert c == 17
assert not (c == 16)
d = c(b)
assert not (d == 27)
assert d == 28
e = b(0)
assert e == 11
assert not (e == 12)
f = e + 3
assert f == 14
assert not (f == 13)
g = a(3)
assert g == 7
assert not (g == 6)
h = d(b)
assert not (h == 40)
assert h == 39
i = add(3)
assert i == 3
assert not (i == 2)
j = c(7)
assert j == 24
assert not (j == 25)
k = i(g)
assert k == 10
assert not (k == 11)
l = j(b)
assert not (l == 34)
assert l == 35
m = e(4)
assert not (m == 14)
assert m == 15
n = k(c)

# POLUCHILA SUCHKA