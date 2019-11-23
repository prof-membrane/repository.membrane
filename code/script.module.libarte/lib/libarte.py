# -*- coding: utf-8 -*-
import sys
import urllib
import libartejsonparser as libArteJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation


def libArteListMain():
	l = []
	l.append({'_name': translation(31031), 'mode': 'libArteListVideos',	'_type': 'dir', 'url':'/zones/listing_MOST_VIEWED?limit=20'}) # Meistgesehen
	l.append({'_name': translation(31032), 'mode': 'libArteListVideos',	'_type': 'dir', 'url':'/zones/magazines_HOME?limit=99'}) # Sendungen A-Z
	l.append({'_name': translation(31033), 'mode': 'libArteListDate',	'_type': 'dir'}) # Die Woche
	l.append({'_name': translation(31039), 'mode': 'libArteListSearch', '_type': 'dir'}) # Suche
	return l

def libArteListCollection():
	return libArteJsonParser.getCollection(params['url'])

def libArteListVideos():
	return libArteJsonParser.getVideos(params['url'])

def libArteListDate():
	return libMediathek.populateDirDate('libArteListDateVideos')

def libArteListDateVideos():
	return libArteJsonParser.getDate(params['yyyymmdd'])

def libArteListSearch():
	search_string = libMediathek.getSearchString()
	return libArteJsonParser.getSearch(search_string) if search_string else None

def libArtePlay():
	d = libArteJsonParser.getVideoUrl(params['url'])
	if d:
		metadata = {}
		for key in ['name', 'plot']:
			value = params.get(key, None)
			if value:
				metadata[key] = value
		if metadata:
			d['metadata'] = metadata
	return d

def list():
	global params
	params = libMediathek.get_params()
	global pluginhandle
	pluginhandle = int(sys.argv[1])
	mode = params.get('mode','libArteListMain')
	if mode == 'libArtePlay':
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

modes = {
	'libArteListMain': libArteListMain,
	'libArteListCollection':libArteListCollection,
	'libArteListVideos': libArteListVideos,
	'libArteListDate': libArteListDate,
	'libArteListDateVideos': libArteListDateVideos,
	'libArteListSearch': libArteListSearch,
	'libArtePlay': libArtePlay,
}

