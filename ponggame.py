import time
from turtle import Screen, Turtle
from player import Player
from scoreboard import ScoreBoard
from ball import Ball
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.player1 = Player()
        self.player2 = Player()
        self.player1_Score = ScoreBoard(xpos=-40)
        self.player2_Score = ScoreBoard(xpos=40)
        self.ball = Ball()
        self.start_game()

    def make_screen(self):
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.title("Pong Arcade Game")
        self.screen.bgcolor("black")
        # Dotted line
        line = Turtle()
        line.width(5)
        line.hideturtle()
        line.color("white")
        line.speed("fastest")
        line.penup()
        line.setpos(0, -280)
        line.seth(90)
        for i in range(0, 38):
            if i % 2 == 0:
                line.pendown()
            else:
                line.penup()
            line.fd(15)
        # End

    def start_game(self):
        self.make_screen()
        self.player1.create_player("left")
        self.player2.create_player("right")

        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(self.player1_move_up, "Up")
        self.screen.onkeypress(self.player1_move_down, "Down")
        self.screen.onkeypress(self.player2_move_up, "w")
        self.screen.onkeypress(self.player2_move_down, "s")

        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.ball.move()
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.wall_bounce()
            if self.ball.distance(self.player2) < 50 and self.ball.xcor() > 250:
                self.ball.board_bounce()
            if self.ball.distance(self.player1) < 50 and self.ball.xcor() < -250:
                self.ball.board_bounce()

            if self.ball.xcor() > 280:
                self.refresh()
                self.player1_Score.increment_score()
            if self.ball.xcor() < -280:
                self.refresh()
                self.player2_Score.increment_score()
        self.screen.exitonclick()

    def player1_move_up(self):
        self.player2.move("Up")

    def player1_move_down(self):
        self.player2.move("Down")

    def player2_move_up(self):
        self.player1.move("w")

    def player2_move_down(self):
        self.player1.move("s")

    def refresh(self):
        self.ball.refresh()
        self.player1.refresh("left")
        self.player2.refresh("right")
