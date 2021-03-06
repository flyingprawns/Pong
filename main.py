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

    # Detect wall collisions
    wall_collision = ball.ycor() > 270 or ball.ycor() < -270
    if wall_collision:
        ball.wall_bounce()

    # Detect paddle collisions
    paddle_collision = (ball.distance(right_paddle) < 50 and 320 < ball.xcor() < 380) or \
            (ball.distance(left_paddle) < 50 and -320 > ball.xcor() > -380)
    if paddle_collision:
        ball.paddle_bounce()

    # Detect out of bounds
    out_of_bounds = ball.xcor() > 400 or ball.xcor() < -400
    if out_of_bounds:
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
    time.sleep(ball.move_speed)

# Exit on click
screen.exitonclick()
