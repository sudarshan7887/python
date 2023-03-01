
# def funcret(num):
#     if num==0:
#         return print
#     if num ==1:
#         return sum
#
# a = funcret(1)
# print(a)

# def executer(func):       # function inside a function
#     func("this")
# executer(print)

# ..........decorators..........
def dec1(func1):
    def nowexec():
        print("Execute now")
        func1()
        print("Executed")
    return nowexec

@dec1      # decorator
def sudarshan():
    print("This is sudarshan")
# sudarshan = dec1(sudarshan)   # if write @dec1 then it not write otherwise write
sudarshan()


