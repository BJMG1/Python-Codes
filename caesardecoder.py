a=input("Put your message to decyrpt here: ")
a=a.lower()
def changecharacters(letter,num):
    for i in range(len(letter)):
        letter[i]=characterchange(letter[i],num)
    word=""
    for i in range(len(letter)):
        word=word+letter[i]

    return word

def characterchange(letter,num):
    a=(ord(letter)-num)
    if a<ord("a"):
            while a<ord("a"):
                    b=122-a
                    b=b%26
                    a=122-b

    return chr(a)

for num in range(26):
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

                
            
