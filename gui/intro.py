#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import os
import os.path
from PIL import Image


class Intro(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.SetBackgroundColour('white')

        self.__initFont()
        self.__initWidget()
        self.__initSizer()
        self.__initLayout()

    def __initFont(self):
        self.font1 = wx.Font(26, wx.FONTFAMILY_SCRIPT, wx.NORMAL, wx.NORMAL)
        self.font2 = wx.Font(22, wx.FONTFAMILY_SCRIPT, wx.NORMAL, wx.NORMAL)
        self.font3 = wx.Font(18, wx.FONTFAMILY_SCRIPT, wx.NORMAL, wx.NORMAL)

    def __initWidget(self):
        self.__initLogo()

        self.titleOne = wx.StaticText(self, -1, u"外差多普勒信号分析")
        self.titleTwo = wx.StaticText(self, -1, u"毕业设计")
        self.titleThree = wx.StaticText(self, -1, u"作者:安超")

        self.titleOne.SetFont(self.font1)
        self.titleTwo.SetFont(self.font2)
        self.titleThree.SetFont(self.font3)

    def __initSizer(self):
        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.hBox0 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox1 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox3 = wx.BoxSizer(wx.HORIZONTAL)

    def __initLayout(self):
        self.hBox0.Add(self.logo, 0, flag=wx.ALIGN_LEFT)
        self.hBox1.Add(self.titleOne, 0, flag=wx.ALIGN_CENTER)
        self.hBox2.Add(self.titleTwo, 0, flag=wx.ALIGN_LEFT)
        self.hBox3.Add(self.titleThree, 0, flag=wx.ALIGN_CENTER)

        self.vBox.Add(self.hBox0, 2, flag=wx.ALIGN_LEFT)
        self.vBox.Add(self.hBox1, 2, flag=wx.ALIGN_CENTER)
        self.vBox.Add(self.hBox2, 6, flag=wx.ALIGN_CENTER)
        self.vBox.Add(self.hBox3, 2, flag=wx.ALIGN_CENTER)

        self.SetSizer(self.vBox, 1)

    def __initLogo(self):
        print os.getcwd()
        resizeImage('./gui/image/logo.png', 200, 60)
        logo = wx.Image('./gui/image/logo.png', wx.BITMAP_TYPE_PNG)
        temp = logo.ConvertToBitmap()
        self.logo = wx.StaticBitmap(self, bitmap=temp)


def resizeImage(file, width, height, type='png'):
    img = Image.open(file)
    out = img.resize((width, height), Image.ANTIALIAS)
    out.save(file, type)


if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None)
    Intro(frame)
    frame.Show(True)
    frame.Centre()
    app.MainLoop()