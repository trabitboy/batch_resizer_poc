### takes a list of pictures and resizes them using pygame
### blocking until list finished

import pygame
from pygame.locals import *

WIDTH=800
HEIGHT=600





def createPygameResizeWindow(dnded):

##    num=None
##    currentpicname=None
##    currentsurf=None
##    selection=None
##    msg=None
##    bgRect=None
##    BASICFONT=None
##    DISPLAYSURF=None
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

    BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    selection=pygame.Rect(100,100,200,200);

    piclist=dnded

    num=0
    currentpicname=piclist[num]
    print(currentpicname)

    msg = BASICFONT.render(currentpicname, True, RED)

    currentsurf=pygame.image.load(currentpicname)

    bgRect=pygame.Rect(0,0,WIDTH,HEIGHT);

    ##tmpBeforeScale=None


    ##pic change will be centralized here
    ## to make cursing forward more readable
    def setCurrentPic():
        ##    currentpicname=piclist[num]
        ##
        ##    msg = BASICFONT.render(currentpicname, True, RED)
        ##
        ##    currentsurf=pygame.image.load(currentpicname)
        pass
        
    def goToNextPic():
        print("saving then changing slot")
        tmpBeforeScale=pygame.Surface((selection.w,selection.w))
        tmpBeforeScale.blit(currentsurf,
                            (0,0),
                            selection
                             )
        pygame.image.save(tmpBeforeScale,"outbefscale.bmp")    
    ##    tmpScaled=pygam
        tmpScaled=pygame.transform.scale(tmpBeforeScale,(600,600))
        pygame.image.save(tmpScaled,"outscaled.bmp")
        
    ##    currentpicname=piclist[num]
    ##
    ##    msg = BASICFONT.render(currentpicname, True, RED)
    ##
    ##    currentsurf=pygame.image.load(currentpicname)


    def displayUI():
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(currentsurf,bgRect)
        pygame.draw.rect(DISPLAYSURF,RED,selection,3)
        DISPLAYSURF.blit(msg,(0,0))
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
                pos=pygame.mouse.get_pos()
                tw=pos[0]-selection.x
                th=pos[1]-selection.y

                tgt=None
                if tw>=th :
                    tgt=tw
                else:
                    tgt=th
                selection.h=tgt
                selection.w=tgt
            elif event.type == MOUSEBUTTONUP:
                print("mouse button up")
    ##            pos=pygame.mouse.get_pos()
    ##            selection.w=pos[0]-selection.x
    ##            selection.h=pos[1]-selection.y
            elif event.type == KEYDOWN:
                if event.key == ( K_SPACE):
                    goToNextPic()



