from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def checklevel (self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(0,-280)
            return True
        else:
            return False
