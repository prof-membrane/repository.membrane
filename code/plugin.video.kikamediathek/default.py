# -*- coding: utf-8 -*-
import libkika

import xbmc
import xbmcgui
import libmediathek3 as libMediathek
import platform

# libkika.list()

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'KiKa Mediathek'
text = 'Die KiKa Mediathek ist momentan nicht verfügbar. Bitte nutzen Sie stattdessen die ZDFtivi Mediathek.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
