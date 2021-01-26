from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((375, 0))
left_paddle = Paddle((-375, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
# Events for right paddle
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")

# Events for left paddle
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")

game_is_on = True
while game_is_on:
    print("while loop on")
    paddle_bounce_count = 0
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Ball - upper wall collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Ball - right paddle collision detection
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        print("paddle bounce")
        ball.bounce_paddle("right_paddle")

    # Ball - left paddle collision detection
    if ball.distance(left_paddle) < 45 and ball.xcor() < -320:
        print("paddle bounce")
        ball.bounce_paddle("left_paddle")

    # Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        score.left_point()

    # Left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        score.right_point()

screen.exitonclick()