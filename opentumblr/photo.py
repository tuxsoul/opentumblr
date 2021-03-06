#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May  4 00:04:42 2009

import wx
import wx.lib.filebrowsebutton as filebrowse


# begin wxGlade: extracode
# end wxGlade



class Photo(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Photo.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Dialog.__init__(self, args[0], **kwds)
        self.api = args[1]
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_photo = wx.Panel(self.panel, -1)
        self.s_photourl_staticbox = wx.StaticBox(self.p_photo, -1, "")
        self.s_photolink_staticbox = wx.StaticBox(self.p_photo, -1, "")
        self.s_photo_staticbox = wx.StaticBox(self.p_photo, -1, "")
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_browse_staticbox = wx.StaticBox(self.p_photo, -1, "")
        self.l_addphoto = wx.StaticText(self.p_photo, -1, "Upload a Photo")
        self.l_photo = wx.StaticText(self.p_photo, -1, "Photo")
        self.b_browse = filebrowse.FileBrowseButton(self.p_photo, -1, size=(703, -1))
        self.l_supports = wx.StaticText(self.p_photo, -1, "Supports JPEG, GIF, PNG and BMP.  Max photo size is 10 MB.")
        self.l_photourl = wx.StaticText(self.p_photo, -1, "Photo Url")
        self.tc_photourl = wx.TextCtrl(self.p_photo, -1, "")
        self.l_caption = wx.StaticText(self.p_photo, -1, "Caption")
        self.tc_caption = wx.TextCtrl(self.p_photo, -1, "", style=wx.TE_MULTILINE)
        self.l_photolink = wx.StaticText(self.p_photo, -1, "Photo links to the URL")
        self.tc_photolink = wx.TextCtrl(self.p_photo, -1, "")
        self.b_create = wx.Button(self.p_photo, -1, "Create post")
        self.b_preview = wx.Button(self.p_photo, -1, "Preview")
        self.b_cancel = wx.Button(self.p_photo, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")

        self.Bind(wx.EVT_BUTTON, self.OnCreatePhoto, id = self.b_create.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Photo.__set_properties
        self.SetTitle("Upload a Photo")
        self.l_addphoto.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addphoto.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_photo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_photo.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_supports.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_photourl.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_photourl.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_photourl.SetMinSize((500, 25))
        self.tc_photourl.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_caption.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_caption.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetMinSize((640, 100))
        self.tc_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_photolink.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_photolink.SetMinSize((624, 50))
        self.tc_photolink.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_photolink.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.p_photo.SetBackgroundColour(wx.Colour(255, 255, 255))
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
        # begin wxGlade: Photo.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        gs_photo = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_photo = wx.StaticBoxSizer(self.s_photo_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_photolink = wx.StaticBoxSizer(self.s_photolink_staticbox, wx.VERTICAL)
        s_photourl = wx.StaticBoxSizer(self.s_photourl_staticbox, wx.HORIZONTAL)
        s_browse = wx.StaticBoxSizer(self.s_browse_staticbox, wx.HORIZONTAL)
        s_photo.Add(self.l_addphoto, 0, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(self.l_photo, 0, wx.ALL|wx.EXPAND, 2)
        s_browse.Add(self.b_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_photo.Add(s_browse, 0, wx.EXPAND, 0)
        s_photo.Add(self.l_supports, 0, wx.BOTTOM|wx.EXPAND, 40)
        s_photourl.Add(self.l_photourl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_photourl.Add(self.tc_photourl, 0, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(s_photourl, 1, wx.EXPAND, 0)
        s_photo.Add(self.l_caption, 0, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(self.tc_caption, 0, wx.ALL, 10)
        s_photolink.Add(self.l_photolink, 0, wx.ALL|wx.EXPAND, 2)
        s_photolink.Add(self.tc_photolink, 0, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(s_photolink, 1, wx.EXPAND, 0)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_buttons.Add(self.b_preview, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 400)
        s_photo.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
        self.p_photo.SetSizer(s_photo)
        gs_photo.Add(self.p_photo, 1, wx.ALL|wx.EXPAND, 20)
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
        gs_photo.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_photo)
        sizer.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Photo
    def OnCreatePhoto(self, evt):
    	self.source = self.tc_photourl.GetValue()
    	if not self.source:
    		self.source = None

    	self.data = self.b_browse.GetValue()
    	if not self.data:
    		self.data = None

    	self.caption = self.tc_caption.GetValue().encode('utf-8')
    	self.click  = self.tc_photolink.GetValue()
    	try:
    		self.post = self.api.write_photo(self.source, self.data, self.caption, self.click)
    	except:
    		print "Posteado en el primario"
    	self.Close()


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    f_photo = Photo(None, -1, "")
    app.SetTopWindow(f_photo)
    f_photo.Show()
    app.MainLoop()
