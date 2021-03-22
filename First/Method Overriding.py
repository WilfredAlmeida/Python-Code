#  In python method overriding is done th same way like the others

class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

a = A()
a.show()

b = B()
b.show()