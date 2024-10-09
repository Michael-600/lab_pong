"""
Additions
- kept the paddles on the screen at all times
- end the game if either player reaches 3 points
-Display Player 1 or 2 wins for 2 secs when player 1 or player 2 reaches 3 points
-added bounce and falling sounds to give a more interactive experience
- changed the paddle size and speed
- added a colourful soccer pitch to the background and renamed the game football pong
- added  randomness to the direction of  the ball and speed
- increase the acceleration by 0.3 everytime it hits the paddle
"""
"""
Created on Sep 13, 2022

@author: Michael Quansah Hayford 
@author: Robert Duvall

This module represents the game of Pong, the first popular arcode game!

Modify the game_step() function to make the game playable
Modify the reset_ball() function to make the ball start in a random direction
"""

import random
import time
import turtle
import os
import random

# choose a name for your game to appear in the title bar of the game window
gameName = 'Football Pong'
# choose the size of your game window
screenWidth = 800
screenHeight = 600
# choose how fast paddles move
paddleSpeed = 40
# choose where paddles are positioned
paddleOffset = 50
# choose where scores are positioned
scoreXOffset = 50
scoreYOffset = 80


# Move the players' paddles up or down based on the speed
def paddle1_up():
    if thePaddle1.ycor() + 50 < 240:
        thePaddle1.sety(thePaddle1.ycor() + paddleSpeed)


def paddle1_down():
    if thePaddle1.ycor() - 50 > -240:
        thePaddle1.sety(thePaddle1.ycor() - paddleSpeed)


def paddle2_up():
    if thePaddle2.ycor() + 50 < 240:
        thePaddle2.sety(thePaddle2.ycor() + paddleSpeed)


def paddle2_down():
    if thePaddle2.ycor() - 50 > -240:
        thePaddle2.sety(thePaddle2.ycor() - paddleSpeed)


def reset_on_click(x, y):
    reset_ball(theBall)


def draw_scene(screen):
    """
    Draw the game's setting.

    Whatever turtles you create here or drawing that you do here will serve as the game's background
    to set the game's theme, but will not be part of the game's action.
    """



    screen.bgpic('Grid.gif')
    screen.bgcolor('lime green')

def draw_paddle(paddle, xPos):
    """
    Draw the interactive piece of the game that the player uses to block the moving ball.
    """
    paddle.speed(0)
    paddle.penup()
    paddle.shape('square')
    paddle.shapesize(4, 1)
    paddle.color('black')
    paddle.goto(xPos, 0)


def draw_score(text, xPos):
    """
    Draw a player's score offset by the given amount from the center of the screen.
    """
    text.speed(0)
    text.penup()
    text.hideturtle()
    text.clear()
    text.color('white')
    text.goto(xPos, screenHeight // 2 - scoreYOffset)
    text.write(str(text.score), align='center', font=('Courier', 64, 'bold'))


def draw_ball(ball):
    """
    Draw the ball that will be moving around the game arena.
    """
    ball.speed(0)
    ball.penup()
    ball.shape('circle')
    ball.color('cyan')


def reset_ball(ball):
    """
    Reset the ball back at the center of the scene after a miss, restart its movement by setting dx and dy variables.
    """
    ball.goto(0, 0)
    ball.dx = 5
    ball.dy = random.randint(-3, 3)

    if ball.dy == 0:
        ball.dy = ball.dy + 2







def game_step():
    """
    Handle game "rules" for every step (i.e., frame or "moment"):
     - movement: move the ball each step?
     - collisions: check if the ball collided with the sides or paddles and then bounce or reset it
    Note, to make the ball appear to bounce, all that is needed is to reverse the appropriate "d" value:
     - if bouncing off the top or bottom, negate theBall.dy
     - if bouncing off either paddle, negate theBall.dx
    """

    # move ball based on its speed
    theBall.goto(theBall.xcor() + theBall.dx, theBall.ycor() + theBall.dy)

    # check if ball hits top or bottom side, bounce it by reversing theBall's dy variable
    if theBall.ycor() >= 240 or theBall.ycor() <= -240:
        theBall.dy = -theBall.dy
        os.system('afplay bounce.wav&')
    # check if the ball got past player 1's paddle (hit the right edge), then reset ball and update player 2's score
    if theBall.xcor() >= screenWidth // 2:
        os.system('afplay falling.wav&')
        theBall.goto(0, 0)
        theScore2Text.score = theScore2Text.score + 1
        draw_score(theScore2Text, -scoreXOffset)


    if theScore2Text.score == 3:
        theScore1Text.score = 0
        theScore2Text.score = 0
        draw_score(theScore1Text, scoreXOffset)
        draw_score(theScore2Text, -scoreXOffset)
        message = turtle.Turtle()
        message.sety(0)
        message.color('Black')
        message.hideturtle()
        message.write('Player 2 Wins!\n New Game Loading...', align='center', font=('Verdana', 30, 'bold'))
        theScreen.update()
        time.sleep(2)
        message.clear()
        theBall.goto(theBall.xcor() + theBall.dx, theBall.ycor() + theBall.dy)

    elif theScore1Text.score == 3:
        theScore1Text.score = 0
        theScore2Text.score = 0
        draw_score(theScore1Text, scoreXOffset)
        draw_score(theScore2Text, -scoreXOffset)
        message = turtle.Turtle()
        message.sety(0)
        message.color('Black')
        message.hideturtle()
        message.write('Player 1 Wins!\n New Game Loading...', align='center', font=('Verdana', 30, 'bold'))
        theScreen.update()
        time.sleep(2)
        message.clear()
        theBall.goto(theBall.xcor() + theBall.dx, theBall.ycor() + theBall.dy)




    # check if the ball got past player 2's paddle (hit the left edge), then reset ball and update player 1's score

    if theBall.xcor() <= -screenWidth // 2:
        os.system('afplay falling.wav&')
        theBall.goto(0, 0)
        theScore1Text.score = theScore1Text.score + 1
        draw_score(theScore1Text, scoreXOffset)



    # check if the ball hits thePaddle1, bounce it by reversing theBall's dx variable
    if theBall.xcor() > thePaddle1.xcor() - 20 and theBall.ycor() < thePaddle1.ycor() + 50 and theBall.ycor() > thePaddle1.ycor() - 50:
        theBall.dx = -theBall.dx 
        os.system('afplay bounce.wav&')

    # check if the ball hits thePaddle2, bounce it by reversing theBall's dx variable
    if theBall.xcor() < thePaddle2.xcor() + 20 and theBall.ycor() < thePaddle2.ycor() + 50 and theBall.ycor() > thePaddle2.ycor() - 50:
        theBall.dx = -theBall.dx
        os.system('afplay bounce.wav&')

    # DO NOT CHANGE - required to see the changes made and keep the game running
    theScreen.update()
    theScreen.ontimer(game_step, 10)


def setup():
    """
    Sets up the initial game scene
    """
    # make the game interactive
    theScreen.tracer(False)
    # listen for key presses
    theScreen.listen()
    theScreen.onkeypress(paddle1_up, 'Up')
    theScreen.onkeypress(paddle1_down, 'Down')
    theScreen.onkeypress(paddle2_up, 'w')
    theScreen.onkeypress(paddle2_down, 's')
    # for debugging purposes, allow mouse click to reset the ball
    theScreen.onclick(reset_on_click)
    # draw the game based on student's code
    draw_scene(theScreen)
    draw_score(theScore1Text, scoreXOffset)
    draw_score(theScore2Text, -scoreXOffset)
    draw_paddle(thePaddle1, screenWidth // 2 - paddleOffset)
    draw_paddle(thePaddle2, -(screenWidth // 2 - paddleOffset))
    draw_ball(theBall)
    reset_ball(theBall)
    # show the results
    theScreen.update()
    # start game's mainloop
    theScreen.ontimer(game_step, 10)


# Set up the game variables
theScreen = turtle.Screen()
theScreen.title(gameName)
theScreen.setup(screenWidth, screenHeight)
theScreen.tracer(False)

# Scores
theScore1Text = turtle.Turtle()
theScore1Text.score = 0
theScore2Text = turtle.Turtle()
theScore2Text.score = 0

# Game objects
thePaddle1 = turtle.Turtle()
thePaddle2 = turtle.Turtle()
theBall = turtle.Turtle()

setup()

# play the game forever
theScreen.mainloop()
