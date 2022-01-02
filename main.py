from turtle import Turtle, Screen
from player import Player
from cars import Cars
from score import Score
import time



player = Player()
car = Cars()
score = Score()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Turtle Crossing")

screen.listen()
screen.onkey(player.up,"Up")

game_on = True
level = 1
MOVE_DISTANCE = 5

while game_on == True:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars(MOVE_DISTANCE)
    if player.ycor()>230:
        player.start()
        level+=1
        score.increase_level(level)
        MOVE_DISTANCE+=4
    for i in car.allcars:
        if player.distance(i)<20:
            screen.clear()
            score.game_over(level)
            game_on = False
            screen.exitonclick()
        
        
