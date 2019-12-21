# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import platform

# libndr.list()

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'NDR Mediathek'
text = 'Gem. Pressemitteilung sind die Inhalte der NDR-Mediathek seit 11.12.2019 ausschließlich über die ARD-Mediathek abrufbar.'
text = text + ' [Py' + platform.python_version() + ']'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
