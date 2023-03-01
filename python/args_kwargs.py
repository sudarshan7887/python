def funargs(normal,*args,**kwargs):
    print(normal)
    for items in args:
        print(items)
        print("\nNow I would Like to introduce some of heroes")
        for key,value in kwargs.items():
            print(f"{key} is a {value}")

sp = ["ram","Shayam","vinod","ketan","rushi","Ramesh"]
normal = "I am a normal Argument and the students are:"
kw = {"rohan":"Monitor","Abhi":"programmer","vinayak":"fitness instructor"}
funargs(normal,*sp,**kw)