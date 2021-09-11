from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

PADDLE_LEFT_POSITION = (-355, 0)
PADDLE_RIGHT_POSITION = (350, 0)
BALL_POSITION = (-200, 0)

# Create game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

# Create paddles and ball
paddle_left = Paddle(PADDLE_LEFT_POSITION)
paddle_right = Paddle(PADDLE_RIGHT_POSITION)
ball = Ball(BALL_POSITION)
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
    # Move ball
    ball.move()
    # Detect collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    # Update screen and wait 0.5 seconds
    screen.update()
    time.sleep(0.5)

# Exit on click
screen.exitonclick()
