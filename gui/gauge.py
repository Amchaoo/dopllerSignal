#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class GaugePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, size=(500, 250))
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
