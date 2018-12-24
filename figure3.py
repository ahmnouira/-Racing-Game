#!/usr/bin/python3
import pgzrun
WIDTH = 700         # width of the window
HEIGHT = 800        # height of the window 
car = Actor("racecar")
car.pos = 350, 560
def draw():             # pygame zero draw function
    screen.fill((128, 128, 128))    # fill the screen with
    car.draw() 

def update(): 
	if keyboard.left : car.x -=2
	if keyboard.right : car.x +=2
	if keyboard.up : car.y -=2
	if keyboard.down : car.y +=2       
 
pgzrun.go()
