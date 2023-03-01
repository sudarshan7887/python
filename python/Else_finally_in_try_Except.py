f1 = open("sudarshan.txt")
try:
    f = open("sudarshan3.txt")

except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
     print("Run this anyway.....")
     f1.close()

print("Important stuff")

