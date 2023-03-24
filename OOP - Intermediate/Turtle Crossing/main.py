import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

REFRESH_RATE = 144

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.up, "Up")
screen.onkey(player.back, "Down")
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
count = 0
while game_is_on:
    time.sleep(1/REFRESH_RATE)
    screen.update()
    if count <= (50 - scoreboard.score * 5):
        count += 1
    else:
        cars.create_car()
        count = 0
    cars.move_cars()

    #Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect a successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.speed_up()
        scoreboard.score_increase()

screen.exitonclick()