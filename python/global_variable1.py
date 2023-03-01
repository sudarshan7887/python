"""
a = 10  #global
def function1(n):
     l = 5  # local
     m = 7  # local->not accessible outside the function1
     print(l,m)   #local call
     global a  # change the global variable value
     a = a + 10
     print(n,"This is Printed")
function1("This is me")
print(a)   # gobal call
"""
def sudarshan():
    x = 20
    def pansare(): # nested function ->function inside a function
        global x
        x = 88
    print("before calling pansare",x)
    pansare()
    print("after calling pansare",x)
sudarshan()
