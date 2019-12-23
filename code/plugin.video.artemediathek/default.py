# -*- coding: utf-8 -*-
import xbmcgui
import libmediathek3 as libMediathek
import libarte

if libarte.list() == False:
	dialog = xbmcgui.Dialog()
	title = 'ARTE Mediathek'
	text = libMediathek.getTranslation(31043)
	dialog.ok(title, text)

"""

import xbmc
import xbmcgui
import libmediathek3 as libMediathek

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'ARTE Mediathek'
text = 'Wegen Änderungen an der ARTE Website ist die ARTE Mediathek bis auf Weiteres nicht verfügbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')

"""