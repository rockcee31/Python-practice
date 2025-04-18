# pass statement is used as place holder means if you want to write logi  of loop later than you can simply write pass instead of leaving it empty
# continue and pass has a difference that continue skip that condition
for num in range(1,10):
    if num==5:
        pass
    print(num)

for num in range(1,10):
    if(num == 5):
        continue
    print(num)

    