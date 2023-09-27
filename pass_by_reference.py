a = [1,2,3]
b = a
print("a:",a)
print("b:",b)

b.extend([4,5,6])

print("a:",a)
print("b:",b)

c = a.copy()
c.extend([7,8,9])

print("a:",a)
print("b:",b)
print("c:",c)