from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

#Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()


    #detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()




screen.exitonclick()
