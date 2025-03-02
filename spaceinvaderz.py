import turtle
import  os

#This will set up the whole screen
mainscreen =  turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaderz")

#Draws the border
border_pen = turtle.Turtle()
border_pen.speed(0) #0 is the fastest
border_pen.color("yellow")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Creates the player
player = turtle.Turtle()
player.color("pink")
player.shape("triangle")
player.penup()
player.speed(0)

#player positioning
player.setposition(0,-250)
player.setheading(90) #sets the player upright but 180 sets it looking to the left, 0(default) sets it to the right and 270 sets it looking down

#player movement
playerspeed = 15

#creating the invader
invader = turtle.Turtle()
invader.color("green")
invader.shape("circle")
invader.penup()
invader.speed(0)
invader.setposition(-200,250)

invaderspeed = 2



#Move the player left. takes the player(x) and it subtract the speed -= to the new location
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x  <  -280: #Lowest value that we will accept for x is -280 (boundary checking)
        x = -280
    player.setx(x)
    

#Move the player right

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280 #Highest value that we will accept for x is 280 (boundary checking)
    player.setx(x)

#Keybindings

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


#Main game loop
while True:
        #Enemy movement
    x = invader.xcor()
    x += invaderspeed
    invader.setx(x)
    
    #Enemy movement around, The ycor makes it go one coordinate down one
    if invader.xcor() > 280:
        y = invader.ycor() 
        y -= 40
        invaderspeed *= -1
        invader.sety(y)
        
    if invader.xcor() < -280:
        y = invader.ycor()
        y -= 40
        invaderspeed *= -1
        invader.sety(y)
        
    mainscreen.update()
    

