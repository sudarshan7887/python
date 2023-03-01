import  os
# print(os.getcwd())                          # current Directory
# os.chdir("c://")                            #change current directory to c
# print(os.getcwd())
# print(type(os.listdir("c://")))             #type of listdir

# os.mkdir("sudarshan")                      # create folder sudarshan
# os.rmdir("sudarshan")                      # delete folder sudarshan
# os.makedirs("sudarshan/pansare")           # create many folder
# os.rename("osfile.txt","osfilemodule")     # rename txt file
# print(os.environ.get('path'))              #enviornment variable
# print(os.path.join("c:/","/harry.txt"))    #join to path
print(os.path.exists("c:/"))                #print true if path is exist otherwise false
