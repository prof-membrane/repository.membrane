# -*- coding: utf-8 -*-
import sys
import libartejsonparser as libArteJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'libArteListMain', 'libArtePlay')

def libArteListMain():
	l = []
	l.append({'_name': translation(31031), 'mode': 'libArteListVideos',	'_type': 'dir', 'url':'/zones/listing_MOST_VIEWED?limit=20'}) # Meistgesehen
	l.append({'_name': translation(31032), 'mode': 'libArteListMagazines',	'_type': 'dir'}) # Sendungen A-Z
	l.append({'_name': translation(31033), 'mode': 'libArteListDate',	'_type': 'dir'}) # Die Woche
	l.append({'_name': translation(31039), 'mode': 'libArteListSearch', '_type': 'dir'}) # Suche
	return l

def libArteListCollection():
	return libArteJsonParser.getCollection(params['url'])

def libArteListVideos():
	return libArteJsonParser.getVideos(params['url'])

def libArteListMagazines():
	return libArteJsonParser.getMagazines()

def libArteListDate():
	return libMediathek.populateDirDate('libArteListDateVideos')

def libArteListDateVideos():
	return libArteJsonParser.getDate(params['yyyymmdd'])

def libArteListSearch():
	search_string = libMediathek.getSearchString()
	return libArteJsonParser.getSearch(search_string) if search_string else None

def libArtePlay():
	result = libArteJsonParser.getVideoUrl(params['url'])
	result = libMediathek.getMetadata(result)
	return result

modes = {
	'libArteListMain': libArteListMain,
	'libArteListCollection':libArteListCollection,
	'libArteListVideos': libArteListVideos,
	'libArteListMagazines': libArteListMagazines,
	'libArteListDate': libArteListDate,
	'libArteListDateVideos': libArteListDateVideos,
	'libArteListSearch': libArteListSearch,
	'libArtePlay': libArtePlay,
}

