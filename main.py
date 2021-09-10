from turtle import Screen
from paddle import Paddle

PADDLE_1_POSITION = (300, 0)
PADDLE_2_POSITION = (-305, 0)

# Create game screen
screen = Screen()
screen.setup(width=640, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

# Create two paddles
paddle_1 = Paddle(PADDLE_1_POSITION)
paddle_2 = Paddle(PADDLE_2_POSITION)
screen.update()

# Exit on click
screen.exitonclick()
