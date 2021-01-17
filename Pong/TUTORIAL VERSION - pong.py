# Simple pong in Python 3 for Beginners
# Python 3.9.1 on Windows
# Tutorial provided by TokyoEdtech
# His YouTube: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
# The purpose of me following these tutorials is to 1) practice, 2) Improve upon
# the base code. I will have a tutorial folder with my minor tweaks. I will
# have a secondary folder where I've improved upon the code and added new features.

import turtle
import winsound
import platform

wn = turtle.Screen()
wn.title("Pong by C.Hill")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("circle")
ball1.color("white")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.15
ball1.dy = 0.15

# Ball 2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("blue")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.15
ball2.dy = -0.15

balls = [ball1, ball2]

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions to move paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def play_sound(sound_file, time = 0):
        # Windows
        if platform.system() == "Windows":
                winsound.PlaySound(sound_file, winsound.SND_ASYNC)
        elif platform.system() == "Linux":
                os.system("aplay -q {}&".format(sound_file))
        else:
                os.system("afplay {}&".format(sound_file))

        # Repeat sound
        if time > 0:
                turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time * 1000))
    
# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    for ball in balls:
        # move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # border checking
        if ball.ycor() > 290:
            play_sound("bounce.wav")
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            play_sound("bounce.wav")
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

        # paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            play_sound("bounce.wav")
            ball.setx(340)
            ball.dx *= -1      

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            play_sound("bounce.wav")
            ball.setx(-340)
            ball.dx *= -1

    # AI Player
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball
            
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
        paddle_b_up()

    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
        paddle_b_down()
