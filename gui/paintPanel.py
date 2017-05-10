#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
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

    def windowFFTGragh(self, parent):
        timeZoneData = self.ins.getTimeZoneData()
        hzZoneData = self.ins.getHZoneDataWithWindow()
        canvas = FigureCanvas(parent, -1, self.graghFigure(timeZoneData, hzZoneData))
        return canvas

    def xcorrWindowFFTFragh(self, parent):
        timeZoneData = self.ins.getXcorrTimeZoneData()
        hzZoneData = self.ins.getXcorrHZoneDataWithWindow()
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
        panel4 = self.windowFFTGragh(self.noteBook)
        panel5 = self.xcorrWindowFFTFragh(self.noteBook)
        self.noteBook.AddPage(panel1, u'原始数据+FFT')
        self.noteBook.AddPage(panel2, u'自相关去噪+FFT')
        self.noteBook.AddPage(panel4, u'加窗计算频域')
        self.noteBook.AddPage(panel5, u'自相关去噪+加窗计算频域')
        self.noteBook.AddPage(panel3, u'对比')

    def graghFigure(self, timeZoneData, hzZoneData):
        figure = Figure(linewidth=1)
        axesT = figure.add_axes([0.1, 0.6, 0.8, 0.35])
        axesT.plot(timeZoneData['x'], timeZoneData['y'], lw=1)
        axesT.set_xlabel(u'时间/s')
        axesT.set_ylabel(u'电压/v')
        axesT.set_title(u'时域图象')

        axesH = figure.add_axes([0.1, 0.1, 0.8, 0.35])
        axesH.plot(hzZoneData['x'], hzZoneData['y'], '-', lw=1)
        # axesH.set_xlim(0)
        axesH.set_xlabel(u'频率/hz')
        axesH.set_ylabel(u'电压/v')
        axesH.set_title(u'DFT之后频域图象')

        for index in hzZoneData['speaks']:
            axesH.annotate(
                hzZoneData['x'][index],
                xy=(hzZoneData['x'][index], hzZoneData['y'][index]),
                xytext=(1, 30),
                textcoords='offset points',
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

        return figure

    def comparedGraghFigure(self, t1, t2, h1, h2):
        figure = Figure(linewidth=1)
        # axesT = figure.add_subplot(211)
        ax1 = figure.add_axes([0.13, 0.6, 0.8, 0.35])
        ax2 = figure.add_axes([0.13, 0.1, 0.8, 0.35])
        l1, l2 = ax1.plot(
            t1['x'], self.normalizeArray(t1['y']), 'r',
            t2['x'], self.normalizeArray(t2['y']), 'g', lw=0.7)

        figure.legend((l1, l2), (u'原始数据', u'自相关后'), 'upper left')

        l3, l4 = ax2.plot(
            h1['x'], self.normalizeArray(h1['y']), 'r',
            h2['x'], self.normalizeArray(h2['y']), 'g', lw=0.7)
        figure.legend((l3, l4), (u'原始数据', u'自相关后'), 'center left')

        return figure

    def normalizeArray(self, a):
        if not isinstance(a, int):
            a = [string.atof(i) for i in a]

        if not isinstance(a, np.ndarray):
            a = np.array(a)

        amin, amax = a.min(), a.max()
        a = (a-amin)/(amax-amin)
        return a
