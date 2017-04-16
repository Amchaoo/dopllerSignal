#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
from gui.selectFile import SelectFile


class GaugePanel(wx.Panel):
    def __init__(self, parent, pipe=None):
        wx.Panel.__init__(self, parent, wx.ID_ANY, size=(500, 250))
        self.parent = parent
        self.SetBackgroundColour("white")
        self.count = 0
        self.gauge = wx.Gauge(
            self, -1, 100, (100, 50), (300, 30), style=wx.GA_PROGRESSBAR)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Center(True)

    def OnIdle(self, event):
        self.count = self.count + 1
        self.gauge.SetValue(self.count)

        if self.count == 100:
            self.parent.panel = SelectFile(self.parent)
            self.Close()


