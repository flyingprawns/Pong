from turtle import Screen
from paddle import Paddle

PADDLE_LEFT_POSITION = (-355, 0)
PADDLE_RIGHT_POSITION = (350, 0)

# Create game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

# Create two paddles
paddle_left = Paddle(PADDLE_LEFT_POSITION)
paddle_right = Paddle(PADDLE_RIGHT_POSITION)
screen.update()

# Listen for user input
screen.listen()
screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)

# Start game
game_is_on = True
while game_is_on:
    screen.update()

# Exit on click
screen.exitonclick()
