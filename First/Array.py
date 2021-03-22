from array import array as default_array
from numpy import array as arr
from numpy import *  # numpy is additional package. refer txtbk for more info.

# In python 2D array can not be created directly and hence numpy is required

a = default_array('u', ['l', 'i', "u"])  # creates 1D array
print("Default Array:\n", a)

# b = arr([1, 2, 3], int)
b = arr([['1', '2', '3'], ['4', '5', '6']], str)  # type of array(int in this case is optional, it is written
# after values
# for integer use 'int', for string use 'str','float' for float
print("2D Array:\n", b)

# linspace(start,end,number_of_parts)
# ------------------------------
'''used to create array from start parameter to end parameter with number of values required as the third parameter.
IMP: end value is INCLUDED in the returned array.
Default value of parts is 50
default datatype of returned values is float'''
b = linspace(1, 10, 10)
print("Linspace: \n", b)
# ------------------------------

# arange(start,end,step)
# ------------------------------
'''returns array.
end is EXCLUDED.
step is number of times to increment before getting next value.
'''
c = arange(1, 11, 2)
print("arange: \n", c)
# ------------------------------

# logspace(start,stop,number_of_parts)
'''start and stop are in power of 10. eg: 10^start....10^end
IMP: end is included in result'''

d = logspace(1, 10, 7)
print("logspace:\n", d)
# -----------------------------------

# zeros(number_of_values_required_in_array, datatype) and ones(number_of_values_required_in_array, datatype)
'''create array with zeros and ones.
datatype is optional.
default is float'''
print("Zeros:\n", zeros(5))
print("Ones:\n", ones(5, int))
