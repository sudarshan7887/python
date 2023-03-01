class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email =f"{self.fname}.{self.lname}@email.com"

    def Explain(self):
         return f"This Employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname ==None and self.lname ==None :
            return "Email is not set plese set email using setter method"
        return f"{self.fname}.{self.lname}@email.com"

    @email.setter           # set the attribute
    def email(self,string):
        print("Setting now....")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter                       #delete setters method
    def email(self):
        self.fname = None
        self.lname = None

emp1 = Employee("Sudarshan","pansare")
emp2 = Employee("Abhi","Wagh")

print(emp1.email)

emp1.fname = "sagar"
print(emp1.email)

emp1.email = "this.that@gmail.com"
print(emp1.email)
print(emp1.fname)
print(emp1.lname)

del emp1.email       #delete setters method
print(emp1.email)
