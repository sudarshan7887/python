# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)

# List comprehesion
ls = [i for i in range(100) if i%3==0]
print(ls)

# dictionary comprehesion
# dict1 = {i:f"item {i}" for i in range(100) if i%3==0}

dict1 = {i:f"Item {i}" for i in range(5)}

dict2 = {value:key for key,value in dict1.items()}      # Reverse dictionary
print(dict1,"\n",dict2)

# set Comprehension
dresses = {dress for dress in ["dress1","dress2","dress1","dress2"]}
print(dresses)

# generator comprehension
evens = (i for i in range(100) if i%2==0)
# print(evens.__next__())
# print(evens.__next__())

for i in evens:
    print(i)

