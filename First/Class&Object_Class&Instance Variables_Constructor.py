# __init__(self) method is the constructor. suppose, myclass is a class and while object creation you write x =
# myclass(4,5), these 4,5 will be received by the __init__(self) method

# static variable also known as class variable,IMP: changing static variable from one object will affect all other
# objects instance variable is the object variable i.e. it is created for every object

#  variables defined OUTSIDE the __init__(self) method are static variables

#  variables defined INSIDE the __init__(self) method are instance variables

# IMP: self points the caller object. self points to the object which is trying to do something. for better
# definition refer Telusko video, internet or txtbk
class car:
    static_variable = 9

    def __init__(self, a):
        self.instance_variable = a  # self is necessary or else the variable wont be accessible outside the init method

    def print_method(self):
        print('Instance Variable= ',
              self.instance_variable)  # instance variables are accessible only inside methods. With my current
        # knowledge it is not accessible but it might be wrong. I don't know :):}

    print('Static variable= ', static_variable)


c1 = car(3)
c1.print_method()
