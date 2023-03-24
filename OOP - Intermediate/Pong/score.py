from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_player = 0
        self.r_player = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.write(f'Score: {self.l_player} - {self.r_player}', align=ALIGNMENT, font=FONT)

    def increment_score(self, player):
        self.clear()
        if player == 1:
            self.l_player += 1
            self.write(f'Score: {self.l_player} - {self.r_player}', align=ALIGNMENT, font=FONT)
        elif player == 2:
            self.r_player += 1
            self.write(f'Score: {self.l_player} - {self.r_player}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER")