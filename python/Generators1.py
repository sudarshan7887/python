"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
"""
def gen(n):                 #generator
    for i in range(n):
        yield i

g = gen(3)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)

h = "Sudarshan"        # String is iterable
for c in h:
    print(c)
# print(ier.__next__())
# ier = iter(h)
# print(ier.__next__())
# print(ier.__next__())
