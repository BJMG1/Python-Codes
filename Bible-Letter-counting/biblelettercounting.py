import csv
with open("kjvbible.txt") as file:
    p=file.read()
j=[]
for i in range(32,126):
    j.append(chr(i))
d=dict.fromkeys(j,0)
x=p.split()
for i in x:
    for h in i:
        b=d.get(h)
        d[h]=b+1
l=list(d.keys())
f=list(d.values())
j=open("mycsv1.csv","w" , newline="")
y=csv.writer(j)
y.writerow(["Character","Occurencies"])
for i in range(len(l)):
    y.writerow([l[i],f[i]])
j.close()