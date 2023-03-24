from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 1
        self.y_move = 1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move )

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def speed_reset(self):
        self.x_move = 1
        self.y_move = 1

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.bounce()