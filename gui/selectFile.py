#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class SelectFile(wx.Panel):
    def __init__(self, parent):
        self.filePath = ''

        wx.Panel.__init__(self, parent, wx.ID_ANY)

        self.__initBox()
        self.__initSelectButton()
        self.__initLayout()
        self.__initEventHandler()

    def __initBox(self):
        self.box = wx.BoxSizer(wx.HORIZONTAL)

    def __initSelectButton(self):
        self.selectBtn = wx.Button(
            self, wx.ID_OPEN, label=u'选择外差数据文件',
            pos=(100, 100), size=(100, 30))
        self.selectBtn.Center()

    def __initLayout(self):
        self.box.Add(
            self.selectBtn, flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, border=2)
        self.SetSizer(self.box)

    def __initEventHandler(self):
        self.Bind(wx.EVT_BUTTON, self.selectFile, self.selectBtn)

    def selectFile(self, e):
        dig = wx.FileDialog(
            self, message=u"请选择外差数据文件", style=wx.FD_PREVIEW, wildcard="*.csv")
        if dig.ShowModal() == wx.ID_OK:
            self.filePath = dig.GetPath().encode('utf-8')
            self.Close()
        else:
            self.filePath = ''


# def selectFileIns():
#     return SelectFile(None, u'外差多普勒信号处理')


# if __name__ == '__main__':
#     app = wx.App()
#     frame = SelectFile(None, u'外差多普勒信号处理')
#     app.MainLoop()
