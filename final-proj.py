from pygame import mixer # Load the required library
import turtle

mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()

def up():
    x,y = turtle.pos()
    turtle.goto(x,y+10)

turtle.onkeypress(up, "Up")
turtle.listen()


