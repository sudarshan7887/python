import time
initial = time.time()

k = 0
while(k<45):
    print("I am Sudarshan")
    k+=1
    time.sleep(2)
print("while loop run in",time.time() -initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("I am Sudarshan")
    time.sleep(2)
print("for loop run in",time.time() -initial2,"seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)