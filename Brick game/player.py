from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=15,stretch_wid=1)
        self.penup()
        self.goto(x,y)

    def up(self):
        new_x = self.xcor() + 20
        self.goto(new_x,self.ycor())

        if self.xcor() > 600:
            self.goto(600, self.ycor())

        if self.xcor() < -600:
            self.goto(-600, self.ycor())

        if self.xcor() > 600:
            self.goto(600, self.ycor())

        if self.xcor() < -600:
            self.goto(-600, self.ycor())

    def down(self):
        new_x = self.xcor() - 20
        self.goto(new_x,self.ycor())
        if self.xcor() > 600:
            self.goto(600, self.ycor())

        if self.xcor() < -600:
            self.goto(-600, self.ycor())

        if self.xcor() > 600:
            self.goto(600, self.ycor())

        if self.xcor() < -600:
            self.goto(-600, self.ycor())