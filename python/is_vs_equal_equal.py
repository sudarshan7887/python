# == ->value equality-Two objects have the same value
# is -> reference equality -Two reference refer to the same object

a = [3,5,6]
b = [4,8,9]

a = b
print(a == b)

print(a is b)

c = a[:]
print(c is a)
print(c==a)

