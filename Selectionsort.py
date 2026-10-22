numbers=[64,43,2,0,99,-123]
sortednumbers=[]
for i in range(len(numbers)):
    a=numbers[i] 
    for h in range(i,len(numbers)):
        if a>numbers[h]:
            a=numbers[h]
    numbers[numbers.index(a)]=numbers[i]
    numbers[i]=a
print(numbers)


