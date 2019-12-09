# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
from libbr import list

if list() == False:
	dialog = xbmcgui.Dialog()
	title = 'BR Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)

