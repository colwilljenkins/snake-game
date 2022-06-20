from turtle import Turtle

FONT = 'courier'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        with open('data.txt', mode='r') as data:
            self.highscore = int(data.read())

        self.goto(0, 275)
        self.score = 0
        self.color('white')
        self.write(f'Scoreboard: {self.score} Highscore : {self.highscore}', align='center', font=(FONT, 15, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Scoreboard: {self.score} Highscore : {self.highscore}', align='center', font=(FONT, 15, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
