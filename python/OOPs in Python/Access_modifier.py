class Employee():
    no_of_leaves = 8        #public access modifier
    _protec = 10          #protected access modifier
    __private = 20        #private access modifier
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

class player:
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"name is{self.name},game is{self.game}"

class Coolprogrammer(Employee,player):
    language = "python"
    def printlanguage(self):
        print(self.language)

emp = Employee("sudarshan",55555,"programmer")
print(emp._protec)            # called protected access modifier
print(emp._Employee__private)   #called private Access modifier

