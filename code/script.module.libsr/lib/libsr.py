# -*- coding: utf-8 -*-
import sys
import urllib
import libsrjsonparser as libSrJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation

#http://hbbtv.sr-mediathek.de/inc/SearchJSON.php

def libSrListMain():
	l = []
	l.append({'name':translation(31030), 'mode':'libSrListVideos', 'urlargs':'{}', '_type':'dir'})
	l.append({'name':translation(31032), 'mode':'libSrListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libSrListDate', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libSrListTopics', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libSrSearch', '_type':'dir'})
	return l
	
def libSrListDate():
	return libMediathek.populateDirDate('libSrListDateVideos')

def libSrListDateVideos():
	return libSrJsonParser.getDate(params['datum'])
	
def libSrListShows():
	libMediathek.sortAZ()
	return libSrJsonParser.getShows()
	
def libSrListTopics():
	libMediathek.sortAZ()
	return libSrJsonParser.getTopics()
	
def libSrListTopic():
	return libSrJsonParser.getTopic(params['t_kurz'])
		
def libSrListVideos():
	#libMediathek.log(str(params))
	return libSrJsonParser.getSearch(params['urlargs'])
	
def libSrSearch():
	search_string = libMediathek.getSearchString()
	return libSrListSearch(search_string) if search_string else None

def libSrListSearch(searchString=False):
	if not searchString:
		searchString = params['searchString']
	return libSrJsonParser.getSearch('{"suche":"'+searchString+'"}')
	
def libSrPlay():
	return libSrJsonParser.getVideoUrl(params['id'])

def list():	
	modes = {
	'libSrListMain': libSrListMain,
	'libSrListShows': libSrListShows,
	'libSrListVideos': libSrListVideos,
	'libSrListDate': libSrListDate,
	'libSrListDateVideos': libSrListDateVideos,
	'libSrListTopics': libSrListTopics,
	'libSrListTopic': libSrListTopic,
	'libSrPlay': libSrPlay,
	'libSrSearch': libSrSearch,
	'libSrListSearch': libSrListSearch,
	
	}
	global params
	params = libMediathek.get_params()
	global pluginhandle
	pluginhandle = int(sys.argv[1])
	mode = params.get('mode','libSrListMain')
	if mode == 'libSrPlay':
		libMediathek.play(libSrPlay())
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()	
