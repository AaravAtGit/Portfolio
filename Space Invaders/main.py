from turtle import Turtle,Screen
from player import Player
from bricks import Brick

screen = Screen()
screen.bgcolor("black")
screen.setup(700,800)

player = Player()

screen.onkeypress(player.move_left,"d")
screen.onkeypress(player.move_right,"a")
screen.listen()

ROWS = 3
COLS = 5
START_X = -200
START_Y = 350
BRICK_WIDTH = 80
BRICK_HEIGHT = 80
 
bricks = []


for row in range(ROWS):
    for col in range(COLS):
        brick = Brick()
        brick.goto(START_X + col * BRICK_WIDTH, START_Y - row * BRICK_HEIGHT)
        bricks.append(brick)

game_is_on = True
count = 0
while game_is_on:
    for brick in bricks:
        brick.move_X()
        if brick.xcor() > 300:
            brick.turn()
        elif brick.xcor() < -300:
            brick.turn()
        if count % 30 == 0:
            brick.move_Y()
    count+=1
screen.mainloop()

