import random
def main():
    print("Type the word you want to find: ",end="")
    targetWord = (input()).upper()

    def monkeys_typing(currentWord):
        guess=""
        for i in range(len(currentWord)):
                guessNumber = random.randint(65, 90)
                guess=guess+chr(guessNumber)
        count = 1
        while guess != currentWord:
            for i in range(len(currentWord)):
                guessNumber = random.randint(65, 90)
                guess=guess+chr(guessNumber)
            
            
            
            if guess==currentWord:
                break
            guess=""
            count +=1
        return count
    word=""
    lastspace=0
    words=[]
    for i in range(len(targetWord)):
        if targetWord[i]==" " or i+1==len(targetWord):
            for x in range(lastspace,i+1):
                if not targetWord[x]==" ":
                    word=word+targetWord[x]
            lastspace=i
            words.append(word)
            
            word=""
            
    guessse=0
    #print(words)
    for d in words:
        print(d)
        guessse+=monkeys_typing(d)
        print(guessse)

while True:
    main()