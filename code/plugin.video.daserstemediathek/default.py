# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import libdaserste

# libdaserste.list()

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'Das Erste Mediathek'
text = 'Gem. Pressemitteilung sind die Inhalte dieser Mediathek seit 28.01.2021 ausschließlich über die ARD-Mediathek abrufbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
