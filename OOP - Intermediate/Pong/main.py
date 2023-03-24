import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

SCREEN_REFRESH_RATE = 144

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(height=600, width=800)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
score = Score()

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(1/SCREEN_REFRESH_RATE)

    #Detection collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    #Detection collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330 ):
        ball.paddle_bounce()
        ball.increase_speed()

    #Detection for scoring point
    if ball.xcor() > 400:
        score.increment_score(1)
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()
        ball.speed_reset()
        ball.ball_reset()

    elif ball.xcor() < -400:
        score.increment_score(2)
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()
        ball.speed_reset()
        ball.ball_reset()


screen.exitonclick()