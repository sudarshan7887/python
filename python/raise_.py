# a = input("What is your name\n")
# b = input("How much do you earn")
# if int(b) ==0:
#     raise ZeroDivisionError("b is 0 so stopped the Execution")
#
# if a.isnumeric():
#     raise Exception("Numbers are not allowed")
#
# print(f" Hello {a}")

c = input("Enter your name:\n")
try:
    print(a)
except Exception as e:

    if c =="sudarshan":
        raise  ValueError("Sudarshan is blocked is not allowed")
    print("Exception Handled")