import turtle

from tkinter import messagebox


wn = turtle.Screen()
wn.title("PONG GAME")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle_A

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.color("black")
paddle_A.shape('square')
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-385, 0)

# paddle_B

paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.color("black")
paddle_B.shape('square')
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(380, 0)

# Ball

Ball = turtle.Turtle()
Ball.speed(0)
Ball.color("black")
Ball.shape('circle')
Ball.penup()
Ball.shapesize(stretch_wid=1, stretch_len=1)

Ball.goto(0, 0)
Ball.dx = 2
Ball.dy = -2

# pen

pen = turtle.Turtle()
pen.color("Black")
pen.penup()
pen.speed(0)
pen.hideturtle()
pen.goto(0, 280)
pen.write('PLAYER_A: 0  PLAYER_B: 0', align='center', font={'Courier', 20, 'normal'})

# Score
score_A = 8
score_B = 8


# Paddle_Function
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)


def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)


def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


# keyboard_function

wn.listen()
wn.onkeypress(paddle_A_up, "w")
wn.onkeypress(paddle_A_down, "s")

wn.onkeypress(paddle_B_up, "e")
wn.onkeypress(paddle_B_down, "d")

# main Loop

while True:
    wn.update()

    # Ball Movement

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border

    if Ball.ycor() > 280:
        Ball.sety(280)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 380:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write(f"PLAYER_A : {score_A}  PLAYER_B : {score_B}", align='center', font={'Courier', 20, 'normal'})
        if score_A == 10:
            messagebox.showinfo("Game Ended" , ''' WIN : PLAYER_B
LOSE :PLAYER_A''')
            pen.goto(0,0)
            pen.write("CLick to exit from game", align = "center" , font={'Courier' , 30, ' normal'}) 
            wn.exitonclick()
        if score_B == 10:
            messagebox.showinfo("Game Ended" , ''' WIN : PLAYER_A
LOSE :PLAYER_B''')
            pen.goto(0,0)
            pen.write("CLick to exit from game", align = "center" , font={'Courier' , 30, ' normal'})
            wn.exitonclick()





    if Ball.xcor() < -380:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write(f"PLAYER_A : {score_A}  PLAYER_B : {score_B}", align='center', font={'Courier', 20, 'normal'})

    # paddle and Ball Collision

    if (Ball.xcor() > 370 and Ball.xcor() < 380) and (
            Ball.ycor() < paddle_B.ycor() + 40 and Ball.ycor() > paddle_B.ycor() - 40):
        Ball.setx(370)
        Ball.dx *= -1

    if (Ball.xcor() < -370 and Ball.xcor() > - 380) and (
            Ball.ycor() < paddle_A.ycor() + 40 and Ball.ycor() > paddle_A.ycor() - 40):
        Ball.setx(-370)
        Ball.dx *= -1


