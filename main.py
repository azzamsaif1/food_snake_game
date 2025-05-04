from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # لإيقاف التحديث التلقائي

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# التحكم
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # *هنا يتم فحص إذا أكل الطعام*
    if snake.head.distance(food) < 15:
        food.refresh()              # <<< هذا هو مكانها الصحيح
        snake.extend()
        scoreboard.increase_score()

    # الاصطدام بالحائط
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.game_over()
        is_game_on = False

    # الاصطدام بالجسم
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
