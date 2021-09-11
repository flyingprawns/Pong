from turtle import Turtle

BALL_COLOR = "white"

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color(BALL_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(0, 0)