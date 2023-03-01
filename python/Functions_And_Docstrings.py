a = 5
b = 10
c = sum((a,b))   # Built in function
print(c)
print("")

# user Defined functions

def function1():
    print("You are in the functions")
function1()
print("")

def function2(p,q):
    """This is a function which will calculate average of two numbers"""
    average = (p+q)/2
    print(average)
function2(6,2)
print(function2.__doc__)    # This is docstring written in function


