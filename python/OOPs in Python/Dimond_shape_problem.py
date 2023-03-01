class A:
    def method(self):
        print("This is a method A")

class B(A):
    def method(self):
        print("This is a method B")

class C(A):
    def method(self):
        print("This is a method C")

class D(C,B):
    def method(self):
        print("This is a method of D")

a = A()
b = B()
c = C()
d = D()
d.method()