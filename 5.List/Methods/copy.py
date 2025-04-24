'''copy  method is used when you dont want to give same meomary location while copying a value it will make shallow copy of value'''

list1 = [1,2,3,4]

list2 = list1.copy()

list2.insert(2,'hello')

print(list1)
print(list2)