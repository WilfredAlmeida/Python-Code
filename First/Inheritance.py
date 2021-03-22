#  Python supports Singlelevel, Multilevel, Multiple inheritance
class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


class B(A):  # Single-level Inheritance
    def feature3(self):
        print("Feature 3")


class X:
    def featurex(self):
        print("Feature X")


class C(B, X):  # Multiple Inheritance
    def feature4(self):
        print("Feature 4")


class D(C):  # Multi-level Inheritance
    def feature5(self):
        print("Feature 5")
