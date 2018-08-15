import turtle
import random
from pygame import mixer

screen_x = 1366
screen_y = 766
screen = turtle.setup(screen_x, screen_y) #this is the screen.

screen=turtle.Screen()
screen.bgpic("sea.gif")
screen.update()

turtle.tracer(1,1)

'''
mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
'''
score = 0


turtle.clear()
turtle.penup()
turtle.goto(600,300)
turtle.write(score, font=("Arial", 20))

#making the bag.
bags = turtle.Turtle()
bags.penup()

turtle.register_shape("bag.gif")
bags.shape("bag.gif")

#making the player.
player = turtle.Turtle() 
player.pu()
turtle.register_shape("net.gif")
player.shape("net.gif")

#making the sea turtles.
sea_turtle = turtle.Turtle()
sea_turtle.penup()
sea_turtle.shape("turtle")
sea_turtle_pos = []
sea_turtle_pos.append(sea_turtle.pos())
#print(sea_turtle_pos)
turtle.register_shape("sea-turtle.gif")
sea_turtle.shape("sea-turtle.gif")
 
def rand():
    max_x = 683
    min_x = -683 #min and max edge of the screen.
    return random.randint(min_x,max_x) #random number for bags



bags1 = bags.clone()
bags2 = bags.clone()
bags3 = bags.clone()
sea_turtle.goto(rand(),-300)
sea1 = sea_turtle.clone()
sea2 = sea_turtle.clone()
sea3 = sea_turtle.clone()
sea4 = sea_turtle.clone()
sea5 = sea_turtle.clone()
sea6 = sea_turtle.clone()
sea7 = sea_turtle.clone()
sea8 = sea_turtle.clone()
sea_list = [ sea_turtle, sea1 , sea2, sea3 ,sea4 , sea5 ,sea6, sea7, sea8]
turtle_num = 9

sea1.goto(rand() , -300)
sea2.goto(rand() , -300)
sea3.goto(rand() , -300)
sea4.goto(rand() , -300)
sea5.goto(rand() , -300)
sea6.goto(rand() , -300)
sea7.goto(rand() , -300)
sea8.goto(rand() , -300)
bags1.goto(rand(), -380)
bags2.goto(rand(), -380)
bags3.goto(rand(), -380)
bags.goto(rand() , -380)

bag_list = [bags, bags1, bags2, bags3]
MAX_Y = 380
y_pos = bags.ycor() #gets the y position

#new_y = y_pos - 1 #set it equals to y_pos - 1 to make the droping affect
def game():
    global score,turtle_num
    
    for i in bag_list:
        y_pos = i.pos()[1]
        if y_pos <= -MAX_Y:
            i.ht()
            i.goto(rand() , 394)
        else:
            x,y = i.pos()
            i.goto(x , y -  20)
            i.st()

    #getting the x and y of the turtles
        x_p,y_p = player.pos()
        x_b,y_b = i.pos()
        if abs(x_p - x_b) < 50 and abs(y_p - y_b) < 50: #makes the bag disapear if they touch the net
            i.ht()
            i.goto(x_b , -MAX_Y)
            score+=1
        for c in sea_list:
            x_t,y_t = c.pos()

            if (abs(x_b - x_t) < 50) and (abs(y_b - y_t) < 50):   #make the turtle disapear if the bag
                c.ht()                                            #touches it
                turtle_num -= 1
                sea_list.remove(c)
    print(turtle_num)
    if turtle_num == 0:
        quit()


    turtle.clear()
    turtle.penup()
    turtle.goto(600,300)
    turtle.write(score, font=("Arial", 20))

    turtle.ontimer(game, 10)    
        #print(bags.pos())
        #print(sea_turtle.pos())
        #print(abs(y_b - y_t))
    
def move_left(): #move left function.
    x = player.xcor()
    x = x - 20
    if x < -683: #the player can't go out of the screen.
        x = -683
    player.setx(x) #set the new x

def move_right(): #move right function.   
    x = player.xcor()
    x = x + 20
    if x > 683: #the player can't go out of the screen.
        x = 683
    player.setx(x) #set the new x
def move_up (): # move up function
    y = player.ycor()
    y = y + 20
    if y > 0: # the player can't go up more than 0.
        y = 0
    player.sety(y) #set the new y.
def move_down (): #move up function
    y = player.ycor()
    y = y - 20
    if y <  -200: #the player can't be less then -200
        y = -200
    player.sety(y)

turtle.listen()
turtle.onkey(move_left, 'Left')   #make the turtle move left.
turtle.onkey(move_right, 'Right') #make the turtle move right.
turtle.onkey(move_up, 'Up')       #make the turtle nove up.
turtle.onkey(move_down, 'Down')   #make the turtle go down.


turtle.ht()
game()

'''    
x_p = player.xcor()
y_p = player.ycor()
x_b = bags.xcor()
y_b = bags.ycor()
x_t = sea_turtle.xcor()
y_t = sea_turtle.ycor()
'''


        



