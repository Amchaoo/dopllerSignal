#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
 
class ExampleFrame(wx.Frame):
    def __init__(self,parent=None,id=-1,title='MyFrame'):
        wx.Frame.__init__(self,parent=parent,id=id,title=title)
        self.Centre()
        box1 = vBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
 
        btn1 = wx.Button(self, -1, u'你好', style=wx.ALIGN_CENTER)
        btn2 = wx.Button(self,label='btn2', style=wx.ALIGN_RIGHT)
        btn3 = wx.Button(self,label='btn3')
        btn4 = wx.Button(self,label='btn4')
        btn5 = wx.Button(self,label='btn5')
 
        #BoxSizer布局
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        box1.Add(btn1, proportion=10,border=5, flag=wx.ALIGN_CENTER|wx.EXPAND)
        vBoxSizer.Add(box1, 10, flag=wx.ALIGN_CENTER)
        vBoxSizer.Add(btn2, proportion=2,flag=wx.TOP|wx.BOTTOM|wx.EXPAND,border=10)
        vBoxSizer.Add(btn3, proportion=3,flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10)
        vBoxSizer.Add(btn4, proportion=2,flag=wx.ALL|wx.EXPAND,border=10)
        vBoxSizer.Add(btn5, proportion=1,flag=wx.TOP|wx.BOTTOM|wx.EXPAND,border=5)
        #vBoxSizer.AddMany([(btn3,proportion=2,flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10),(btn4)])
        self.SetSizer(vBoxSizer)
 
class ExampleApp(wx.App):
    def OnInit(self):
        frame = ExampleFrame()
        frame.Show()
        return True
 
if __name__  == "__main__":
    app = ExampleApp()
    app.MainLoop()