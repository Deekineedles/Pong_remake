from turtle import Turtle
import random
from scoreboard import Scoreboard

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_pos_move = 10
        self.y_pos_move = 10

    def move(self):
        new_x = self.x_pos_move + self.xcor()
        new_y = self.y_pos_move + self.ycor()
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_pos_move *= -1

    def paddle_bounce_left(self):
        self.x_pos_move = -abs(self.x_pos_move)

    def paddle_bounce_right(self):
        self.x_pos_move = abs(self.x_pos_move)

    def reset_position(self, scoreboard):
        scoreboard.clear()
        self.paddle_bounce_right()
        self.setposition(0, 0)
        self.x_pos_move = 10
        self.y_pos_move = 10

        scoreboard.update_scoreboard()

    def speed_up(self):
        self.x_pos_move = abs(self.x_pos_move) + 2
        self.y_pos_move = abs(self.y_pos_move) + 2

    def speed_upl(self):
        self.x_pos_move = -abs(self.x_pos_move) + -2
        self.y_pos_move = -abs(self.y_pos_move) + -2




