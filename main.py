from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

is_snake_moving = True
while is_snake_moving:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.move_food() # The food will be moved to a new random position
        snake.extend_snake() # A new segment will be created and added to the snake, so the snake will be longer
        scoreboard.increase_score() # The playes score will be increased
    # Detect collison with wall
    if snake.snake_head.xcor() < -280 or snake.snake_head.xcor() > 280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    # Detect collision with snake tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()


screen.mainloop()
