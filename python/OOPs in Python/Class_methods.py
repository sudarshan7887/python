class Employee():
    no_of_leaves = 8
    def __init__(self,aname,arole,asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetails(self):
       return f"name is {self.name},role is {self.role} and salary is {self.salary}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

Ram=Employee("Ram","Software Enginner",55000)
Shyam = Employee("Shyam","Data Analytics",60000)

Ram.change_leaves(34)
print(Ram.no_of_leaves)