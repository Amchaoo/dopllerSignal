#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx


class LoginFrame(wx.Frame):
    def __init__(self, parent, id, title, size):

        wx.Frame.__init__(self, parent, id, title)
        self.Center()
        self.SetSize(size)  # 要在这里初始化长宽，只传给init参数没用

        self.bkg = wx.Panel(self)

        self.font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)

        self.ServerName = wx.StaticText(self.bkg, label="Server Address: ")
        self.ServerName.SetFont(self.font)
        self.Input_ServerName = wx.TextCtrl(self.bkg)

        self.UserName = wx.StaticText(self.bkg, label="       User Name: ")
        self.UserName.SetFont(self.font)
        self.Input_UserName = wx.TextCtrl(self.bkg)

        self.LoginButton = wx.Button(self.bkg, label="Login")
        self.QuitButton = wx.Button(self.bkg, label="Quit")

        self.box1 = wx.BoxSizer()
        self.box1.Add(self.ServerName, proportion=0)
        self.box1.Add(self.Input_ServerName, proportion=1,
                      flag=wx.EXPAND | wx.ALL, border=5)

        self.box2 = wx.BoxSizer()
        self.box2.Add(self.UserName, proportion=0)
        self.box2.Add(self.Input_UserName, proportion=1,
                      flag=wx.EXPAND | wx.ALL, border=5)

        self.box3 = wx.BoxSizer()
        self.box3.Add(self.LoginButton, proportion=1)
        self.box3.Add(self.QuitButton, proportion=1)

        self.allbox = wx.BoxSizer(wx.VERTICAL)
        self.allbox.Add(self.box1, flag=wx.EXPAND | wx.ALL, border=20)
        self.allbox.Add(self.box2, flag=wx.EXPAND | wx.ALL, border=20)
        self.allbox.Add(self.box3, flag=wx.EXPAND | wx.ALL, border=20)

        self.bkg.SetSizer(self.allbox)

        self.LoginButton.Bind(wx.EVT_BUTTON, self.Login)
        self.QuitButton.Bind(wx.EVT_BUTTON, self.CloseWin)
        self.Show(True)

    def Login(self, evt):
        # Login
        #
        self.Close()
        ChatFrame(None, -1, title="chatroom", size=(500, 400))

    def CloseWin(self, evt):
        self.Close()


class ChatFrame(wx.Frame):
    def __init__(self, parent, id, title, size):

        wx.Frame.__init__(self, parent, id, title)
        self.Center()
        self.SetSize(size)

        self.bkg = wx.Panel(self)  # 将控件放在Panel上，而不是直接放在frame上

        self.tshow = wx.TextCtrl(self.bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

        self.tinput = wx.TextCtrl(self.bkg)
        self.bt = wx.Button(self.bkg, label="Send")

        self.box1 = wx.BoxSizer()
        self.box1.Add(self.tinput, proportion=1, flag=wx.EXPAND)
        self.box1.Add(self.bt, proportion=0)

        self.box2 = wx.BoxSizer(wx.VERTICAL)
        self.box2.Add(self.tshow, flag=wx.EXPAND |
                      wx.ALL, border=5, proportion=1)
        self.box2.Add(self.box1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM |
                      wx.RIGHT, border=5, proportion=0)  # 把第一个BoxSiSizer放入整体Boxizer

        self.bkg.SetSizer(self.box2)

        self.bt.Bind(wx.EVT_BUTTON, self.btaction)  # 为控件绑定事件和处理函数
        self.Bind(wx.EVT_CLOSE, self.closewin)
        self.Show(True)

    def btaction(self, evt):
        self.tshow.AppendText(self.tinput.GetValue() + "\n")
        self.tinput.SetValue("")

    def tcaction(self, evt):
        print "aa"

    def closewin(self, evt):
        print "close.."
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    LoginFrame(None, -1, title="LoginFrame", size=(500, 250))
    app.MainLoop()
