from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 16, "bold"))
        self.hideturtle()

    def inc_r_score(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 16, "bold"))

    def inc_l_score(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Arial", 16, "bold"))


