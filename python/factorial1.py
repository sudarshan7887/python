
def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac

    pass
number = int(input("enter your number"))
print(factorial(number))
