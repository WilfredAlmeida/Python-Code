#  Python does not support method overloading in c++, java style.
#  we need to use a little trick here.
#  We will initialize the number of parameters in a method to none and will use them
#  if they are not none

class A:
    def sum(self, a=None, b=None, c=None):
        # this can only take upto 3 argument while calling
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return a


a = A()

print(a.sum(1))
