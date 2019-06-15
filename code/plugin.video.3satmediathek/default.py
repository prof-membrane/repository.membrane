# -*- coding: utf-8 -*-
from lib3sat import *
import xbmc
import xbmcgui
import libmediathek3 as libMediathek

# war: list()

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = "3sat Mediathek"
text = "Aufgrund von Änderungen an der 3sat Website ist die 3sat Mediathek für Kodi bis auf Weiteres nicht verfügbar."
dialog.ok(title, text)
xbmc.executebuiltin("XBMC.ActivateWindow(Home)")
