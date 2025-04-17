'''Day1'''

# sequence type is datatype which are  being indexed and ordered and and iterable in order
# python automatically understand type of data  we dont need to specify it like other language we just have to pass based on sytax


# tuple
# stores more than one element of any data type 
# immutable
a=("hello","dirty","fellow")

print(a)
print(type(a))


# list
# has more than one element which can be of any type and are stored inside []
# mutable
b=["pappaya","kela",10]

print(b)
print(type(b))


# string
# sequence of character
# ordered support indexing and slicing
# immutable
c= "Rohit"

print(c)
print(type(c))
print(c[0:6]) #slicing(extrating element based on index)


# range 
# represents sequence of numbers 
# often used in loops
# immutable
# oredered: support indexing
r = range(0,5)
print(r)
print(list(r))
print(r[2])

