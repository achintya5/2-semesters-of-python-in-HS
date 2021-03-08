import turtle
import random
win=turtle.Screen()
win.title("Shooting Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


#scoring
score=0
#Gun
gun=turtle.Turtle()
gun.speed(0)
gun.shape("square")
gun.color("white")
gun.shapesize(stretch_wid=1, stretch_len=5)
gun.penup()
gun.goto(-350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(gun.xcor()+50,gun.ycor())
ball.dx=5
ball.dy=0

#obstacle
obs=turtle.Turtle()
obs.speed(0)
obs.shape("square")
obs.color("white")
obs.penup()
obs.goto(350,0)

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0", align="center", font=("Courier",24, "normal"))

#instructions
p=turtle.Turtle()
p.speed(0)
p.color("white")
p.penup()
p.hideturtle()
p.goto(0,0)
p.write("Rules\n Press w to move up\n Press s to move down\n Press space to shoot\n Score 10 points to win", align="center", font=("Courier",24, "normal"))

#Functions
def gun_up():
    y=gun.ycor()
    y+=30
    gun.sety(y)
def gun_down():
    y=gun.ycor()
    y-=30
    gun.sety(y)
def ball_return():
    ball.sety(gun.ycor())
    ball.setx(gun.xcor())
#keybord binding
win.listen()
win.onkeypress(gun_up,"w")
win.onkeypress(gun_down,"s")
win.onkeypress(ball_return,"space")

#Main game loop
while True:
    win.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # random obstacle coordinates
    c = list(range(-270, 270, 30))
    r = random.choice(c)
    if win.onkeypress(ball_return,"space"):
        count+=1
    if ball.xcor() == obs.xcor() and ball.ycor() == obs.ycor():
        obs.sety(r)
        obs.sety(r)
        score+=1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    if score==10:
        p.clear()
        pen.clear()
        pen.goto(0,0)
        pen.write("YOU WIN", align="center", font=("Courier", 50, "normal"))


