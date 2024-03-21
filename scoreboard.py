from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt", "r") as file:
            score = file.read()
            self.highest_score = int(score)
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("highest_score.txt", "r") as file:
            new_high_score = file.read()
            self.highest_score = int(new_high_score)
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align="center", font=("Arial", 18, "normal"))
    # This function will increase the score every time the snake collides with the food

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    # If the players score is greater than the highest score, then the highest score will be the new highest score and will be saved the the file.

    def reset_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as file:
                file.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()