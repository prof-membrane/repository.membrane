# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import libwdr

if libwdr.list() == False:
	dialog = xbmcgui.Dialog()
	title = 'WDR Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)
