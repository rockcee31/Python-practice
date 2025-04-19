# identity operotor checks if both vaiable pointing to same meomary location
a=[1,2,3]
b=a
c=[1,2,3]

print(a is b)
print(b is a)

print(c is a)