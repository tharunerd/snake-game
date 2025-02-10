import turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # ✅ Corrected positions
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake :

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_positions:
            snake_body = turtle.Turtle("circle")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(position)
            self.segments.append(snake_body)

    def add_segment(self,position):
        new_segment = turtle.Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


