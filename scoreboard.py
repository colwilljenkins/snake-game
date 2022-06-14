from turtle import Turtle
FONT = 'courier'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        self.color('white')
        self.write(f'Scoreboard: {self.score}', align='center', font=(FONT, 15, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Scoreboard: {self.score}', align='center', font=(FONT, 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=(FONT, 15, 'bold'))