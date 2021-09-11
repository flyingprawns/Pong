from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE_LEFT_POSITION = (-355, 0)
PADDLE_RIGHT_POSITION = (355, 0)
BALL_POSITION = (0, 0)

# Create game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)

# Create paddles, ball, scoreboard
left_paddle = Paddle(PADDLE_LEFT_POSITION)
right_paddle = Paddle(PADDLE_RIGHT_POSITION)
ball = Ball(BALL_POSITION)
score = ScoreBoard()
screen.update()

# Listen for user input
screen.listen()
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

# Start game
game_is_on = True
while game_is_on:
    ball.move()
    # Detect collisions
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()
    # Detect paddle collision
    if (ball.distance(right_paddle) < 50 and 320 < ball.xcor() < 380) or \
            (ball.distance(left_paddle) < 50 and -320 > ball.xcor() > -380):
        ball.paddle_bounce()
    # Detect out of bounds
    if ball.xcor() > 400 or ball.xcor() < -400:
        # Update score
        if ball.get_side() == "left":
            score.r_score += 1
        elif ball.get_side() == "right":
            score.l_score += 1
        score.display_score()
        # Reset game state
        time.sleep(1)
        ball.reset_ball()
        left_paddle.goto(PADDLE_LEFT_POSITION)
        right_paddle.goto(PADDLE_RIGHT_POSITION)
    # Update screen and wait 0.5 seconds
    screen.update()
    time.sleep(0.1)

# Exit on click
screen.exitonclick()
