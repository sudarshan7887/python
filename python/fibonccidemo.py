# fibonacci series in recursive method
# 0 1 1 2 3 5 8 13 .....
number = int(input("Enter your number:\n"))
def fibonacci(n):
    if n ==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(number))