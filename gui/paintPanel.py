#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import wx
import numpy as np
import string
# import wx.lib.mixins.inspection as WIT
from utils.paint import PaintData
matplotlib.use('WXAgg')
matplotlib.rcParams['font.sans-serif'] = ['SimHei']


class CanvasPanel(wx.Panel):
    def __init__(self, parent, filePath):
        wx.Panel.__init__(self, parent, -1)
        self.ins = PaintData(filePath)
        self.initNoteBook()
        self.initLayout()

    def xcorrGragh(self, parent):
        timeZoneData = self.ins.getXcorrTimeZoneData()
        hzZoneData = self.ins.getXcorrHZoneData()
        canvas = FigureCanvas(parent, -1, self.graghFigure(timeZoneData, hzZoneData))
        return canvas

    def normalGragh(self, parent):
        timeZoneData = self.ins.getTimeZoneData()
        hzZoneData = self.ins.getHZoneData()
        canvas = FigureCanvas(parent, -1, self.graghFigure(timeZoneData, hzZoneData))
        return canvas

    def comparedGragh(self, parent):
        t1 = self.ins.getTimeZoneData()
        t2 = self.ins.getXcorrTimeZoneData()
        h1 = self.ins.getHZoneData()
        h2 = self.ins.getXcorrHZoneData()
        canvas = FigureCanvas(parent, -1, self.comparedGraghFigure(t1, t2, h1, h2))
        return canvas

    def initLayout(self):
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.noteBook, 1, flag=wx.ALIGN_CENTER | wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()

        # self.add_toolbar()

    def initNoteBook(self):
        self.noteBook = wx.Notebook(self)
        panel1 = self.normalGragh(self.noteBook)
        panel2 = self.xcorrGragh(self.noteBook)
        panel3 = self.comparedGragh(self.noteBook)
        self.noteBook.AddPage(panel1, u'原始数据不做去噪处理')
        self.noteBook.AddPage(panel2, u'原始数据自相关去噪')
        self.noteBook.AddPage(panel3, u'对比')

    def graghFigure(self, timeZoneData, hzZoneData):
        figure = Figure(linewidth=1)
        axesT = figure.add_axes([0.1, 0.6, 0.8, 0.35])
        axesT.plot(timeZoneData['x'], timeZoneData['y'])
        axesT.set_xlabel(u'时间/s')
        axesT.set_ylabel(u'电压/v\n')
        axesT.set_title(u'时域图象')

        axesH = figure.add_axes([0.1, 0.1, 0.8, 0.35])
        axesH.plot(hzZoneData['x'], hzZoneData['y'], '-')
        axesH.set_xlabel(u'频率/hz')
        axesH.set_ylabel(u'电压/v')
        axesH.set_title(u'\nDFT之后频域图象')

        for index in hzZoneData['speaks']:
            axesH.annotate(hzZoneData['x'][index],
                xy=(hzZoneData['x'][index], hzZoneData['y'][index]),
                xytext=(hzZoneData['x'][index], hzZoneData['y'][index]),
                arrowprops=dict(facecolor='green', shrink=0.01))

        return figure

    def comparedGraghFigure(self, t1, t2, h1, h2):
        figure = Figure(linewidth=1)
        # axesT = figure.add_subplot(211)
        ax1 = figure.add_axes([0.1, 0.1, 0.8, 0.35])
        ax2 = figure.add_axes([0.1, 0.6, 0.8, 0.35])
        l1, l2 = ax1.plot(
            t1['x'], self.normalizeArray(t1['y']), 'r',
            t2['x'], self.normalizeArray(t2['y']), 'g')

        figure.legend((l1, l2), (u'原始数据', u'自相关后'), 'upper left')

        # axesH = figure.add_subplot(212)
        l3, l4 = ax2.plot(
            h1['x'], self.normalizeArray(h1['y']), 'r',
            h2['x'], self.normalizeArray(h2['y']), 'g')
        figure.legend((l3, l4), (u'原始数据', u'自相关后'), 'upper left')

        return figure

    def normalizeArray(self, a):
        if not isinstance(a, int):
            a = [string.atof(i) for i in a]

        if not isinstance(a, np.ndarray):
            a = np.array(a)

        print type(a)
        amin, amax = a.min(), a.max()
        a = (a-amin)/(amax-amin)
        return a
