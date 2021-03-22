#  When an operator is used a method of its name is called and we overload that method
#  and perform operator overloading
"""
+ = __add__(self)
- = __sub__(self)
* = __mul__(self)
/ = __truediv__(self)
% = __mod__(self)
^ = __xor__(self)
& = __and__(self)

"""

#  Overloading '/' to perform multiplication

a = 4
b = 2


def __truediv__(self, m, n):
    return m * n


print(a / b)
