from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.save_high_score()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()
        self.score = 0
        with open("high_score.txt", mode="w") as data:
            data.write(f"{self.high_score}")