import csv
src = open("Files/kjvbible.txt")
letters = list(src.read())
word=""
uqword = []
for i in range(len(letters)):
    if  not 65 <= ord(letters[i]) <= 90 or not 97 <= ord(letters[i]) <= 122:
        if not word in uqword:
            uqword.append(word)
        word=""
    else:
        word = word + str(letters[i])

