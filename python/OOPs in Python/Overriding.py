class A:
    classvar1 = "in class A"
    def __init__(self):
        self.var1 = "I am inside a constructor of class A"
        self.classvar1 = "instance variable of class A"
        self.special = "special"
class B(A):
    classvar1 = "in class B"
    def __init__(self):
        self.var1 = "I am inside a constructor of class B"
        self.classvar1 = "instance variable of class B"
        super().__init__()       # called overrided method

a = A()
b = B()
print(b.classvar1)
print(b.special,b.var1,b.classvar1)