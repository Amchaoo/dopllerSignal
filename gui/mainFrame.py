#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from gui.intro import Intro
from gui.gauge import GaugePanel


class MainFrame(wx.Frame):
    def __init__(self, parent=None, title=''):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.Center()
        self.__initMenu()
        self.panel = Intro(self)

        self.Show(True)

    def __initMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_OPEN, u"打开")
        self.Bind(wx.EVT_MENU, self.openFile, id=wx.ID_OPEN)

        menu.AppendSeparator()
        menu.Append(wx.ID_CLOSE, u"退出")
        self.Bind(wx.EVT_MENU, self.close, id=wx.ID_CLOSE)

        menuBar = wx.MenuBar()
        menuBar.Append(menu, u"文件")
        self.SetMenuBar(menuBar)

    def openFile(self, e):
        dig = wx.FileDialog(
            self, message=u"请选择外差数据文件",
            style=wx.FD_PREVIEW, wildcard="*.csv")
        if dig.ShowModal() == wx.ID_OK:
            self.filePath = dig.GetPath().encode('utf-8')
            self.showGauge()
        else:
            self.filePath = ''

    def close(self, e):
        dlg = wx.MessageDialog(
            self, u'确认退出',
            '退出挺行', wx.YES_NO | wx.ICON_EXCLAMATION)

        if dlg.ShowModal() == wx.ID_YES:
            self.Close()

    def showGauge(self):
        self.panel.Destroy()
        self.panel = GaugePanel(self)
        # wx.CallAfter(self.showSlect)

    # def showSlect(self):
    #     self.gaugePanel.Hide()
    #     self.filePanel.Show()


