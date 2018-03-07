# 15 min
# +10 min
# +20 min

#poc for the great M
import pygame
from pygame.locals import *


WIDTH=640
HEIGHT=480

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)

selection=pygame.Rect(100,100,200,200);


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
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(currentsurf,bgRect)
    pygame.draw.rect(DISPLAYSURF,RED,selection,3)
    pygame.display.update()

running=True

while running:

    #UI display
    displayUI()
    
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            pygame.quit()
            running=False
        elif event.type == MOUSEBUTTONDOWN:
            print("mouse button down")
            pos=pygame.mouse.get_pos()
            selection.x=pos[0]
            selection.y=pos[1]
            
        elif event.type == MOUSEMOTION:
            print("mouse button move")
    ##        self.quit=True
            #terminate()
    # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
    #            elif event.type == JOYBUTTONDOWN:
            #print("Joystick button pressed.")
    #           elif event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
        elif event.type == MOUSEBUTTONUP:
            print("mouse button up")
            pos=pygame.mouse.get_pos()
            selection.w=pos[0]-selection.x
            selection.h=pos[1]-selection.y
        elif event.type == KEYDOWN:
            if event.key == ( K_f):
                goToNextPic()
#                send_to_arduino(ser,'f')
##            elif event.key == (K_j):
##                send_to_arduino(ser,'j')



