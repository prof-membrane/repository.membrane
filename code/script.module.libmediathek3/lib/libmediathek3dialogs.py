# -*- coding: utf-8 -*-
import sys
import xbmcgui

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus

import libmediathek3utils

def dialogDate():
	dialog = xbmcgui.Dialog()
	return dialog.numeric(1, libmediathek3utils.getTranslation(31030)).replace('/','').replace(' ','0')

def getSearchString(do_quote=True):
	dialog = xbmcgui.Dialog()
	d = dialog.input(libmediathek3utils.getTranslation(31039),type=xbmcgui.INPUT_ALPHANUM)
	if do_quote:
		d = quote_plus(d)
	return d
