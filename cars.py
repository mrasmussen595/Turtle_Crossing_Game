from turtle import Turtle
import random
color_list = ["red", "green", "blue", "yellow", "black","purple"]

class Cars(Turtle):
    
    def __init__(self):

        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(600,600)
        self.allcars = []
    
    def create_car(self):
        chance = random.randint(1,5)
        if chance ==1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(color_list))
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.goto(300,random.randint(-250,200))
            new_car.showturtle()
            self.allcars.append(new_car)
    
    def move_cars(self, i):
        for car in self.allcars:
            car.backward(i)
