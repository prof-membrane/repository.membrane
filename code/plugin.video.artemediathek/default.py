# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import libarte

if libarte.list() == False:
	dialog = xbmcgui.Dialog()
	title = 'ARTE Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)

