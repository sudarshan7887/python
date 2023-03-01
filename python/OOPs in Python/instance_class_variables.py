class Employee():
    no_of_leaves = 10         #class Attribute
    pass

# no_of_leaves cannot change with the help of instance of class
# i.e     rohan.no_of_leaves = 13  is not working

# it only change with the help of main class
# i.e
# Employee.no_of_leaves = 12
# print(Employee.no_of_leaves)

ram = Employee()
shyam = Employee()

ram.name = "Ram"
ram.salary = 45000
ram.section = "Inventory"

shyam.name = "Shyam"
shyam.salary = 50000
shyam.section = "Student"

print(ram.no_of_leaves)
