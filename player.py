from turtle import Turtle

MOVING_DISTANCE = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        segment = Turtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def create_player(self, side):
        if side == "left":
            self.goto(-280, 0)
        else:
            self.goto(278, 0)

    def refresh(self, side):
        if side == "left":
            self.goto(-280, 0)
        else:
            self.goto(278, 0)

    def move(self, direction):
        if direction == "Up" or direction == "w":
            if self.ycor() <= 220:
                self.goto(self.xcor(), self.ycor() + MOVING_DISTANCE)
        else:
            if self.ycor() >= -220:
                self.goto(self.xcor(), self.ycor() - MOVING_DISTANCE)
