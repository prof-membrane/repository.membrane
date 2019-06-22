# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
from lib3sathtmlparser import list

if list() == False:
	dialog = xbmcgui.Dialog()
	title = '3sat Mediathek'
	text = 'Dieses Medium ist kein abspielbares Video.'
	dialog.ok(title, text)

"""
libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = '3sat Mediathek'
text = 'Aufgrund von Änderungen an der 3sat Website ist die 3sat Mediathek für Kodi bis auf Weiteres nicht verfügbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
"""