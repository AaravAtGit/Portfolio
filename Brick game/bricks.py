from turtle import Turtle
import random

COLORS = ["#83FFE6", "#FF5F5F", "#FDB827", "#FA4EAB", "#50D890", "#83FFE6"]
class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=2, stretch_len=4)
        self.color(random.choice(COLORS))
        self.penup()
