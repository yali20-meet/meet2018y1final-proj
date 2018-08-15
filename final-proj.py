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
bags1 = bags.clone()
bags2 = bags.clone()
bags3 = bags.clone()
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
 
def rand():
    max_x = 683
    min_x = -683 #min and max edge of the screen.
    return random.randint(min_x,max_x) #random number for bags


bags.goto(rand() , 300)
sea_turtle.goto(rand(),-300)
bags1 = bags.clone()
bags2 = bags.clone()
bags3 = bags.clone()
sea1 = sea_turtle.clone()
sea2 = sea_turtle.clone()
sea1.goto(rand() , -300)
sea2.goto(rand() , -300)
bags1.goto(rand() , 300)
bags2.goto(rand() , 300)
bags.goto(rand() , 300)



y_pos = bags.ycor() #gets the y position

new_y = y_pos - 1 #set it equals to y_pos - 1 to make the droping affect
while y_pos > -394: #as long as the bags dont touch the border make them fall
    bags.speed(1)
    y_pos = y_pos - 20
    bags.goto(bags.xcor() , y_pos)

    #getting the x and y of the turtles
    x_p,y_p = player.pos()
    x_b,y_b = bags.pos()
    x_t,y_t = sea_turtle.pos()

    print((x_b,y_b))
    print(x_t,y_t)
    if (abs(x_b - x_t) < 50) and (abs(y_b - y_t) < 50):   #make the turtle disapear if the bag
        sea_turtle.ht()                                   #touches it
        
        #print(bags.pos())
        #print(sea_turtle.pos())
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


    if abs(x_p - x_b) < 50 and abs(y_p - y_b) < 50: #makes the bag disapear if they touch the net
        bags.ht()

bags.ht()
'''    
x_p = player.xcor()
y_p = player.ycor()
x_b = bags.xcor()
y_b = bags.ycor()
x_t = sea_turtle.xcor()
y_t = sea_turtle.ycor()
'''


        



