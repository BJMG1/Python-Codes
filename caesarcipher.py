a=input("Put Message to encode here: ")
a=a.lower()
num=int(input("Put your number here: "))
def changecharacters(letter,num):
    for i in range(len(letter)):
        letter[i]=characterchange(letter[i],num)
    word=""
    for i in range(len(letter)):
        word=word+letter[i]

    return word

def characterchange(letter,num):
    a=(ord(letter)+num)
    if a>ord("z"):
            while a>ord("z"):
                    b=a-97
                    b=b%26
                    a=97+b

    return chr(a)
tempword=[]
words=[]
for i in range(len(a)):
    if a[i]==" ":
        words.append(changecharacters(tempword,num))
        tempword=[]
    elif (i+1)==len(a):
        tempword.append(a[i])
        words.append(changecharacters(tempword,num))
        tempword=[]
    else:        
        tempword.append(a[i])
print(*words, sep=" ")

                
            