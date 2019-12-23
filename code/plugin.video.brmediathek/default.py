# -*- coding: utf-8 -*-
import xbmcgui
import libmediathek3 as libMediathek
import libbr

if libbr.list() == False:
	dialog = xbmcgui.Dialog()
	title = 'BR Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)

