
# list are mutable can change

name = ["Ram","Shyam","Sita","Gita","Krishna",57]
print(name)
print(type(name))          # print type

numbers = [34,23,56,65,12,33]
print(numbers[2])    # print 2nd index number

"""
        numbers.sort()
        print(numbers)          #sort given nos in asending order

        numbers.reverse()
        print(numbers)          #sort given nos in desending order
"""
#       print(numbers[::2])            # list slicing same as string slicing

print(max(numbers))                 #print max number
print(min(numbers))                 #print min number
print(len(numbers))                 #print  length of list


numbers.append(45)                     #Add 45 in last index
print(numbers)

numbers.insert(3 , 66)
print(numbers)                      # add 3rd index as 66

numbers.pop()                         # pop last element
print(numbers)

"""
     numbers.clear()
     print(numbers)
"""
numbers.count()
print(numbers)

numbers.index(3)
print(numbers)

numbers.reverse()
print(numbers)


print(numbers)



