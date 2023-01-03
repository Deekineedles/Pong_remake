from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 50, "bold")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.pu()
        self.color("white")
        self.goto(0, 230)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score1}     {self.score2}", align=ALIGNMENT, font=FONT)

    def midline(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, -600)
        self.setheading(90)
        for i in range(20):
            self.pd()
            self.fd(15)


