class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email =f"{self.fname}.{self.lname}@email.com"

    def Explain(self):
         return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

skillf = Employee("skill","f")
print(skillf.email)
print(type(skillf))
print(id(skillf))
print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))