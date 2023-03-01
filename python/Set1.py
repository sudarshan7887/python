# set print unic value only
s = set()
print(type(s))

s.add(1)
s.add(3)
s.add(2)
print(s)

s1 = s.intersection({1,2,3})
print(s,s1)

s2 = s.union({1,3,4})
print(s,s2)
