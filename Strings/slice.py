'''Slicing means extracting element from string'''

a="hair"

b=a[1:5] # slicing here first column is inclusive and second is exclusive

print(b)

'''string slicing structure - slice[start:end:gap]'''

a="rohit"
print(a[0:6:2])
# by default gap 1 hota hai means print every first element

# and if you do something like that
print(a[::]) #it will print whole string
print(a[::-1])