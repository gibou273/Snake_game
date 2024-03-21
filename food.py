from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.move_food()

    def move_food(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 280)
        self.goto(x=new_x, y=new_y)
