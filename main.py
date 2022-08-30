import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.up, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_generator()
    car_manager.move_cars(scoreboard.level)

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == FINISH_LINE_Y:
        player.reset()
        scoreboard.reset()
        car_manager.reset()

screen.exitonclick()
