from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
paddle = Paddle()
screen.listen()
ball = Ball()
scoreboard = Scoreboard()



screen.onkey(paddle.move_up_right, "Up")
screen.onkey(paddle.move_down_right, "Down")
screen.onkey(paddle.move_up_left, "w")
screen.onkey(paddle.move_down_left, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle.paddles[0]) < 50 and ball.xcor() > 335:
        ball.paddle_bounce_left()
        ball.speed_upl()
    if ball.distance(paddle.paddles[1]) < 50 and ball.xcor() < -335:
        ball.paddle_bounce_right()
        ball.speed_up()
    if ball.xcor() > 380:
        scoreboard.score1 += 1
        ball.reset_position(scoreboard)
    elif ball.xcor() < -380:
        scoreboard.score2 += 1
        ball.reset_position(scoreboard)


        # or ball.xcor() < -370




screen.exitonclick()