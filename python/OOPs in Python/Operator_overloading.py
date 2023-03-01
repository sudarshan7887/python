class Employee:
    no_of_leaves = 15

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name},salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):         #dunder methods used to operator overloading
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee '{self.name}',{self.salary},'{self.role}'"

    def __str__(self):
        return f"name is {self.name},salary is {self.salary} and role is {self.role}"

emp1 = Employee("Sudarshan",50000,"programmer")
# emp2 = Employee("rahul",25000,"cleaner")
# print(emp1 / emp2)                #for dunder method

print(str(emp1))
print(repr(emp1))