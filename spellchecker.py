import json
l=[]
c=[]
with open ("words.json") as file:
    realwords=json.load(file)
li=[]
lx=[]
j=""
with open("words.txt") as f:
    p=f.read()
    p=p.split()
for i in range(len(p)):
    x=p[i]
    for h in range(len(x)):
        li.append(x[h])
    for q in range(len(li)):
        if li[q].isupper()==True:
            li[q]=li[q].lower()
        if li[q].isalpha()==False:
            lx.append(li[q])
    for g in range(len(lx)):
        li.remove(lx[g])
    for t in range(len(li)):
        j=j+li[t]
    p[i]=j
    j=""
    li=[]
    lx=[]
for y in p:
    if y in realwords:
        if not y in l:
            l.append(y)
    else:
        if not y in c:
            c.append(y)
print("These words are spelt correctly:",",".join(l),"\n")
print("These words were spelt incorrectly:",",".join(c),"\n")