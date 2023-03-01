# numbers = ["3","34","64"]
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# numbers[2] = numbers[2] + 1
# print(numbers[2])

# def sq(a):
#     return a*a
#
# num = [2,6,8,9,5,20]
# square = list(map(sq,num))
# print(square)

# ................map ..................

num = [2,6,8,9,5,20]
multi = list(map(lambda x:x*x,num))    # above def function logic in lambda exp
print(multi)

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

print()

# ...................filter......................
print("in filter function")
list1 =[1,2,3,4,5,6,7,8,9]

def greater(num1):
    return num1>5

gr_than_5 = list(filter(greater,list1))
print(gr_than_5)

#.............reduce...............
from functools import reduce

print("in reduce function")
lis = [1,2,3,4,5]

# num2 = 0
# for i in lis:
#     num2 = num2+i
# print(num2)

# Above logic in one line
num2 = reduce(lambda x,y:x+y,lis)
print(num2)