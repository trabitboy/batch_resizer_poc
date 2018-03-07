# +10 min

#poc for the great M
import pygame
from pygame.locals import *


WIDTH=640
HEIGHT=480

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)


#poc, pic list here
piclist=["test.bmp","test2.bmp","test3.bmp"]

currentpicname=piclist[1]

currentsurf=pygame.image.load(currentpicname)

bgRect=pygame.Rect(0,0,640,480);


def goToNextPic():
    print("saving then changing slot")
    #TODO resize save

    #TODO move slot

def displayUI():
    ctx.DISPLAYSURF.fill(WHITE)
    ctx.DISPLAYSURF.blit(currentsurf,bgRect)

while True:

    #UI display
    displayUI()
    
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN:
            print("mouse button down")
    ##        self.quit=True
            #terminate()
    # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
    #            elif event.type == JOYBUTTONDOWN:
            #print("Joystick button pressed.")
    #           elif event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
        elif event.type == MOUSEBUTTONUP:
            print("mouse button up")
        
        elif event.type == KEYDOWN:
            if event.key == ( K_f):
                goToNextPic()
#                send_to_arduino(ser,'f')
##            elif event.key == (K_j):
##                send_to_arduino(ser,'j')



