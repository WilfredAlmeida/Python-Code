a = 2


class MyException(Exception):
    print("User Defined Exception thrown...")


try:
    print("Resource Open \n")
    b = int(input("Enter a number\n"))
    c = a / b
    print("2 / Input = ", c)
    print("Bye:)")
    raise MyException()

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except MyException:
    print("Something went wrong...")

finally:
    print("\n Resource Closed")
