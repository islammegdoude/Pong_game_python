# imported turtle module
import turtle

wind = turtle.Screen()
wind.title("Pong by ElMegdoude")
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
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4
#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)


# functions
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


# keyboard bindings
wind.listen()
wind.onkeypress(hatba1_up, "z")
wind.onkeypress(hatba1_down, "d")
wind.onkeypress(hatba2_up, "Up")
wind.onkeypress(hatba2_down, "Down")
# main game loop
while True:
    wind.update()

    # move th ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Palyer 1 : {} **** Player 2 : {}".format(score1, score2), align="center", font=("Courier", 22, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Palyer 1 : {} **** Player 2 : {}".format(score1, score2), align="center", font=("Courier", 22, "normal"))

    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<hatba2.ycor()+40 and ball.ycor()>hatba2.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < hatba1.ycor() + 40 and ball.ycor() > hatba1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1