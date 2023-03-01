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

Ram=Employee("Ram","Software Enginner",55000)
Shyam = Employee("Shyam","Data Analytics",60000)

shubham = player("Shubham",["Cricket"])
karan = Coolprogrammer('karan',56666,"Coolprogrammer")

det = karan.printdetails()
karan.printlanguage()
print(det)

print(Coolprogrammer.language)

