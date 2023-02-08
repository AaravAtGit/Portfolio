from turtle import Turtle
import random

COLORS = ["#83FFE6", "#FF5F5F", "#FDB827", "#FA4EAB", "#50D890", "#83FFE6"]
class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        # if self.xcor() > 200:
        #     self.turn()
        self.add = 10

    def move_X(self):
        x,y = self.pos()
        self.goto(x+self.add,y)


    def move_Y(self):
        x,self.y = self.pos()
        self.goto(x,self.y-10)
    
    def turn(self):
        self.add =  self.add * -1


