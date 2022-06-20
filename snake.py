from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.all_snake = []
        self.create_snake()
        self.head = self.all_snake[0]

    def create_snake(self):
        for body_index in STARTING_POSITION:
            self.add_segment(body_index)

    def add_segment(self, body_index):
        new_body = Turtle(shape='square')
        new_body.color('white')
        new_body.penup()
        new_body.goto(body_index)
        new_body.speed(2)
        self.all_snake.append(new_body)

    def reset(self):
        for seg in self.all_snake:
            seg.goto(1000,1000)
        self.all_snake.clear()
        self.create_snake()
        self.head = self.all_snake[0]

    def extend(self):
        self.add_segment(self.all_snake[-1].position())

    def move(self):
        for segment in range(len(self.all_snake) - 1, 0, -1):
            new_x = self.all_snake[segment - 1].xcor()
            new_y = self.all_snake[segment - 1].ycor()
            self.all_snake[segment].goto(new_x, new_y)
        self.all_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
