#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200, 100))
        read_file_button = wx.Button(self, wx.ID_OPEN, '&Open')
        self.Bind(wx.EVT_BUTTON, self.openCsvFile, read_file_button)
        self.Show(True)

    def openFile(self, e):
        dig = wx.FileDialog(self, message="open file", style=wx.FD_PREVIEW, wildcard="*.csv")
        if dig.ShowModal() == wx.ID_OK:
            # print dig.GetDirectory().encode('utf-8')
            return dig.GetPath().encode('utf-8')


app = wx.App()
frame = MyFrame(None, 'prac')
app.MainLoop()