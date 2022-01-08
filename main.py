from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def start():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.right, 'Right')

    game_is_on = True
    new_game = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect colision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow_snake()
            scoreboard.increase_score()

        # Detect colision with wall
        if snake.head.xcor() > 298 or snake.head.xcor() < -298 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
            game_is_on = False
            scoreboard.game_over()

        # Detect colision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

        # for segment in snake.segments:
        #     if segment == snake.head:
        #         pass
        #     elif snake.head.distance(segment) < 10:
        #         game_is_on = False
        #         scoreboard.game_over()

    screen.exitonclick()


start()
