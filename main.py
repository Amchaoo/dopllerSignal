#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from gui.mainFrame import MainFrame


if __name__ == '__main__':
    app = wx.App()
    MainFrame(title=u'外差检测中的多普勒分析')
    app.MainLoop()
