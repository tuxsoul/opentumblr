#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Tue Mar 10 22:46:04 2009

from tumblr import Api
import wx

# begin wxGlade: extracode
# end wxGlade



class Text(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Text.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, args[0], **kwds)
        #assert False,dir(args[1])
        self.api = args[1]
        self.p_options = wx.Panel(self, -1)
        self.p_text = wx.Panel(self, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_text_staticbox = wx.StaticBox(self.p_text, -1, "")
        self.l_text = wx.StaticText(self.p_text, -1, "Add a Text Post")
        self.l_title = wx.StaticText(self.p_text, -1, "Title (optional)")
        self.tc_title = wx.TextCtrl(self.p_text, -1, "")
        self.l_post = wx.StaticText(self.p_text, -1, "Post")
        self.tc_post = wx.TextCtrl(self.p_text, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_text, -1, "Create post")
        self.b_preview = wx.Button(self.p_text, -1, "Preview")
        self.b_cancel = wx.Button(self.p_text, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")
        
        self.Bind(wx.EVT_BUTTON, self.OnCreatePost, id = self.b_create.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Text.__set_properties
        self.SetTitle("Add Text Post")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_text.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_title.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_title.SetMinSize((623, 50))
        self.tc_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_post.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_post.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_post.SetMinSize((633, 350))
        self.tc_post.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.b_create.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.b_preview.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.b_cancel.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.b_options.SetMinSize((141, 30))
        self.l_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetSelection(0)
        self.l_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_tag.SetMinSize((201, 80))
        self.tc_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_url.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_url.SetBackgroundColour(wx.Colour(221, 221, 221))
        self.tc_url.SetForegroundColour(wx.Colour(192, 192, 192))
        self.tc_url.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_options.SetBackgroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Text.__do_layout
        gs_text = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_text = wx.StaticBoxSizer(self.s_text_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_text.Add(self.l_text, 0, wx.ALL, 2)
        s_text.Add(self.l_title, 0, wx.ALL, 2)
        s_text.Add(self.tc_title, 0, wx.ALL|wx.EXPAND, 2)
        s_text.Add(self.l_post, 0, wx.ALL|wx.EXPAND, 2)
        s_text.Add(self.tc_post, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_create, 0, wx.LEFT|wx.RIGHT, 2)
        s_buttons.Add(self.b_preview, 0, wx.LEFT|wx.RIGHT, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_RIGHT, 380)
        s_text.Add(s_buttons, 1, wx.ALL|wx.EXPAND, 10)
        self.p_text.SetSizer(s_text)
        gs_text.Add(self.p_text, 1, wx.ALL|wx.EXPAND, 20)
        s_options.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 30)
        s_options.Add(self.l_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.cb_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_url, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_url, 0, wx.ALL|wx.EXPAND, 5)
        self.p_options.SetSizer(s_options)
        gs_text.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.SetSizer(gs_text)
        gs_text.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Text
    def OnCreatePost(self, evt):
		self.title = self.tc_title.GetValue()
		self.body = self.tc_post.GetValue()
		try:
			self.post = self.api.write_regular(self.title, self.body)
		except UnicodeError:
			print "Posteado en blog primario"	
		#print "Posteado en " % self.post
		#assert False,dir(self.post.values)
		self.Close()


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_text = Text(None, -1, "")
    app.SetTopWindow(d_text)
    d_text.Show()
    app.MainLoop()
