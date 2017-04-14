import wx
from gui.selectFile import selectFileIns


if __name__ == '__main__':
    app = wx.App()
    selectFileFrame = selectFileIns()
    app.MainLoop()
