#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import xbmc
import xbmcgui
import xbmcaddon
import libardneu
import libardplayer
import libardjsonparser as libArdJsonParser

import libmediathek3 as libMediathek

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus

def list():
	show_hint_classic = libMediathek.getSettingBool('show_hint_classic')
	if show_hint_classic:
		libMediathek.setSettingBool('show_hint_classic', False)
		addon = xbmcaddon.Addon()
		title = addon.getAddonInfo('name')
		text = addon.getLocalizedString(32100)
		xbmcgui.Dialog().ok(title, text)
	use_classic = libMediathek.getSettingBool('use_classic')
	use_classic_prev_value = libMediathek.getSettingBool('use_classic_prev_value')
	if (use_classic != use_classic_prev_value) or show_hint_classic:
		xbmc.executebuiltin('Container.Update(path,replace)')
		params = libMediathek.get_params()
		if 'mode' in params: 
			del params['mode']  # force default mode
		if use_classic != use_classic_prev_value:
			libMediathek.setSettingBool('use_classic_prev_value', use_classic)
			addon = xbmcaddon.Addon()
			title = addon.getAddonInfo('name')
			text = addon.getLocalizedString(32101)
			xbmcgui.Dialog().notification(title, text, os.path.join(addon.getAddonInfo('path'), 'icon.png'))
	if use_classic: 
		return libMediathek.list(modes, 'libArdListMain', 'libArdPlayClassic', 'libArdPlayHtml')
	else:
		return libardneu.list()

channels = [
	('ARD-alpha','5868'),
	('BR','2224'),
	('Das Erste','208'),
	('HR','5884'),
	('MDR','5882'),
	('MDR / Sachsen','1386804'),
	('MDR / Sachsen-Anhalt','1386898'),
	('MDR / Thüringen','1386988'),
	('NDR','5906'),
	('One','673348'),
	('RB','5898'),
	('RBB','5874'),
	('SR','5870'),
	('SWR','5310'),
	('SWR / Baden-Württemberg','5904'),
	('SWR / Rheinland-Pfalz','5872'),
	('Tagesschau24','5878'),
	('WDR','5902'),
]

def libArdListMain():
	l = []
	translation = libMediathek.getTranslation
	l.append({'name':translation(31032), 'mode':'libArdListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Rubriken/mehr?documentId=21282550&json', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Themen/mehr?documentId=21301810&json', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListVideos():
	params = libMediathek.get_params()
	return libArdJsonParser.parseVideos(params['url'])

def libArdListShows():
	return libArdJsonParser.parseAZ()

def libArdListChannel():
	l = []
	for i, channel in enumerate(channels):
		d = {}
		d['_name'] = channel[0]
		d['_type'] = 'dir'
		d['channel'] = str(i)
		d['mode'] = 'libArdListChannelDate'
		l.append(d)
	return l

def libArdListChannelDate():
	params = libMediathek.get_params()
	return libMediathek.populateDirDate('libArdListChannelDateVideos',params['channel'])

def libArdListChannelDateVideos():
	params = libMediathek.get_params()
	url = 'http://appdata.ardmediathek.de/appdata/servlet/tv/sendungVerpasst?json&kanal='+channels[int(params['channel'])][1]+'&tag='+params['datum']
	return libArdJsonParser.parseDate(url)

def libArdPlayClassic():
	params = libMediathek.get_params()
	result = libardplayer.getVideoUrlClassic(videoID = params['documentId'])
	result = libMediathek.getMetadata(result)
	return result

modes = {
	'libArdListMain': libArdListMain,
	'libArdListVideos': libArdListVideos,
	'libArdListShows': libArdListShows,
	'libArdListChannel': libArdListChannel,
	'libArdListChannelDate': libArdListChannelDate,
	'libArdListChannelDateVideos': libArdListChannelDateVideos,
	'libArdListSearch': libardneu.libArdListSearch,
	'libArdPlayClassic': libArdPlayClassic,
	'libArdPlayHtml': libardneu.libArdPlayHtml,
}