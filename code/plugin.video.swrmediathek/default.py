# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import platform

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'SWR Mediathek'
text = 'Gem. Pressemitteilung sind die Inhalte der SWR-Mediathek seit 19.08.2019 ausschließlich über die ARD-Mediathek abrufbar.'
text = text + ' [Py' + platform.python_version() + ']'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
