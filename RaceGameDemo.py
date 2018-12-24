#!/usr/bin/python3
import pgzrun
from random import randint  		# import the randint class from random module

WIDTH = 700         # width of the window
HEIGHT = 800        # height of the window 
car = Actor("racecar")
car.pos = 350, 560
trackLeft = [] 		# list to store left barries 
trackRight = [] 	# list to store right barries 
trackCount = 0		# count the number of barries 
trackPosition = 350
trackWidth = 150	# width between left and right barries
trackDirection = False
SPEED = 4				# sets the speed of the game 


def draw():             # pygame zero draw function
    screen.fill((128, 128, 128))    # fill the screen with
    car.draw()
    b = 0
    while b < len(trackLeft):
    	trackLeft[b].draw()
    	trackRight[b].draw()
    	b +=1 

def update(): 
    if keyboard.left : car.x -=2
    if keyboard.right : car.x +=2
    if keyboard.up : car.y -=2
    if keyboard.down : car.y +=2       
    updateTrack()


def makeTrack():                    # function to make one barrie at the left and right
    global trackCount, trackLeft, trackRight, trackPosition, trackWidth
    trackLeft.append(Actor("bare", pos = (trackPosition-trackWidth, 0)))
    trackRight.append(Actor("bare", pos = (trackPosition + trackWidth, 0)))
    trackCount +=1


def updateTrack():
    global trackCount, trackPosition, trackDirection, trackWidth,SPEED
    b = 0
    while b < len(trackLeft):      
        trackLeft[b].y += SPEED
        trackRight[b].y += SPEED
        b += 1
    if trackLeft[len(trackLeft)-1].y > 32:
        if trackDirection == False: trackPosition += 16
        if trackDirection == True:  trackPosition -= 16
        if randint(0,4) == 1:   trackDirection = not trackDirection
        if trackPosition > 700 - trackWidth:
            trackDirection = True
        if trackPosition < trackWidth:
            trackDirection = False
        makeTrack()
makeTrack() 
pgzrun.go()
