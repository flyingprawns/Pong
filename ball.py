from turtle import Turtle

BALL_COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color(BALL_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)

    def move(self):
        new_coord = (self.xcor()+50, self.ycor()+50)
        self.goto(new_coord)
