import turtle
import random

screen_x = 1366
screen_y = 766
screen = turtle.setup(screen_x, screen_y) #this is the screen.

#making the bag.
bags = turtle.Turtle()
bags.speed(0)
bags.penup()
bag_list = []
bag_list.append(bags)


#making the player.
player = turtle.Turtle() 
player.pu()


#making the sea turtles.
sea_turtle = turtle.Turtle()
sea_turtle.speed(0)
sea_turtle.penup()
sea_turtle.shape("turtle")
sea_turtle_pos = []
sea_turtle_pos.append(sea_turtle.pos())
print(sea_turtle_pos)


max_x = 683
min_x = -683 #min and max edge of the screen.
rand = random.randint(min_x,max_x) #random number for bags
rand2 = random.randint(min_x,max_x) #random number for sea turtles
bags.goto(rand, 200) #we set the bags to go to the random number
sea_turtle.goto(rand , -300) #we set the turtles to go to the random number

y_pos = bags.ycor() #gets the y position
new_y = y_pos - 1 #set it equals to y_pos - 1 to make the droping affect 
while y_pos > -394: #as long as the bags dont touch the border make them fall 
    bags.speed(1)
    y_pos = y_pos - 20
    bags.goto(rand , y_pos)
    print(bags.pos())
    print(sea_turtle_pos)
    if bags.pos() == sea_turtle.pos():   #make the turtle disapear if the bag
        sea_turtle.ht()                                   #touches it


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

    if bags.pos() == player.pos():
        bags.ht()

        



