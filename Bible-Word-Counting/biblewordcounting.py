import json #imports library for json files
k=[]#creating 3 empty lists
o=[]
chapters=[]
with open('verses-1769.json') as file: #opens the json we are extracting the word counts from
    data=json.load(file) #sets data to the contents of the file
    for i in data.keys(): #i is the list of the key names of each chapter
        chapters.append(i) #i is then added to our previous empty list which will end up have all chapter names
def words(book):#defining a function called words require an input variable
    c="" #c is an empty str
    for i in data[book]: #i is equal to the loop no. character in the book i.e if the book is "the and" on the first loop i is equal to t
        if i.isupper()==True:#checks if character is uppercase returns boolen
            i=i.lower()#if it was makes it lowercase
        if i in(" ,.[{()}]!&?;:"):#checks to see if i is any of those characters runs this loop if it is
            for b in range(len(o)):#b = the current loop no. starting @ 0
                c=c+o[b] #combines the current str with the character @ b postition in the list
            if not c in k:#if the str of c is not already in k 
                k.append(c) #adds c to the list k
            c=""#clears the string
            o.clear()#clears the character list
        else:
            o.append(i) #appends the current character to the list of O
def counting(book):#defining a new function takes an input variable
    c=""#creates an empty string
    for i in data[book]:#works the same as the previous function until
        if i.isupper()==True:
            i=i.lower()
        if i in(" ,.[{()}]!&?;:"):
            for b in range(len(o)):
                c=c+o[b]
            x=d.get(c)#here, where it finds the string c as a key in the dictionary and gets its current value
            if x==None:#sometimes the value of the key was None so I had this to make sure if it did it was changed to 0
                x=0
            x+=1 #adds 1 to the current value of the key
            d[c]=x #sets it as the new value
            c=""#clears the string 
            o.clear()#clears the list
        else:
            o.append(i) #appends the current character to the list of O
for i in range(len(chapters)):#runs the amount of times as there is chapters
    words(chapters[i])#runs the function for each chapter
k.sort()#sorts the words collected into alphabetical order
d= dict.fromkeys(k,0)#creates a dictionary from the list of k as the keys and sets the values as 0
for i in range(len(chapters)):#runs the amount of times as there is chapters
    counting(chapters[i])#runs the function for each chapter 
l=list(d.keys()) #creates a list of all the keys 
f=list(d.values()) #creates a list of all the values
import csv #importing library for writing/reading to csv files this is where i store the collected data
j = open("wordcount.csv","w" , newline="") #opening
y=csv.writer(j) #sets y as writing to the file
y.writerow(["Word","Occurencies"]) #writes the headers
for i in range(len(l)):#writes the keys on the left column and the values on the right creating the csv
    y.writerow([l[i],f[i]])
j.close()#closing
