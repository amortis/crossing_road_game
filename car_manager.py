from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []

    def car_generator(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(choice(COLORS))
            car.setpos(300, randint(-250, 250))
            self.cars.append(car)

    def move_cars(self, level):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1))

    def reset(self):
        for car in self.cars:
            car.goto(-350,0)
