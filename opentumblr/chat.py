#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun May  3 23:57:11 2009

import wx
import string
try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api
# begin wxGlade: extracode
# end wxGlade



class Chat(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Chat.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, args[0], **kwds)
        self.api = args[1]
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_chat = wx.Panel(self.panel, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_chat_staticbox = wx.StaticBox(self.p_chat, -1, "")
        self.l_addchat = wx.StaticText(self.p_chat, -1, "Add a Chat Post")
        self.l_title = wx.StaticText(self.p_chat, -1, "Title (optional)")
        self.tc_title = wx.TextCtrl(self.p_chat, -1, "")
        self.l_dialogue = wx.StaticText(self.p_chat, -1, "Dialogue")
        self.l_example = wx.StaticText(self.p_chat, -1, "Example")
        self.l_tourist = wx.StaticText(self.p_chat, -1, "Tourist: Could you give us directions to Olive Garden?")
        self.l_nyorker = wx.StaticText(self.p_chat, -1, "New Yorker: No, but I could give you directions to an actual Italian restaurant.")
        self.tc_dialogue = wx.TextCtrl(self.p_chat, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_chat, -1, "Create post")
        self.b_preview = wx.Button(self.p_chat, -1, "Preview")
        self.b_cancel = wx.Button(self.p_chat, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")

        self.Bind(wx.EVT_BUTTON, self.OnCreateChat, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())
        self.Bind(wx.EVT_COMBOBOX, self.OnPublishingOptions, id = self.cb_publishing.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Chat.__set_properties
        self.SetTitle("Add Text Post")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_addchat.SetMinSize((-1, 80))
        self.l_addchat.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addchat.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_title.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_title.SetMinSize((600, 50))
        self.tc_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        self.l_dialogue.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_dialogue.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_example.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.l_example.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_tourist.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.l_nyorker.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.tc_dialogue.SetMinSize((600, 150))
        self.tc_dialogue.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.p_chat.SetBackgroundColour(wx.Colour(255, 255, 255))
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
        self.panel.SetBackgroundColour(wx.Colour(55, 85, 113))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Chat.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        gs_chat = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_chat = wx.StaticBoxSizer(self.s_chat_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_chat.Add(self.l_addchat, 0, wx.ALL|wx.EXPAND, 2)
        s_chat.Add(self.l_title, 0, wx.ALL|wx.EXPAND, 2)
        s_chat.Add(self.tc_title, 0, wx.ALL|wx.EXPAND, 10)
        s_chat.Add(self.l_dialogue, 0, wx.ALL|wx.EXPAND, 2)
        s_chat.Add(self.l_example, 0, wx.LEFT|wx.TOP|wx.EXPAND, 2)
        s_chat.Add(self.l_tourist, 0, wx.LEFT|wx.EXPAND, 2)
        s_chat.Add(self.l_nyorker, 0, wx.LEFT|wx.EXPAND, 2)
        s_chat.Add(self.tc_dialogue, 0, wx.ALL|wx.EXPAND, 10)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_preview, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 363)
        s_chat.Add(s_buttons, 1, wx.ALL|wx.EXPAND, 2)
        self.p_chat.SetSizer(s_chat)
        gs_chat.Add(self.p_chat, 1, wx.ALL|wx.EXPAND, 20)
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
        gs_chat.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_chat)
        sizer.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Chat
    def OnPublishingOptions(self, evt):
        if self.cb_publishing.GetValue() == "add to queue" or self.cb_publishing.GetValue() == "private":
            self.l_date.Show(False)
            self.tc_date.Show(False)
            self.tc_tag.SetFocus()
            
        if self.cb_publishing.GetValue() == "publish now" or self.cb_publishing.GetValue() == "publish on...":
            if self.cb_publishing.GetValue() == "publish on...":
                self.l_date.SetLabel('Publish time:')
                self.tc_date.SetValue('next tuesday, 10am')
            else:
                self.l_date.SetLabel('Date this post')
                self.tc_date.SetValue('now')
            
            self.l_date.Show()
            self.tc_date.Show()
            self.tc_date.SetFocus()
            
        if self.cb_publishing.GetValue() == "save as draft":
            self.l_date.SetLabel('Status message:')
            self.tc_date.SetValue('')
            self.tc_date.Show()
            self.tc_date.SetFocus()
            
    def OnCreateChat(self, evt):
    	self.title = self.tc_title.GetValue().encode('utf-8')
    	self.conversation = self.tc_dialogue.GetValue().encode('utf-8')
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0


        #self.format = None
        self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
    	try:
    		self.post = self.api.write_conversation(self.title, self.conversation)
    	except:
    		print "posteado en el blog primario"
    	self.Close()

    def OnCancel(self, evt):
	    self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_chat = Chat(None, -1, "")
    app.SetTopWindow(d_chat)
    d_chat.Show()
    app.MainLoop()
