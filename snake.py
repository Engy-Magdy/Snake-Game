from turtle import Turtle,Screen
window=Screen()
class Snake:
    def __init__(self):
        self.turtles=[]
        self.position=[(-40,0),(-20,0),(0,0)]
        self.creat_snake()
        self.head=self.turtles[-1]
    def creat_snake(self):
        for i in range(len(self.position)):
          new_turtle=Turtle(shape="square")
          new_turtle.color("white")
          new_turtle.penup()
          new_turtle.goto(self.position[i])
          self.turtles.append(new_turtle)
    def move(self):
        for i in range (len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.turtles[-1].forward(20)
    def up (self):
        self.head.setheading(90)
    def down (self):
        self.head.setheading(270)
    def right (self):
        self.head.setheading(0)
    def left (self):
        self.head.setheading(180)
    def extent(self):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0,new_segment)
   


        


        

