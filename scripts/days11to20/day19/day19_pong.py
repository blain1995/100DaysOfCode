from turtle import Screen
from scoreboard import Scoreboard
from players import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
ball = Ball()

paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))

screen.listen()
screen.onkey(paddle_1.go_up, "a")
screen.onkey(paddle_1.go_down, "z")
screen.onkey(paddle_2.go_up, "Up")
screen.onkey(paddle_2.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_1) < 50 and ball.xcor() < -320 or ball.distance(paddle_2) < 50 and ball.xcor() > 320:
        ball.rebound()

    if ball.xcor() > 380:
        score.score1 += 1
        score.clear()
        score.display_score()
        ball.reset()

    elif ball.xcor() < -380:
        score.score2 += 1
        score.clear()
        score.display_score()
        ball.reset()

    if score.score1 > 9:
        score.clear()
        score.game_over("left")
        game_is_on = False

    elif score.score2 > 9:
        score.clear()
        score.game_over("right")
        game_is_on = False

screen.exitonclick()
