
d1 = {}
print(type(d1))

d2 = {"ram":"maggi","shyam":"roti","abhi":"chinees","shubham":{"b":"maggi","l":"burgar","d":"roti"}}
print(d2)

d2["vinayak"] = "chiken"     # add value in dictionary
print(d2)

del d2["abhi"]            # delete a specific value from dictionary
print(d2)

print(d2["shubham"])     # print specific value

d3 = d2.copy()          # copy a dictionary
print(d3)

d2.update({"Geeta":"chinees"})  # update value or add value
print(d2)

print(d2.keys())              # print only keys

print(d2.items())              # print items in dictionary



