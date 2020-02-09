#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import date, timedelta

import libardneu
import libardplayer
import libardjsonparser as libArdJsonParser

import libmediathek3 as libMediathek

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus

translation = libMediathek.getTranslation
params = libMediathek.get_params() 

def list():
	# return libardneu.list()
	return libMediathek.list(modes, 'libArdListMain', 'libArdPlayClassic', 'libArdPlayNeu')

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
	l.append({'name':translation(31032), 'mode':'libArdListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Rubriken/mehr?documentId=21282550&json', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Themen/mehr?documentId=21301810&json', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListVideos():
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
	return libMediathek.populateDirDate('libArdListChannelDateVideos',params['channel'])

def libArdListChannelDateVideos():
	url = 'http://appdata.ardmediathek.de/appdata/servlet/tv/sendungVerpasst?json&kanal='+channels[int(params['channel'])][1]+'&tag='+params['datum']
	return libArdJsonParser.parseDate(url)

def libArdPlayClassic():
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
	'libArdPlayNeu': libardneu.libArdPlayNeu,
}