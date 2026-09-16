from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}",font=("arial",24,"normal"),align="center")
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        window=Screen()
        window.bgcolor("darkred")
        self.goto(0,0)
        self.write(f"Game over\nYour Score:{self.score}",font=("arial",30,"normal"),align="center")
    
