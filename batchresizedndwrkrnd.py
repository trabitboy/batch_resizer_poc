# 15 min
# +10 min
# +20 min
# + 40 min

#TODO
# scale down picture larger than viewport,
# determine zoom level
# select based on zoom level
# navigate to next slot

#poc for the great M
import pygame
from pygame.locals import *

import wx
import threading
 
########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, window):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window
 
    #----------------------------------------------------------------------
    def OnDropFiles(self, x, y, filenames):
        """
        When files are dropped, write where they were dropped and then
        the file paths themselves
        """
        self.window.SetInsertionPointEnd()
        self.window.updateText("\n%d file(s) dropped at %d,%d:\n" %
                              (len(filenames), x, y))
        for filepath in filenames:
            self.window.updateText(filepath + '\n')    
 
########################################################################
class DnDPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        file_drop_target = MyFileDropTarget(self)
        lbl = wx.StaticText(self, label="Drag some files here:")
        self.fileTextCtrl = wx.TextCtrl(self,
                                        style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
        self.fileTextCtrl.SetDropTarget(file_drop_target)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(lbl, 0, wx.ALL, 5)
        sizer.Add(self.fileTextCtrl, 1, wx.EXPAND|wx.ALL, 5)
        self.SetSizer(sizer)
 
    #----------------------------------------------------------------------
    def SetInsertionPointEnd(self):
        """
        Put insertion point at end of text control to prevent overwriting
        """
        self.fileTextCtrl.SetInsertionPointEnd()
 
    #----------------------------------------------------------------------
    def updateText(self, text):
        """
        Write text to the text control
        """
        self.fileTextCtrl.WriteText(text)
 
########################################################################
class DnDFrame(wx.Frame):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="DnD Tutorial")
        panel = DnDPanel(self)
        self.Show()
 
#----------------------------------------------------------------------

def createDnd():
    app = wx.App(False)
    frame = DnDFrame()
    app.MainLoop()

createDnd()

WIDTH=800
HEIGHT=600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)

BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

selection=pygame.Rect(100,100,200,200);



#poc, pic list here
piclist=["test.bmp","test2.bmp","test3.bmp"]

num=0
currentpicname=piclist[num]
print(currentpicname)

msg = BASICFONT.render(currentpicname, True, RED)

currentsurf=pygame.image.load(currentpicname)

bgRect=pygame.Rect(0,0,WIDTH,HEIGHT);

##tmpBeforeScale=None

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
    
    #TODO resize save
##    pygame.transform.scale()
    
    #TODO move slot
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



