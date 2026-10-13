import time
#!/usr/bin/env python3


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




choice=input("Do you want to convert octal to decimal: t/f ")
if choice=="f":
    choice=input("Do you want to convert decimal to octal: t/f ")
    if choice=="f":
        print("N")
    elif choice=="t":
        print(decimaltooctalconv(int(input())))
elif choice=="t":
    num = (input("Input Octal Number here: "))
    octaldecimalconv(num)