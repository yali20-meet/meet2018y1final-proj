import turtle
import random

screen_x = 1366
screen_y = 766
screen = turtle.setup(screen_x, screen_y) #this is the screen.

screen=turtle.Screen()
screen.bgpic("sea.gif")
screen.update()

#making the bag.
bags = turtle.Turtle()
bags.speed(0)
bags.penup()
bag_list = []
bag_list.append(bags)
turtle.register_shape("bag.gif")
bags.shape("bag.gif")


#making the player.
player = turtle.Turtle() 
player.pu()
turtle.register_shape("net.gif")
player.shape("net.gif")

#making the sea turtles.
sea_turtle = turtle.Turtle()
sea_turtle.speed(0)
sea_turtle.penup()
sea_turtle.shape("turtle")
sea_turtle_pos = []
sea_turtle_pos.append(sea_turtle.pos())
print(sea_turtle_pos)
turtle.register_shape("sea-turtle.gif")
sea_turtle.shape("sea-turtle.gif")

#getting the x and y of the turtles
x_p = player.xcor()
y_p = player.ycor()
x_b = bags.xcor()
y_b = bags.ycor()
x_t = sea_turtle.xcor()
y_t = sea_turtle.ycor()
 

max_x = 683
min_x = -683 #min and max edge of the screen.
rand = random.randint(min_x,max_x) #random number for bags
rand2 = random.randint(min_x,max_x) #random number for sea turtles
bags.goto(rand, 300) #we set the bags to go to the random number
sea_turtle.goto(rand , -300) #we set the turtles to go to the random number

y_pos = bags.ycor() #gets the y position
new_y = y_pos - 1 #set it equals to y_pos - 1 to make the droping affect 
while y_pos > -394: #as long as the bags dont touch the border make them fall 
    bags.speed(1)
    y_pos = y_pos - 20
    bags.goto(rand , y_pos)
    #print(bags.pos())
    #print(sea_turtle_pos)
    if (abs(x_b - x_t) < 20) and (abs(y_b - y_t)< 20):   #make the turtle disapear if the bag
        sea_turtle.ht()                                   #touches it
        
        print(bags.pos())
        print(sea_turtle.pos())
        print(abs(y_b - y_t))
        
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


    turtle.listen()
    turtle.onkey(move_left, 'Left')   #make the turtle move left.
    turtle.onkey(move_right, 'Right') #make the turtle move right.


    if abs(x_p - x_b) < 20 and abs(y_p - y_b) < 20: #makes the bag disapear if they touch the net
        bags.ht()

bags.ht()


        



