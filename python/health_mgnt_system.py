# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("sudarshan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("sudarshan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("pansare-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("pansare-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("abhi-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("abhi-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(sudarshan),2(pansare),3(abhi)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for sudarshan 2 pansare 3 for abhi "))
    take(b)
else:
    b = int(input("Press 1 for sudarshan 2 for pansare 3 for abhi "))
    retrieve(b)

