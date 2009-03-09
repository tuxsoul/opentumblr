#!/usr/bin/env python
# -*- coding: us-ascii -*-

from tumblr import Api

import tumblr
import urllib2

# generated by wxGlade 0.6.3 on Wed Mar  4 16:13:34 2009

import wx

# begin wxGlade: extracode
# end wxGlade

errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}

class Login(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Login.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel = wx.Panel(self, -1)
        self.panel_login = wx.Panel(self.panel, -1, style=wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL)
        self.sizer_login_staticbox = wx.StaticBox(self.panel_login, -1, "")
        self.l_tumblr = wx.StaticText(self, -1, "Tumblr", style=wx.ALIGN_CENTRE)
        self.l_login = wx.StaticText(self.panel_login, -1, "Log in")
        self.l_mail = wx.StaticText(self.panel_login, -1, "E-mail address")
        self.tc_mail = wx.TextCtrl(self.panel_login, -1, "", style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
        self.tc_mail.SetValue("mi mail")
        self.l_password = wx.StaticText(self.panel_login, -1, "Password")
        self.tc_password = wx.TextCtrl(self.panel_login, -1, "", style=wx.TE_PROCESS_TAB|wx.TE_PASSWORD)
        self.b_login = wx.Button(self.panel_login, -1, "Login")
        
        self.Bind(wx.EVT_BUTTON, self.OnAuthTumblr, id = self.b_login.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        
    def OnAuthTumblr(self, event):
    	self.Blog = ''
    	self.User = self.tc_mail.GetValue()
    	self.Password = self.tc_password.GetValue()
    	
    	self.api = Api(self.Blog, self.User, self.Password)
    	#assert False,dir(self.api)
    	try:
    		self.auth = self.api.auth_check()
    		print "Te haz logueado"
    	except tumblr.TumblrAuthError:
    		print errors['403']
    	except urllib2.HTTPError:
    		print errors['404']
    	except urllib2.URLError:
    		print errors['urlopen']
    		
    	
    	#print "Api:" % api
		#print 'Email: %s Password: %s'% (self.tc_mail.GetValue() , self.tc_password.GetValue()) 

    def __set_properties(self):
        # begin wxGlade: Login.__set_properties
        self.SetTitle("Login")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.SetForegroundColour(wx.Colour(55, 85, 113))
        self.l_tumblr.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_tumblr.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_tumblr.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_login.SetMinSize((74, 30))
        self.l_login.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_login.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_mail.SetMinSize((260, 30))
        self.l_mail.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_mail.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_mail.SetMinSize((260, 30))
        self.tc_mail.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_mail.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_password.SetMinSize((260, 30))
        self.l_password.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_password.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_password.SetMinSize((260, 30))
        self.tc_password.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_password.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panel_login.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(55, 85, 113))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Login.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_login = wx.StaticBoxSizer(self.sizer_login_staticbox, wx.VERTICAL)
        sizer_1.Add(self.l_tumblr, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_login.Add(self.l_login, 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add(self.l_mail, 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add(self.tc_mail, 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add(self.l_password, 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add(self.tc_password, 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add((30, 30), 0, wx.ALL|wx.EXPAND, 10)
        sizer_login.Add(self.b_login, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        self.panel_login.SetSizer(sizer_login)
        sizer.Add(self.panel_login, 1, wx.ALL|wx.EXPAND, 10)
        self.panel.SetSizer(sizer)
        sizer_1.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Login

class MyLogin(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        f_login = Login(None, -1, "")
        self.SetTopWindow(f_login)
        f_login.Show()
        return 1

# end of class MyLogin

if __name__ == "__main__":
    app = MyLogin(0)
    app.MainLoop()