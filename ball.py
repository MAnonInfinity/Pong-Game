from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self, paddle):
        if paddle == "right_paddle":
            self.x_move = -(abs(self.x_move))
        elif paddle == "left_paddle":
            self.x_move = abs(self.x_move)
        self.ball_speed *= 0.9

    def reset(self):
        self.goto((0, 0))
        self.ball_speed = 0.1
        self.x_move *= -1
