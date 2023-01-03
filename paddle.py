from turtle import Turtle
PADDLE_SPEED = 20
class Paddle:

    def __init__(self):
        self.position = 350
        self.paddles = []
        for _ in range(2):
            paddle = Turtle("square")
            paddle.color("white")
            paddle.shapesize(stretch_wid=1, stretch_len=5)
            paddle.setheading(90)
            paddle.pu()
            paddle.setposition(self.position, 0)
            self.position = 350 * -1
            self.paddles.append(paddle)






    def move_up_right(self):
        self.paddles[0].forward(PADDLE_SPEED)

    def move_down_right(self):

        self.paddles[0].backward(PADDLE_SPEED)

    def move_up_left(self):

        self.paddles[1].forward(PADDLE_SPEED)

    def move_down_left(self):

        self.paddles[1].backward(PADDLE_SPEED)


