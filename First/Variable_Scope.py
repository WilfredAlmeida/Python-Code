#  There are 4 types of variable scopes in python:
#  1. Local
#  2. Global
#  3. Enclosed
#  4. Built-In
#
#
# Local: Inside Function/method. Accessible only to inside function body.
#
# Global: Available to whole module.
#
# Enclosed: Inside inner function of a function. Accessible to defining function body
# and parent function body, not outside parent function body.
#
# Built-In: In built variables defined in python.
#
# If in a code there exists a variable of same name and all 4 scopes then python will
# follow the LEGB rule. Local->Enclosed->Global->Built-In
#

g = 3
print("Global Variable= ", g)


def f1():
    l = 5
    print("Local Variable= ", l)
    print("Global Variable inside local variable's function= ", g)

    def f2():
        e = 9
        print("Enclosed Variable= ", e)
        print("Local Variable inside enclosed variable's function= ", l)
        print("Global Variable inside enclosed variable's function= ", g)

    f2()

    # To modify global variable inside function, use global keyword as follows:
    globals()[g] = 25
    print("Modified Global Variable inside local variable's function= ", globals()[g])
    # or declare variable global using global BEFORE ACCESSING IT ANYWHERE using 'global' keyword as follows:
    # global g
    # g=7 # Note that only declaration can happen using global keyword and not any value assigning.
    # global f = 88 # This will produce error


f1()

print("Global variable at program end= ", globals()[g])
# Only writing 'g' here prints 3, I don't know why :)
