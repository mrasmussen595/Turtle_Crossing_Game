from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.showturtle()
        self.start()
        
    def start(self):
        self.goto(0,-260)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
