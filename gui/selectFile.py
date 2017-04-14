#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class SelectFile(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        self.__initPanel()
        self.__initBox()
        self.__initSelectButton()
        self.__initLayout()
        self.__initEventHandler()

        self.Show(True)

    def __initPanel(self):
        self.panel = wx.Panel(self)
        self.panel.Center()
        self.SetSize((500, 250))

    def __initBox(self):
        self.box = wx.BoxSizer()

    def __initSelectButton(self):
        self.selectBtn = wx.Button(
            self.panel, wx.ID_OPEN, label=u'选择外差数据文件', size=(100, 30))
        self.selectBtn.Center()

    def __initLayout(self):
        self.box.Add(
            self.selectBtn, proportion=1, flag=wx.SHAPED,
            border=2)
        self.panel.SetSizer(self.box)

    def __initEventHandler(self):
        self.Bind(wx.EVT_BUTTON, self.selectFile, self.selectBtn)

    def selectFile(self, e):
        dig = wx.FileDialog(
            self, message="open file", style=wx.FD_PREVIEW, wildcard="*.csv")
        if dig.ShowModal() == wx.ID_OK:
            return dig.GetPath().encode('utf-8')


if __name__ == '__main__':
    app = wx.App()
    frame = SelectFile(None, u'外差多普勒型号处理')
    app.MainLoop()