### takes a list of pictures and resizes them using pygame
### blocking until list finished

##WIP zoom not centered on mouse

import pygame
import os
from pygame.locals import *

#for test
initialzoom=1
initvpx=0
initvpy=0



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
##        self.xzoomcenter=None
##        self.yzoomcenter=None
        #when moving viewport around , in SOURCE SURFACE COORDINATES
        self.xviewport=None
        self.yviewport=None
        #to move the square while you hold
        self.leftpressed=False

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
def setCurrentPic(ctx,pathandname,newzoom,xzoomcenter,yzoomcenter):
    ctx.currentsurf=pygame.image.load(pathandname)
    ctx.currentpicname=pathandname
    ctx.msg = ctx.BASICFONT.render(ctx.currentpicname, True, ctx.RED)

    #initialzoom


    if xzoomcenter ==None or yzoomcenter==None:
        ctx.xviewport=initvpx
        ctx.yviewport=initvpy
    else:
##        ctx.xviewport=initvpx
##        ctx.yviewport=initvpy
##        #todo not left corner but middle
        ctx.xviewport=xzoomcenter/ctx.zoom+ctx.xviewport-WIDTH/(2*ctx.zoom)
        ctx.yviewport=yzoomcenter/ctx.zoom+ctx.yviewport-HEIGHT/(2*ctx.zoom)
        print("calculated from click xvp yvp "+str(ctx.xviewport)+" "+str(ctx.yviewport))
        

    if ctx.xviewport<0  :
        ctx.xviewport=0

    if ctx.yviewport<0  :
        ctx.yviewport=0
        
    ctx.zoom=newzoom

    print("zoom "+str(newzoom))
    print("xvp yvp "+str(ctx.xviewport)+" "+str(ctx.yviewport))
    
    #zooming whole picture ? let's be stupid
    #(huge ram usage, needs to be optimized later )
    tgtw=int(ctx.currentsurf.get_width()*newzoom)
    tgth=int(ctx.currentsurf.get_height()*newzoom)
    
    ctx.zoomedsurf=pygame.transform.scale(ctx.currentsurf,(tgtw,tgth))

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

##    ctx.selection=None
##    ctx.selection=pygame.Rect(100,100,200,200);

    piclist=dnded

    num=0
##    currentpicname=piclist[num]
##    print(currentpicname)
##    ctx.msg = ctx.BASICFONT.render(ctx.currentpicname, True, ctx.RED)

    setCurrentPic(ctx,piclist[num],initialzoom,None,None)
##    ctx.currentsurf=pygame.image.load(currentpicname)

    bgRect=pygame.Rect(0,0,WIDTH,HEIGHT);

    ##tmpBeforeScale=None


    ##pic change will be centralized here
        


    def displayUI():
        ctx.DISPLAYSURF.fill(ctx.WHITE)
#        ctx.DISPLAYSURF.blit(ctx.currentsurf,bgRect)
        ctx.DISPLAYSURF.blit(ctx.zoomedsurf,bgRect,pygame.Rect(ctx.xviewport*ctx.zoom,ctx.yviewport*ctx.zoom,WIDTH,HEIGHT))

        if ctx.selection!=None:
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
                print(event)
                print(event.button)
                if event.button == 1 : # leftclick
                    print("left button down")
                    ctx.leftpressed=True
                    if ctx.selection==None:
                        ctx.selection=pygame.Rect(0,0,0,0)
                    pos=pygame.mouse.get_pos()
                    ctx.selection.x=pos[0]/ctx.zoom +ctx.xviewport
                    ctx.selection.y=pos[1]/ctx.zoom+ctx.yviewport
                elif event.button==4 :
                    print("mousewheel up")
                    zoom=ctx.zoom+0.5
                    xroll=pygame.mouse.get_pos()[0]
                    yroll=pygame.mouse.get_pos()[1]
                    print("xr yr "+str(xroll)+" "+str(yroll))
                    setCurrentPic(ctx,piclist[num],zoom,xroll,yroll)

                elif event.button==5  :
                    print("mousewheel down")
                    zoom=ctx.zoom-0.5
                    if zoom<0.5 :
                        zoom=0.5
                    setCurrentPic(ctx,piclist[num],zoom,pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    
            elif event.type == MOUSEMOTION:
##                print("mouse button move")
                if ctx.leftpressed :
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
                if event.button==1:
                    print("left button up")
                    ctx.leftpressed=False
                
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
                        setCurrentPic(ctx,piclist[num],initialzoom,None,None)


