from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player = Turtle("triangle")
        # self.turtlesize(stretch_wid=5,stretch_len=5)
        self.player.penup()
        self.player.goto(0,-350)
        self.player.color("#50C878")
        self.player.left(90)
        self.player.shapesize(3,3)

    def move_left(self):
        x,y = self.player.pos()
        new_x = x + 10
        self.player.goto(new_x,y)

    def move_right(self):
        x,y = self.player.pos()
        new_x = x - 10
        self.player.goto(new_x,y)