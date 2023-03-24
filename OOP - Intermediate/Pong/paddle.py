from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.original_position = position
        self.color("white")
        self.penup()
        self.shape("square")
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)

    def paddle_reset(self):
        self.goto(self.original_position)