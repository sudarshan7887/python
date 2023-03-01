class student():
    pass

sudarshan = student()         # objects
Ram = student()

sudarshan.name = "Sudarshan Pansare"                   #instance
sudarshan.std = "fymcs"
sudarshan.subjects = ["AOS","mobile Technology","SPM"]

Ram.name = "Ram"
Ram.std ="12th"
Ram.subjects = ["physics","chemistry","math","English"]

print("Sudarshan values")
print(sudarshan.name )
print(sudarshan.std)
print(sudarshan.subjects)
print("")

print("Ram values")
print(Ram.name)
print(Ram.std)
print(Ram.subjects)