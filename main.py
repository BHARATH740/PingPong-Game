from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# game_point = screen.textinput(title="Set Game point", prompt="What will you like the game point to be:")
screen.title("PongGame")
screen.tracer(0)

# create paddle right
paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()

# Moving paddle
screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()

    # collision with r_paddle
    if ball.xcor() >= 330:
        if ball.distance(paddle_r) <= 50:
            ball.x_bounce()

    # collision with l_paddle
    if ball.xcor() == -330:
        if ball.distance(paddle_l) <= 50:
            ball.x_bounce()

    # collision with right wall
    if ball.xcor() == 380:
        score.inc_l_score()
        time.sleep(0.5)
        ball.reset_pos()

    # collision with right wall
    if ball.xcor() == -380:
        score.inc_r_score()
        time.sleep(0.5)
        ball.goto(0, 0)
        ball.reset_pos()

    if score.r_score == 10 or score.l_score == 10:
        game_is_on = False
        print(f"Score: Left Player \t Right Player")
        print(f"           {score.l_score}    \t     {score.r_score}")
        print("\n")
        if score.l_score == 10:
            print(f"Congrats!! Left Player is the Winner!!")
        else:
            print(f"Congrats!! Right Player is the Winner!!")

