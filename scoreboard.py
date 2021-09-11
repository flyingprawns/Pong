from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")
LEFT_SCORE_POSITION = (-100, 200)
RIGHT_SCORE_POSITION = (100, 200)


class ScoreBoard(Turtle):
    def __init__(self):
        # Set scoreboard appearance
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        # Track the score
        self.l_score = 0
        self.r_score = 0
        # Display the scores
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.getscreen().update()
