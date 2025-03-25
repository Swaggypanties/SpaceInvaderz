import turtle
import math
import random
import platform


if platform.system() == "Windows":
    try:
        import winsound
    except:
        print("Winsound module not available")    

# This will set up the whole screen
mainscreen =  turtle.Screen()
mainscreen.bgcolor("black")
mainscreen.title("Space Invaderz")
mainscreen.bgpic("invadersbackground.gif")
mainscreen.tracer(0)

# Registering the shapes
mainscreen.register_shape("invader.gif")
mainscreen.register_shape("player.gif")


# Draws the border
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

# Setting the score
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


# Creates the player
player = turtle.Turtle()
player.color("pink")
player.shape("player.gif")
player.penup()
player.speed(0)

# player positioning
player.setposition(0,-250)
player.setheading(90) # Sets the player upright but 180 sets it looking to the left, 0(default) sets it to the right and 270 sets it looking down

# player movement
player.speed = 5

# Create an empty list of enemies
invaders = []

# The amount of invaders
number_of_invaders = 30

# Add enemies to the list
for i in range(number_of_invaders):
    invaders.append(turtle.Turtle())

invader_start_x = -225
invader_start_y = 250
invader_number = 0

# creating the invader
for invader in invaders:
    invader.color("green")
    invader.shape("invader.gif")
    invader.penup()
    invader.speed(0)
    x = invader_start_x + (50 * invader_number)
    y = invader_start_y
    invader.setposition(x,y)
    # Update the enemy number
    invader_number += 1
    if invader_number == 10:
        invader_start_y -=50
        invader_number = 0
    
invaderspeed = 0.1

#Creating the gun
bullet = turtle.Turtle()
bullet.color("red")
bullet.shape("arrow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 10

# Define the bullet state
# ready = ready to fire
# fire = bullet is firing

bulletstate = "ready"




# Move the player left. takes the player(x) and it subtract the speed -= to the new location
def move_left():
    player.speed = -1

# Move the player right
def move_right():
    player.speed = 1
    
def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280: # Lowest value that we will accept for x is -280 (boundary checking)
        x = -280
    if x > 280:
        x = 280 # Highest value that we will accept for x is 280 (boundary checking)    
    player.setx(x)
    
        

# Function for shooting the bullet

def fire_bullet():
    # Declare bulletstate as global if it needs changed (if a variable is defined inside of a function its a local variable but if its outside a function like bulletstate or playerspeed its a global variable)
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("C:/Users/Jere/Desktop/Python Project/SpaceInvaderz/lazer.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
    # Moving the bullet above me
        x =  player.xcor()
        y = player.ycor() +10
        bullet.setposition(x, y)
        bullet.showturtle()
        
        # The collision for the bullet
def isCollision(t1, t2):
     distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
     if distance <15:
         return True
     else:
         return False
     
def play_sound(sound_file, time = 0):
    if platform.system() == "Windows":
        winsound.PlaySound(sound_file, winsound.SND_ASYNC)      
    # Repeat sound
    if time > 0:
        turtle.ontimer(lambda: play_sound(sound_file, time), t=int(time*1000))       
     
# Keybindings

mainscreen.listen()
mainscreen.onkey(move_left, "Left")
mainscreen.onkey(move_right, "Right")
mainscreen.onkey(fire_bullet, "space")

# Background music
play_sound("C:/Users/Jere/Desktop/Python Project/SpaceInvaderz/gamemusic.wav", 90)


# Main game loop
while True:
    mainscreen.update()
    move_player()
    
    for invader in invaders:
        # Enemy movement
        x = invader.xcor()
        x += invaderspeed
        invader.setx(x)
    
    # Enemy movement, The ycor makes it go one coordinate down one
        if invader.xcor() > 280:
            # Nested loop so that all enemies go down at the same time
            for inv in invaders:
                y = inv.ycor() 
                y -= 40
                inv.sety(y)
            # Change enemy direction
            invaderspeed *= -1
        
        if invader.xcor() < -280:
            # Nested loop so that all enemies go down at the same time
            for inv in invaders:
                y = inv.ycor()
                y -= 40
                inv.sety(y)
            # Change enemy direction
            invaderspeed *= -1
            
    # Checking collision for the bullet and the enemy
        if isCollision(bullet, invader):
            play_sound("C:/Users/Jere/Desktop/Python Project/SpaceInvaderz/explosion.wav")
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            invader.setposition(0,10000)
            # Scoring
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        
        # If the enemy hits the player the game is over
        if isCollision(player, invader):
            play_sound("explosion.wav")
            player.hideturtle()
            invader.hideturtle()
            print("Game Over")
            break        

# Bullet movement
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
# Border check for the bullet
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"
                        
                
    mainscreen.update()
    



