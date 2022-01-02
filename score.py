from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200,230)
        self.write(f"Level: 1", False, align= "center", font= 'Arial')
    
    def increase_level(self, i):
        self.clear()
        self.write(f"Level: {i}", False, align= "center", font= 'Arial')
    
    def game_over(self, level):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over! Final Level: {level}", False, align= "center", font= 'Arial')
