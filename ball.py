from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slowest")
        self.y_move = 10
        self.x_move = 10
        self.refresh()

    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def board_bounce(self):
        self.x_move *= -1
