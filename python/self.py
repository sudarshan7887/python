class Employee():
    no_of_leaves = 8
    def printdetails(self):
       return f"name is {self.name},role is {self.role} and salary is {self.salary}"

Ram=Employee()
shyam = Employee()

Ram.name = "Ram"
Ram.role = "Software Enginner"
Ram.salary = 56000

shyam.name = "shyam"
shyam.role = "Data Analytics"
shyam.salary = 70000

print(shyam.printdetails())
