class Employee():
    def __init__(self,aname,arole,asalary):
        self.name = aname
        self.role = arole
        self.salary = asalary

    def printdetails(self):
       return f"name is {self.name},role is {self.role} and salary is {self.salary}"

    @classmethod
    def from_dash(cls,string):
        # params = string.split("-")           # split string from karans
        # print(params)                        #print a karans value in the list
        # return cls(params[0],params[1],params[2])

        return cls(*string.split("-"))        #commented part in one line

Ram=Employee("Ram","Software Enginner",55000)
Shyam = Employee("Shyam","Data Analytics",60000)
karan = Employee.from_dash("karan-student-1000")

print(karan.salary)
