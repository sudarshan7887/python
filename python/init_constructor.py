class Employee():
    no_of_leaves = 8
    def __init__(self,aname,arole,asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetails(self):
       return f"name is {self.name},role is {self.role} and salary is {self.salary}"

Ram=Employee("sudarshan","Software Enginner",55000)

print(Ram.role)