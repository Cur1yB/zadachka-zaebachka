'''
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
            if isinstance(args[0], Number):
                args=(int(args[0]),)
            if self.parent is None:
                return Number(self.number+args[0], parent=self)
            return Number(self.number + self.parent.number)

        def __int__(self):
            return self.number
        
        def __str__(self):
            return str(self.number)

        def __add__(self, other):
            return int(self.number) + int(other)
        
        def __eq__(self, value):
            return int(self) == int(value)
        
        def __lt__(self, other):
            return int(self) < int(other)
        
    return Number(n)

print(add(5)(66)(9) + 90)

'''a = add(5)
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
l = g(e)'''

# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python