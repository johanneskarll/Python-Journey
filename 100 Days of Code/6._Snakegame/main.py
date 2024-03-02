from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game Xixixixi")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        scoreboard.increasescore()

    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -298 or snake.head.ycor() > 299 or snake.head.ycor() < -298:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # for segment in snake.snakebody:
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
        
    for segment in snake.snakebody[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
           
    
screen.exitonclick()
