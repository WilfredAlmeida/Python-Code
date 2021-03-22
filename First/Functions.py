# There is no concept of pass by reference in python.
def f1():
    print("function f1")


def person(name, age=90):
    # Default value to be assigned if value is not passed while function call.
    # Known as Keyworded arguements(kwargs)
    print("Name= ", name)
    print("Age - 1 = ", age - 1)


# person('a', 12)  # Calls the function with passed values

# person(age=12,name='a')  # Assigns values to specified parameters irrespective of
# position of argument in function definition

def sum(*b):  # * indicates that the number of arguments is not fixed and there can be
    # 'n' number of arguments. 'b' is a tuple. Known as variable length arguments(varargs)
    c = 0
    for i in b:
        c = c + i
    print(c)


#sum(1,2,3,4)

def person1(**b):  # Used for allowing keyword=value pairs.
    # Known as keyworded variable length arguments. 'b' is a dictionary
    for i, j in b.items():
        print(i, "=", j)


person1(name='a', age=12.5, mobile=121212, city='mumbai')
