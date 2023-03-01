def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac
number = int(input("enter your number"))
print("factorial in iterative method is:",factorial_iterative(number))

def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print("factorial in recursive method is:",factorial_recursive(number))