#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May  4 00:13:17 2009

import wx

# begin wxGlade: extracode
# end wxGlade



class Video(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Video.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, args[0], **kwds)
        self.api = args[1]
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_video = wx.Panel(self.panel, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_video_staticbox = wx.StaticBox(self.p_video, -1, "")
        self.l_addvideo = wx.StaticText(self.p_video, -1, "Add a Video")
        self.l_embed = wx.StaticText(self.p_video, -1, "Embed a Video")
        self.label_1 = wx.StaticText(self.p_video, -1, "This can be a URL from video sites like YouTube or Vimeo, or the raw Embed-tag from\nany video/flash site. (ie. http://youtube.com/watch?v=oCmAD-z7-mA)")
        self.tc_embed = wx.TextCtrl(self.p_video, -1, "")
        self.l_caption = wx.StaticText(self.p_video, -1, "Caption (optional)")
        self.tc_caption = wx.TextCtrl(self.p_video, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_video, -1, "Create post")
        self.b_preview = wx.Button(self.p_video, -1, "Preview")
        self.b_cancel = wx.Button(self.p_video, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")

        self.Bind(wx.EVT_BUTTON, self.OnCreateVideo, id = self.b_create.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Video.__set_properties
        self.SetTitle("Add a Video")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_addvideo.SetMinSize((-1, 80))
        self.l_addvideo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addvideo.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_embed.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_embed.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_1.SetForegroundColour(wx.Colour(35, 142, 107))
        self.tc_embed.SetMinSize((600, 150))
        self.tc_embed.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 1, ""))
        self.l_caption.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_caption.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetMinSize((600, 150))
        self.tc_caption.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.p_video.SetBackgroundColour(wx.Colour(255, 255, 255))
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
        # begin wxGlade: Video.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        gs_video = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_video = wx.StaticBoxSizer(self.s_video_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_video.Add(self.l_addvideo, 0, wx.ALL|wx.EXPAND, 2)
        s_video.Add(self.l_embed, 0, wx.ALL|wx.EXPAND, 2)
        s_video.Add(self.label_1, 0, wx.ALL|wx.EXPAND, 2)
        s_video.Add(self.tc_embed, 0, wx.ALL|wx.EXPAND, 10)
        s_video.Add(self.l_caption, 0, wx.ALL|wx.EXPAND, 2)
        s_video.Add(self.tc_caption, 0, wx.ALL|wx.EXPAND, 10)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_preview, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 363)
        s_video.Add(s_buttons, 1, wx.ALL|wx.EXPAND, 2)
        self.p_video.SetSizer(s_video)
        gs_video.Add(self.p_video, 1, wx.ALL|wx.EXPAND, 20)
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
        gs_video.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_video)
        sizer_1.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Video
    def OnCreateVideo(self, evt):
    	self.embed = self.tc_embed.GetValue()
    	self.caption = self.tc_caption.GetValue().encode('utf-8')
    	try:
    		self.post = self.api.write_video(self.embed, self.caption)
    	except:
    		print "posteado en el blog primario"
    	self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_video = Video(None, -1, "")
    app.SetTopWindow(d_video)
    d_video.Show()
    app.MainLoop()
