# imported turtle module
import turtle

wind = turtle.Screen()
wind.title("Pong by Hesham jesse")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# hatba 1 :
hatba1 = turtle.Turtle()
hatba1.speed(0)
hatba1.shape("square")
hatba1.color("blue")
hatba1.shapesize(stretch_wid=5, stretch_len=1)
hatba1.penup()
hatba1.goto(-350, 0)
# hatba 2 :
hatba2 = turtle.Turtle()
hatba2.speed(0)
hatba2.shape("square")
hatba2.color("red")
hatba2.shapesize(stretch_wid=5, stretch_len=1)
hatba2.penup()
hatba2.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
#functions
def hatba1_up():
    y = hatba1.ycor()
    y += 20
    hatba1.sety(y)
def hatba1_down():
    y = hatba1.ycor()
    y -= 20
    hatba1.sety(y)
def hatba2_up():
    y = hatba2.ycor()
    y += 20
    hatba2.sety(y)
def hatba2_down():
    y = hatba2.ycor()
    y -= 20
    hatba2.sety(y)
#keyboard bindings
wind.listen()
wind.onkeypress(hatba1_up, "z")
wind.onkeypress(hatba1_down, "d")
wind.onkeypress(hatba2_up, "Up")
wind.onkeypress(hatba2_down, "Down")
# main game loop
while True:
    wind.update()
