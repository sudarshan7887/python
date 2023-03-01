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

    @staticmethod
    def printgood(string):
        print("This is good function, " +string)

class programmer(Employee):  #inherit employee class
    def __init__(self,aname,arole,asalary,languages):        #constructor
        self.name = aname
        self.role = arole
        self.salary = asalary
        self.languages= languages

    def printprog(self):
         return f"name is {self.name},role is {self.role} and salary is {self.salary} and languages are{self.languages}"


Ram=Employee("Ram","Software Enginner",55000)
Shyam = Employee("Shyam","Data Analytics",60000)

rohan = programmer("rohan","programmer",59594,["python","java"])
shubham = programmer("Shubham","programmer",45677,["python","cpp"])

print(rohan.printdetails())      # because it inherit property of employee class
print(rohan.printprog())

