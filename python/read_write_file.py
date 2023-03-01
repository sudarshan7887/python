# handle read and write both file
f = open("sudarshan3.txt","r+")    # r+ means read and write file
print(f.read())
f.write("thank you")
f.close()
