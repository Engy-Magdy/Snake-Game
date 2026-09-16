from turtle import Turtle
import random
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5,0.5)
        self.penup()
        self.appear()
    
    def appear (self):
        random_X=random.randint(-350,350)
        random_Y=random.randint(-350,350)
        self.goto(random_X,random_Y)
