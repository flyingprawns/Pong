from turtle import Turtle

BALL_COLOR = "white"


class Ball(Turtle):
    def __init__(self, position):
        super().__init__(shape="circle")
        self.color(BALL_COLOR)
        self.penup()
        self.speed("fastest")
        self.goto(position)
        # x_move, y_move: how much the ball moves per frame
        self.x_move = 50
        self.y_move = 50

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
