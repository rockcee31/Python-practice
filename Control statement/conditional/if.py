a = int(input('please enter yout age :'))
valid_age = 18

if a>=valid_age:
    print("you are valid to vote")
elif a<valid_age:
    print("age is not valid to vote")
else:
    print('invalid age')