### takes a list of pictures and resizes them using pygame
### blocking until list finished

import pygame
import os
from pygame.locals import *

#for test
initialzoom=2
initvpx=100
initvpy=100

WIDTH=800
HEIGHT=600

#when refactoring putting script variables as globals ceased to work
#this is a known workaround
class PygContext(object):
    def __init__(self):
        self.DISPLAYSURF=None        
        self.BASICFONT=None        
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.selection=None
        #here the pic in original size
        self.currentsurf=None
        #here the pic scaled to current zoom level, for display
        self.zoomedsurf=None
        self.currentpicname=None
        self.msg=None        
        self.zoom=None
        #when pointing and zooming with mouse wheel
        #this is the center of the zoom in SOURCE SURFACE COORDINATES
        self.xzoomcenter=None
        self.yzoomcenter=None
        #when moving viewport around , in SOURCE SURFACE COORDINATES
        self.xviewport=None
        self.yviewport=None

def scalesave(ctx):
        print("saving then changing slot")
        tmpBeforeScale=pygame.Surface((ctx.selection.w,ctx.selection.w))
        tmpBeforeScale.blit(ctx.currentsurf,
                            (0,0),
                            ctx.selection
                             )
        pygame.image.save(tmpBeforeScale,"outbefscale.bmp")    
    ##    tmpScaled=pygam
        tmpScaled=pygame.transform.scale(tmpBeforeScale,(600,600))
        pygame.image.save(tmpScaled,"outscaled"+os.path.basename(ctx.currentpicname))
        
    ##    currentpicname=piclist[num]
    ##
    ##    msg = BASICFONT.render(currentpicname, True, RED)
    ##
    ##    ctx.currentsurf=pygame.image.load(currentpicname)
        

## to make cursing forward more readable
def setCurrentPic(ctx,pathandname):
    ctx.currentsurf=pygame.image.load(pathandname)
    ctx.currentpicname=pathandname
    ctx.msg = ctx.BASICFONT.render(ctx.currentpicname, True, ctx.RED)

    ctx.zoom=initialzoom

    #zooming whole picture ? let's be stupid
    #(huge ram usage, needs to be optimized later )
    tgtw=ctx.currentsurf.get_width()*2
    tgth=ctx.currentsurf.get_height()*2
    
    ctx.zoomedsurf=pygame.transform.scale(ctx.currentsurf,(tgtw,tgth))
    
    ctx.xviewport=initvpx
    ctx.yviewport=initvpy
    ##    currentpicname=piclist[num]
    ##
    ##    msg = BASICFONT.render(currentpicname, True, RED)
    ##
    ##    currentsurf=pygame.image.load(currentpicname)
    pass


def createPygameResizeWindow(dnded):

##    num=None
##    currentpicname=None
##    currentsurf=None
##    selection=None
##    msg=None
##    bgRect=None
##    BASICFONT=None
##    DISPLAYSURF=None
    ctx=PygContext()

    pygame.init()
    ctx.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

    ctx.BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

    ctx.selection=pygame.Rect(100,100,200,200);

    piclist=dnded

    num=0
##    currentpicname=piclist[num]
##    print(currentpicname)
##    ctx.msg = ctx.BASICFONT.render(ctx.currentpicname, True, ctx.RED)

    setCurrentPic(ctx,piclist[num])
##    ctx.currentsurf=pygame.image.load(currentpicname)

    bgRect=pygame.Rect(0,0,WIDTH,HEIGHT);

    ##tmpBeforeScale=None


    ##pic change will be centralized here
        


    def displayUI():
        ctx.DISPLAYSURF.fill(ctx.WHITE)
#        ctx.DISPLAYSURF.blit(ctx.currentsurf,bgRect)
        ctx.DISPLAYSURF.blit(ctx.zoomedsurf,bgRect,pygame.Rect(ctx.xviewport*ctx.zoom,ctx.yviewport*ctx.zoom,WIDTH,HEIGHT))

        todisp=pygame.Rect((ctx.selection.x-ctx.xviewport)*ctx.zoom,(ctx.selection.y-ctx.yviewport)*ctx.zoom,ctx.selection.w*ctx.zoom,ctx.selection.h*ctx.zoom)

        pygame.draw.rect(ctx.DISPLAYSURF,ctx.RED,todisp,3)

        ctx.DISPLAYSURF.blit(ctx.msg,(0,0))
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
                ctx.selection.x=pos[0]/ctx.zoom +ctx.xviewport
                ctx.selection.y=pos[1]/ctx.zoom+ctx.yviewport
                
            elif event.type == MOUSEMOTION:
                print("mouse button move")
                pos=pygame.mouse.get_pos()
                tw=pos[0]/ctx.zoom+ctx.xviewport-ctx.selection.x
                th=pos[1]/ctx.zoom+ctx.yviewport-ctx.selection.y

                tgt=None
                if tw>=th :
                    tgt=tw
                else:
                    tgt=th
                ctx.selection.h=tgt
                ctx.selection.w=tgt
            elif event.type == MOUSEBUTTONUP:
                print("mouse button up")
    ##            pos=pygame.mouse.get_pos()
    ##            selection.w=pos[0]-selection.x
    ##            selection.h=pos[1]-selection.y
            elif event.type == KEYDOWN:
                if event.key == ( K_SPACE):
                    scalesave(ctx)
                    num=num+1
                    if num>=len(piclist):
                        running=False
                        pygame.quit()
                        #everything consumed
                    else:
##                        print()
                        setCurrentPic(ctx,piclist[num])


