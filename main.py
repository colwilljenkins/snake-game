from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Window set up
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title('SNAKE GAME')
screen.bgcolor('medium violet red')

# importing supporting classes
snake = Snake()
food = Food()
score = Scoreboard()

# for while loop
game_is_on = True

# calibrating keys
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # detect collision ith wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        score.update_score()
        snake.reset()


    # collision with self
    for segment in snake.all_snake[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            score.update_score()
            snake.reset()


screen.exitonclick()
