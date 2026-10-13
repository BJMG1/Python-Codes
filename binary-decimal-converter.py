#!/usr/bin/env python3

def largestnum(x,numbers):
    num=1
    while not num>=x:
            num=num*2
    if num==x:
        x=0
        numbers.append(num)
    elif num>x:
        x=x-(num//2)
        numbers.append(num//2)

    return x

def decimalconv():
    number = int(input("Input Number to convert:"))
    numbers=[]
    while not number==0:
        number=largestnum(number,numbers)
    num=1
    binary=""
    while not len(numbers)==0:
        if num==numbers[-1]:
            binary=binary+"1"
            numbers.pop(-1)
        else:
            binary=binary+"0"
        num=num*2
    print(binary[::-1])


def binaryconv():
    num = (input("Input Binary to convert:"))
    number=0
    nums=[]
    for i in range(len(num)):
        nums.append(int(num[i]))

    while len(nums)!=0:
        number+=2**(len(nums)-1)*(nums[0])
        nums.pop(0)
        
    print(number)

choice=input("Do you want to convert binary to decimal: t/f ")
if choice=="f":
    choice=input("Do you want to convert decimal to binary: t/f ")
    if choice=="f":
        print("N")
    elif choice=="t":
        decimalconv()
elif choice=="t":
    binaryconv()
