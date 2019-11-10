""" 
Pong

source: https://www.youtube.com/watch?v=XGf2GcyHPhc

by FA

"""

#Easier to understand than PyGame, at first.

import turtle 

import os 


window = turtle.Screen()

window.title("Pong")

window.bgcolor("green")

window.setup(width=800, height=600)

window.tracer(0) #manually update the screen


#Tracking scores

scoreA, scoreB = 0, 0


#Paddle A

paddleA  = turtle.Turtle()

paddleA.speed(0) #speed of animation maximum

paddleA.shape(name="square")

paddleA.color("red")

paddleA.shapesize(stretch_wid=5, stretch_len=1, outline=True) #default 20 px

paddleA.penup()

paddleA.goto(x=-350,y=0)


#Paddle B

paddleB  = turtle.Turtle()

paddleB.speed(0) #speed of animation maximum

paddleB.shape(name="square")

paddleB.color("blue")

paddleB.shapesize(stretch_wid=5, stretch_len=1, outline=True) #default 20 px

paddleB.penup()

paddleB.goto(x=350,y=0)



#Ball

ball  = turtle.Turtle()

ball.speed(0) #speed of animation maximum

ball.shape(name="circle")

ball.color("white")

ball.penup()

ball.goto(x=0,y=0)

ball.dx, ball.dy = 2,2 #ball moves up and diagonally



#Pen A

penA = turtle.Turtle()

penA.speed(speed=0)

penA.color("white")

penA.penup() 

penA.hideturtle() #dont show the pen

penA.goto(x=-300, y=260)

penA.write(arg="Player A: 0", align='center', font=("Comic Sans", 35, "bold"))



#Pen B

penB = turtle.Turtle()

penB.speed(speed=0)

penB.color("white")

penB.penup() 

penB.hideturtle() #dont show the pen

penB.goto(x=300, y=260)

penB.write(arg="Player B: 0", align='center', font=("Comic Sans", 35, "bold"))

#winner message
winner = turtle.Turtle()

winner.speed(speed=0)

winner.color("white")

winner.penup()

winner.hideturtle()

winner.goto(x=0,y=0)


#Line

line = turtle.Turtle()

line.shape(name="square")

line.speed(0)

line.color("white")

line.penup()

line.goto(0,0)

line.shapesize(stretch_wid=30, stretch_len=1, outline=True) #default 20 px

#Define the user's functions

def paddleA_up():
    
    y = paddleA.ycor()
    
    y += 20 #20 pixels to one y-movement
    
    ymax = 300-30
    
    if y <= ymax:
        
        paddleA.sety(y)

    
def paddleA_down():
    
    y = paddleA.ycor()
    
    y -= 20 #20 pixels to one y-movement
    
    ymin = -300+30
    
    if y >= ymin:
        
        paddleA.sety(y)

def paddleB_up():
    
    y = paddleB.ycor()
    
    y += 20 #20 pixels to one y-movement
    
    ymax = 300-30
    
    if y <= ymax:
        
        paddleB.sety(y)

def paddleB_down():
    
    y = paddleB.ycor()
    
    y -= 20 #20 pixels to one y-movement
    
    ymin = -300+30
    
    if y >= ymin:
        
        paddleB.sety(y)

#Keyboard binding
    
window.listen()

window.onkeypress(paddleA_up, "w")

window.onkeypress(paddleA_down, "s")

window.onkeypress(paddleB_up, "Up")

window.onkeypress(paddleB_down, "Down")



#Main loop of the game

game_on = True

while game_on:
    
    window.update()
    
    #move the ball
    
    ball.setx(ball.xcor() + ball.dx) #ball's origin is 0,0. We move it by 2
    
    ball.sety(ball.ycor() + ball.dy)
    
    #border checking
    
    if ball.ycor() > 290:
        
        ball.sety(290)
        
        ball.dy *= -1 #reverse direction
        
        os.system("afplay sound34.mp3&")

    if ball.ycor() < -290:
        
        ball.sety(-290)
        
        ball.dy *= -1 #reverse direction
        
        os.system("afplay sound34.mp3&")
        
    if ball.xcor() > 390:
        
        ball.setx(0)
        
        ball.dx *= -1 #reverse direction
        
        scoreA += 1
    
        penA.clear()
        
        penB.clear()
        
        penA.write(arg="Player A: {}".format(scoreA), align='center', font=("Comic Sans", 35, "bold"))
        
        penB.write(arg="Player B: {}".format(scoreB), align='center', font=("Comic Sans", 35, "bold"))
        
    if ball.xcor() < -390:
        
        ball.setx(0)
        
        ball.dx *= -1 #reverse direction
        
        scoreB += 1
        
        penA.clear()
        
        penB.clear()
        
        penA.write(arg="Player A: {}".format(scoreA), align='center', font=("Comic Sans", 35, "bold"))
        
        penB.write(arg="Player B: {}".format(scoreB), align='center', font=("Comic Sans", 35, "bold"))
        
    # Paddle and ball collisions
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50 ):
        
        ball.setx(340)
        
        ball.dx *= -1
        
        os.system("afplay sound69.wav&")
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50 ):
        
        ball.setx(-340)
        
        ball.dx *= -1
        
        os.system("afplay sound69.wav&")


    if scoreA == 2:
    
        winner.write(arg="PLAYER A WINS!", align='center',font=("Comic Sans", 100, "bold") )
        
        turtle.bye()
        
        
    elif scoreB == 2:
        
        winner.write(arg="PLAYER B WINS!", align='center',font=("Comic Sans", 100, "bold") )
        
        turtle.bye()
        
        