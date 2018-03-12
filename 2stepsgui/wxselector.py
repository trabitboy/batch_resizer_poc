### creates a drag and drop window to select image files
## blocking until you close it

import wx

########################################################################
class MyFileDropTarget(wx.FileDropTarget):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, window,dnded):
        """Constructor"""
        wx.FileDropTarget.__init__(self)
        self.window = window
        self.dnded=dnded
 
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
            self.dnded.append(filepath)
        print(self.dnded)
 
########################################################################
class DnDPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent,dnded):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        file_drop_target = MyFileDropTarget(self,dnded)
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
    def __init__(self,dnded):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="DnD Tutorial")
        panel = DnDPanel(self,dnded)
        self.Show()
 
#----------------------------------------------------------------------

def createDnd(dnded):
    app = wx.App(False)
    frame = DnDFrame(dnded)
    app.MainLoop()
