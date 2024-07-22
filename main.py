import turtle
import random

#screen settings
screen= turtle.Screen()
screen.bgcolor("silver")
screen.title("Catch The Turtle")
FONT= ("Arial", 30 ,"normal")
grid_size=10
score=0
gameover=False

#turtlelist
turtlelist=[]

#countdownturtle
countdownturtle=turtle.Turtle()

#make turtle properties
x_cord=[-20,-10,0,10,20]
y_cord=[20,10,0,-10]

#SOCRETURTLE
scoreturtle=turtle.Turtle()


def setup_scroreturtle():
    scoreturtle.hideturtle()
    scoreturtle.color("white")
    scoreturtle.penup()

    topheight=screen.window_height()/2
    y = topheight*0.9

    scoreturtle.setpos(0,y)
    scoreturtle.write(arg= "Score : 0", move=False, align="center", font=FONT)

def maketurtle(x,y):
    t= turtle.Turtle()

    def handleclick(x,y):
        global score
        score+=1
        scoreturtle.clear()
        scoreturtle.write(arg=f"Score : {score}", move=False, align="center", font=FONT)
        print(x,y)


    t.onclick(handleclick)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("red")
    t.goto(x*grid_size,y*grid_size)
    turtlelist.append(t)

def setup_turtles():

    for x in x_cord:
         for y in y_cord:
            maketurtle(x,y)

def hideturtle():
    for t in turtlelist:
        t.hideturtle()

#recursive function
def showturtlerandom():
    if not gameover:
        hideturtle()
        random.choice(turtlelist).showturtle()
        screen.ontimer(showturtlerandom,200)

def countdown(time):
    global gameover
    countdownturtle.hideturtle()
    countdownturtle.color("black")
    countdownturtle.penup()

    topheight = screen.window_height() / 2
    y = topheight * 0.9

    countdownturtle.setpos(0, y-30)
    countdownturtle.clear()

    if time>0:
        countdownturtle.clear()
        countdownturtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time-1),1000)
    else:
        gameover=True
        countdownturtle.clear()
        hideturtle()
        countdownturtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def startgame():
    turtle.tracer(0)

    setup_scroreturtle()
    setup_turtles()
    hideturtle()
    showturtlerandom()
    countdown(10)
    turtle.tracer(1)


startgame()
turtle.mainloop()
