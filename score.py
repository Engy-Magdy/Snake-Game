from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.update_score()

    def get_highscore(self):
        with open("highscore.txt") as file:
            return int(file.read())
        
    def save_highscore(self):
        with open("highscore.txt","w") as file:
            file.write(str(self.highscore))


    def update_score(self):
        self.write(f"Score: {self.score}   High Score:{self.highscore}",font=("arial",24,"normal"),align="center")
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()
        
  def game_over(self):
        window=Screen()
        self.clear()
        window.bgcolor("darkred")
        self.goto(0,0)
        if self.score>self.highscore:
            self.highscore=self.score
            self.save_highscore()
        self.write(f"----------Game over----------\n\nYour Score:{self.score}\n\nHigh Score:{self.highscore}",font=("arial",30,"normal"),align="center")
    
        self.write(f"Game over\nYour Score:{self.score}",font=("arial",30,"normal"),align="center")
    
