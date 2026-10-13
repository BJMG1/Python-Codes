


def hextodecimal(num):
    hex=[]
    for i in range(len(num)):
        hex.append(num[i])
    numbers = []
    while not len(hex)==0:
        if ord(hex[0])>=97:
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
            x=x+"0"
    return x


print(decimalhex(int(input())))
