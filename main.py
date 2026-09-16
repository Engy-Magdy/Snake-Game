from turtle import Turtle,Screen
import time
window=Screen()
window.setup(800,800)
window.bgcolor("black")
window.title("Snake Game")

from snake import Snake
from food import Food
from score import Scoreboard
food=Food()
snake=Snake()
score=Scoreboard()
game_on=True
while game_on:
    window.tracer(0)
    snake.move()
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,"Down")
    window.onkey(snake.right,"Right")
    window.onkey(snake.left,"Left")
    window.update()
    time.sleep(0.1)
    if snake.head.distance(food)<15:
        food.appear()
        snake.extent()
        score.increase_score()
    if snake.head.xcor()>370 or snake.head.xcor()<-370 or snake.head.ycor()>370 or snake.head.ycor()<-370:  
        game_on=False
        score.game_over()
    for segment in snake.turtles[:-1]:
        if snake.head.distance(segment)<10:
            game_on=False
            score.game_over()
window.exitonclick()
