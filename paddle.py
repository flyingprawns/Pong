from turtle import Turtle

PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__(shape="square")
        self.setheading(90)
        self.turtlesize(stretch_len=5)
        self.color(PADDLE_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(paddle_position)

    def up(self):
        self.sety(self.ycor()+75)

    def down(self):
        self.sety(self.ycor()-75)
