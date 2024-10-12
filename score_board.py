from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("High_Score.txt", mode="r") as High_Score:
            self.high_score = int(High_Score.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_Score.txt", mode = "w") as High_Score:
                High_Score.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.clear()
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


