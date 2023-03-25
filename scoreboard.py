from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.color("black")
        self.write(f"Level = {self.level}", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level = {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.hideturtle()
        self.penup()
        self.write("Game Over!", font=FONT, align="center")


