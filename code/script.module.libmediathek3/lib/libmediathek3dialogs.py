# -*- coding: utf-8 -*-
import sys
import xbmcgui

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus

from libmediathek3utils import *

def dialogDate():
	dialog = xbmcgui.Dialog()
	return dialog.numeric(1, getTranslation(31030)).replace('/','').replace(' ','0')

def getSearchString(do_quote=True):
	keySearchString = 'searchString'
	f_mkdir(pathUserdata(''))
	search_string = f_open(pathUserdata(keySearchString))
	dialog = xbmcgui.Dialog()
	search_string = dialog.input(getTranslation(31039),type=xbmcgui.INPUT_ALPHANUM,defaultt=search_string)
	f_write(pathUserdata(keySearchString), search_string)
	if do_quote:
		search_string = quote_plus(search_string)
	return search_string
