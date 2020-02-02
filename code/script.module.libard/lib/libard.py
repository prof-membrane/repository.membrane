# -*- coding: utf-8 -*-
import sys
from datetime import date, timedelta

import libardlisting
import libardrssparser
import libardplayer
import libardjsonparser as libArdJsonParser

import libmediathek3 as libMediathek

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus


def getNew():
	return libardlisting.listRSS('http://www.ardmediathek.de/tv/Neueste-Videos/mehr?documentId=21282466&rss=true')

def getMostViewed():
	return libardlisting.listRSS('http://www.ardmediathek.de/tv/Meistabgerufene-Videos/mehr?documentId=21282514&m23644322=quelle.tv&rss=true')

def getSearch(search_string,page=0):
	return libArdJsonParser.parseSearch('http://www.ardmediathek.de/ard/search/'+search_string)

def getPage(url,page=1):
	return listing.listRSS(url,page)

def getVideosJson(url,page = '1'):
	return libArdJsonParser.parseVideos(url)

def getVideosXml(videoId):
	return listing.getVideosXml(videoId)

def parser(data):
	return rssparser.parser(data)

translation = libMediathek.getTranslation

channels = [
	('ARD-alpha','5868'),
	('BR','2224'),
	('Das Erste','208'),
	('HR','5884'),
	('MDR','5882'),
	('MDR / Sachsen','1386804'),
	('MDR / Sachsen-Anhalt','1386898'),
	('MDR / Thüringen','1386988'),
	('NDR / Fernsehen','5906'),
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
	#l.append({'name':translation(31030), 'mode':'libArdListVideosSinglePage', 'url':'http://www.ardmediathek.de/tv/Neueste-Videos/mehr?documentId=21282466&rss=true', '_type':'dir'})
	#l.append({'name':translation(31031), 'mode':'libArdListVideosSinglePage', 'url':'http://www.ardmediathek.de/tv/Meistabgerufene-Videos/mehr?documentId=21282514&m23644322=quelle.tv&rss=true', '_type':'dir'})
	#l.append({'name':translation(31032), 'mode':'libArdListLetters', '_type':'dir'})
	l.append({'name':translation(31032), 'mode':'libArdListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Rubriken/mehr?documentId=21282550&json', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Themen/mehr?documentId=21301810&json', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListVideos():
	return getVideosJson(params['url'])#,page)

def libArdListVideosSinglePage():
	page = params.get('page','1')
	items,nextPage = libardlisting.listRSS(params['url'],page)
	return items

def libArdListLetters():
	return libMediathek.populateDirAZ('libArdListShows',[])

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

def libArdListSearch():
	search_string = libMediathek.getSearchString(do_quote=False)
	return getSearch(search_string) if search_string else None

def getMetadata(result):
	if result:
		metadata = {}
		for key in ['name', 'plot', 'thumb']:
			value = params.get(key, None)
			if value:
				metadata[key] = value
		if metadata:
			result['metadata'] = metadata
	return result

def libArdPlayClassic():
	result = libardplayer.getVideoUrlClassic(videoID = params['documentId'])
	result = getMetadata(result)
	return result

def libArdPlayNeu():
	result = libArdJsonParser.getVideoUrlNeu(params['url'])
	result = getMetadata(result)
	return result

def list():
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libArdListMain')
	if mode in ['libArdPlayClassic', 'libArdPlayNeu']:
		media = modes.get(mode)()
		if media is None:
			return False
		else:
			libMediathek.play(media)
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()
	return True

modes = {
	'libArdListMain':libArdListMain,
	'libArdListVideos':libArdListVideos,
	'libArdListVideosSinglePage':libArdListVideosSinglePage,
	'libArdListLetters':libArdListLetters,
	'libArdListShows':libArdListShows,
	'libArdListChannel':libArdListChannel,
	'libArdListChannelDate':libArdListChannelDate,
	'libArdListChannelDateVideos':libArdListChannelDateVideos,
	'libArdListSearch':libArdListSearch,
	'libArdPlayClassic':libArdPlayClassic,
	'libArdPlayNeu':libArdPlayNeu,
}