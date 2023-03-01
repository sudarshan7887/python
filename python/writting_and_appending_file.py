# f = open("Sudarshan2.txt","w")       #Write mode
f = open("sudarshan2.txt","a")         #append a file
# f.write("my name is Sudarshan\n")
a=f.write("my name is Sudarshan\n")   # written no of charater from a file
print(a)
f.close()