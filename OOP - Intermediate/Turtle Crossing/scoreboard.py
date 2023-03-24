from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-290, 250)
        self.write(f"Level: {self.score}", font=FONT)

    def score_increase(self):
        self.clear()
        self.score +=1
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="Center", font=FONT)