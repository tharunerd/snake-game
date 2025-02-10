import turtle

class Scoreboard(turtle.Turtle):  # Inheriting from Turtle class
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_scoreboard()  # Call this method to display the initial score

    def update_scoreboard(self):
        """Clear and rewrite the score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase the score and update display"""
        self.score += 1
        self.update_scoreboard()
