# -*- coding: utf-8 -*-
import xbmcgui
import libmediathek3 as libMediathek
import libard

if libard.list() == False:
	dialog = xbmcgui.Dialog()
	title = 'ARD Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)
