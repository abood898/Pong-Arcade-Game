from turtle import Turtle
FONT = ("Arial", 60, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(xpos, 220)
        self.hideturtle()
        self.display_score()

    def increment_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)
