import turtle
from ball import Ball
from player import Paddle
from time import sleep
from bricks import Brick
import multiprocessing


screen = turtle.Screen()
screen.bgcolor("#222831")
screen.title("Breakout!")
screen.setup(width=1.0, height=1.0) 

ROWS = 4
COLS = 12
BRICK_WIDTH = 120
BRICK_HEIGHT = 80
START_X = -600
START_Y = 200

player = Paddle(0,-250)
screen.onkeypress(player.up,"d")
screen.onkeypress(player.down,"a")
screen.listen()

ball = Ball()
ball.goto(0,-220)


bricks = []
turtle.color("#EEEEEE")
turtle.hideturtle()

# playsound("C:/Users/user/Downloads/Magenta_Storm.mp3")


for row in range(ROWS):
    for col in range(COLS):
        brick = Brick()
        brick.goto(START_X + col * BRICK_WIDTH, START_Y - row * BRICK_HEIGHT)
        bricks.append(brick)





game_is_on = True
turtle.tracer(10) 
while game_is_on:
    sleep(0.02)
    ball.move()
    screen.update()
    # bonces the ball from top and bottom wall
    if ball.ycor() > 300:
        ball.bounce()

    if (ball.xcor() > player.xcor() - 120) and (ball.xcor() < player.xcor() + 120) and (ball.ycor() < player.ycor() + 20) and (ball.ycor() > player.ycor() - 20) :
        ball.bounce()


    if ball.xcor() > 650:
        ball.bounceX()

    if ball.xcor() < -650:
        ball.bounceX()

    if ball.ycor() < -300:
        game_is_on = False
        turtle.write("GAME OVER", align="center", font=("Cooper Black", 25, "italic"))


    for brick in bricks:
        if (ball.xcor() > brick.xcor() - BRICK_WIDTH/2 and
            ball.xcor() < brick.xcor() + BRICK_WIDTH/2 and
            ball.ycor() > brick.ycor() - BRICK_HEIGHT/2 and
            ball.ycor() < brick.ycor() + BRICK_HEIGHT/2):
            # collision detected
            ball.bounce()
            print("BOOM")
            brick.hideturtle()
            bricks.remove(brick)


    if len(bricks) < 1:
        turtle.write("YOU WON GG!", align="center", font=("Cooper Black", 25, "italic"))

screen.exitonclick()

