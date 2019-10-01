# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import libmdr

# libmdr.list()

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'MDR Mediathek'
text = 'Gem. Pressemitteilung sind die Inhalte der MDR-Mediathek seit 11.09.2019 ausschließlich über die ARD-Mediathek abrufbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
