from turtle import Screen
from paddle import Paddle

PADDLE_1_POSITION = (-355, 0)
PADDLE_2_POSITION = (350, 0)

# Create game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")

# Create two paddles
paddle_1 = Paddle(PADDLE_1_POSITION)
paddle_2 = Paddle(PADDLE_2_POSITION)
screen.update()

# Listen for user input
screen.listen()
screen.onkey(key="w", fun=paddle_1.up)
screen.onkey(key="s", fun=paddle_1.down)
screen.onkey(key="Up", fun=paddle_2.up)
screen.onkey(key="Down", fun=paddle_2.down)

# Exit on click
screen.exitonclick()
