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
        self.x_move = 20
        self.y_move = 20
        # Track the last paddle to bounce the ball. This prevents "double bounces".
        self.last_bounce = "none"

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        # Calculate which side the ball is on
        if self.xcor() > 0:
            current_side = "right"
        else:
            current_side = "left"
        # Prevent multiple bounces on one side
        if current_side != self.last_bounce:
            self.x_move *= -1
            self.last_bounce = current_side

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.last_bounce = "none"
