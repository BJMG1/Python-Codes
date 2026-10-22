


from turtle import*
from random import*

e = ["red","orange","yellow","blue","purple","gold","cyan","skyblue","DeepPink","LightSeaGreen","orchid","turquoise","red4","salmon","pink"]
x = [-200,-150,-100,-50,0,50,100,150]
y = [0,50,100,150,200,250,300,350]
j = [-225,-200,-175,-150,-125,-100,-75,-50]
pk = []
q = []
lisst=[]
c=[]
d=[]
runs=0
for i in y:
    runs+=1
    for bob in x:
        c=[bob,i]
        d.append(c)
        c=[]
    if runs%2==0 and not runs==0:
        if len(x)>2:
            x.remove(x[0])
            x.remove(x[-1])
    
print(d)

print("How many baubles do you want?")
a=int(input())
if a>len(d):
    a=len(d)
print("How much tinsel do you want?")
b=int(input())
if b>6:
    b=6

speed(0)
pensize(9)
hideturtle()


def tree():
    pensize(9)
    s = 100
    penup()
    goto(0,0)
    left(270)
    forward(50)
    right(90)
    begin_fill()
    pendown()
    for loop in range(3):
        pencolor("brown")
        fillcolor("brown")
        forward(50)
        right(90)

    forward(50)
    end_fill()
    right(180)
    forward(50)
    left(90)
    forward(25)
    for loop in range(10):
        pencolor("green")
        fillcolor("green")
        begin_fill()
        forward(2*s)
        right(135)
        forward(s)
        right(45)
        forward(2.6*s)
        right(45)
        forward(s)
        right(135)
        forward(2*s)
        end_fill()
        right(90)
        forward(0.707*s)
        left(90)
        s += -10
    pencolor("yellow")
    fillcolor("yellow")
    right(90)
    forward(10)
    right(90)
    forward(30)
    right(180)
    pensize(17)
    begin_fill()
    for loop in range(5):
        forward(60)
        left(144)
    end_fill()

def tinsel():
    for loop in range(b):
        penup()
        pq=(y[randint(0,5)])
        pa=pq*0.02
        print(pa)
        pb=(j[int(pa)])
        while pb in pk:
            pq=(y[randint(0,5)])
            pa=pq*0.02
            print(pa)
            pb=(j[int(pa)])
            
        if not pb in pk:
            goto(pb,pq)
            pendown()
            pencolor(e[randint(0,14)])
            pensize(15)
            setheading(180)
            for loop in range(15):
                speed(0)
                left(1)
                forward(pb*0.1)
            pk.append(pb)

            
            
            
def bauble():
    pensize(0)
    pencolor("black")
    for loop in range(a):        
        z=d[randint(0,len(d)-1)]
        d.remove(z)
        penup()
        goto(z)
        pendown()
        fillcolor(e[randint(0,14)])
        begin_fill()
        for loop in range(45):
            speed(0)
            right(8)
            forward(2)
        end_fill()



tree()
tinsel()
bauble()

exitonclick()



