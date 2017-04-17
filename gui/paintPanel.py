#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
# import wx.lib.mixins.inspection as WIT
from utils.paint import PaintData
matplotlib.use('WXAgg')


class CanvasPanel(wx.Panel):
    def __init__(self, parent, filePath):
        wx.Panel.__init__(self, parent, -1)
        ins = PaintData(filePath)
        timeZoneData = ins.getTdata()
        hzZoneData = ins.getHdata()

        self.figure = Figure()
        self.axesT = self.figure.add_subplot(211)
        self.axesT.plot(timeZoneData['x'], timeZoneData['y'])
        self.axesT.set_xlabel(u'时间/s')
        self.axesT.set_ylabel(u'电压/v')
        self.axesH = self.figure.add_subplot(212)
        self.axesH.plot(hzZoneData['x'], hzZoneData['y'])
        self.axesH.set_xlabel(u'频率/s')
        self.axesH.set_ylabel(u'电压/v')

        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        self.add_toolbar()  # comment this out for no toolbar

    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        # By adding toolbar in sizer, we are able to put it at the bottom
        # of the frame - so appearance is closer to GTK version.
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        # update the axes menu on the toolbar
        self.toolbar.update()


# alternatively you could use
# class App(wx.App):
# class App(WIT.InspectableApp):
#     def OnInit(self):
#         'Create the main window and insert the custom frame'
#         self.Init()
#         frame = wx.Frame(None)
#         CanvasPanel(frame)
#         frame.Show(True)

#         return True

# app = App(0)
# app.MainLoop()