from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
ROTATION = 90
DIRECTION = {"Right": 0, "Up": 90, "Left": 180, "Down": 270}


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment(position=STARTING_POSITION[i])

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DIRECTION["Down"]:
            self.snake_head.setheading(DIRECTION["Up"])

    def down(self):
        if self.snake_head.heading() != DIRECTION["Up"]:
            self.snake_head.setheading(DIRECTION["Down"])

    def left(self):
        if self.snake_head.heading() != DIRECTION["Right"]:
            self.snake_head.setheading(DIRECTION["Left"])

    def right(self):
        if self.snake_head.heading() != DIRECTION["Left"]:
            self.snake_head.setheading(DIRECTION["Right"])
