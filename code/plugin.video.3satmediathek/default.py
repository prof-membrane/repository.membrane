# -*- coding: utf-8 -*-
import xbmcgui
import libmediathek3 as libMediathek
import lib3sathtmlparser

if lib3sathtmlparser.list() == False:
	dialog = xbmcgui.Dialog()
	title = '3sat Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)

"""

import xbmc
import xbmcgui
import libmediathek3 as libMediathek

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = '3sat Mediathek'
text = 'Wegen Änderungen an der 3sat Website ist die 3sat Mediathek bis auf Weiteres nicht verfügbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
"""