#!/usr/bin/env python3

def hextodecimal(num):
    hex=[]
    for i in range(len(num)):
        hex.append(num[i])
    numbers = []
    while not len(hex)==0:
        if ord(hex[0])>=65:
            hex[0]=hex[0].lower()
            numbers.append(int(ord(hex[0])-87) * (16 ** (len(hex)-1)))
        else:
            numbers.append(int(hex[0]) * (16 ** (len(hex)-1)))
            
        hex.pop(0)
    return sum(numbers)

def decimaltohex(x):
    num = 1
    parts = []
    if not x==0:
        while not x==0:
            if x==1:
                parts.append(x)
                x=0
                num = 1
            elif num==x:
                parts.append(x // num)
                x=0
                num=1
            elif num>=x:
                parts.append(x // (num // 16))
                x=x % (num // 16)
                num = 1
            else:
                num = num * 16
        hexd=""
        for i in range(len(parts)):
            if int(parts[i])<10:
                hexd=hexd+str(parts[i])
            else:
                hexd=hexd+str(chr(parts[i]+87))
    else:
        hexd="0"
    return hexd

def decimalhex(c):
    x=(decimaltohex(c))
    while True:
        b=(hextodecimal(x))
        if c==b:
            break
        else:
             x = x + "0"
    return x

def octaldecimalconv(num):
    number = []
    num=str(num)
    for i in range(len(num)):
        number.append(num[i])
    decimal = 0
    while not len(number)==0:
        decimal += int(number[0]) * 8**(len(number)-1)
        number.pop(0)
    return decimal

def decimaloctalconv(number):
    num = 1
    parts = []
    output = ""
    while not number==0:
        if num>number:
            
            parts.append(number // (num // 8))
            number=number % (num // 8)
            num = 1
        else:
            num = num * 8
    while not len(parts)==0:
        output=output + str(parts[0])
        parts.pop(0)
    if output ==  "":
        output=0
    return int(output)

def decimaltooctalconv(c):
    x=(decimaloctalconv(c))
    while True:
        b=(octaldecimalconv(x))
        if c==b:
            break
        else:
            x = x * 10
    return x

def binarydecimalconv(num):
    number=0
    nums=[]
    for i in range(len(num)):
        nums.append(int(num[i]))

    while len(nums)!=0:
        number+=2**(len(nums)-1)*(nums[0])
        nums.pop(0)
        
    return number

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

def decimalbinaryconv(number):
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
    if binary=="":
        binary="0"
    return binary[::-1]



while True:
    choice=input("Do you want to input a binary number: t/f ")
    if choice=="f":
        choice=input("Do you want to input a decimal number: t/f ")
        if choice=="f":
            choice=input("Do you want to input a octal number: t/f ")
            if choice=="f":
                choice=input("Do you want to input a hex number: t/f ")
                if choice=="t":
                    num = (input("Input Hex to convert: "))
                    x=hextodecimal(num)
                    print("Decimal:",x)
                    print("Binary:",decimalbinaryconv(x))
                    print("Octal:",decimaltooctalconv(x))
                elif choice=="f":
                    break
            elif choice=="t":
                num = (input("Input Octal to convert: "))
                x=octaldecimalconv(num)
                print("Decimal:",x)
                print("Binary:",decimalbinaryconv(x))
                print("Hex:",decimalhex(x))
        elif choice=="t":
            number = int(input("Input Number to convert: "))
            print("Binary:",decimalbinaryconv(number))
            print("Octal:",decimaltooctalconv(number))
            print("Hex:",decimalhex(number))
    elif choice=="t":
        num = (input("Input Binary to convert: "))
        x=binarydecimalconv(num)
        print("Decimal:",x)
        print("Octal:",decimaltooctalconv(x))
        print("Hex:",decimalhex(x))
