# -*- coding: utf-8 -*-
import sys
import urllib
import libswrparser as libSwrParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation

def libSwrListMain():
	libMediathek.searchWorkaroundRemove()
	l = []
	l.append({'_name':translation(31030), 'mode':'libSwrListVideos', 'url':'http://swrmediathek.de/app-2/svp.html', '_type':'dir'})
	l.append({'_name':translation(31031), 'mode':'libSwrListVideos', 'url':'http://swrmediathek.de/app-2/index.html', '_type':'dir'})
	l.append({'_name':translation(31032), 'mode':'libSwrListDir', 'url':'http://swrmediathek.de/app-2/tv.html', '_type':'dir'})
	l.append({'_name':translation(31033), 'mode':'libSwrListDate', '_type':'dir'})
	l.append({'_name':translation(31034), 'mode':'libSwrListDir', 'url':'http://swrmediathek.de/app-2/rubriken.html', '_type':'dir'})
	l.append({'_name':translation(31035), 'mode':'libSwrListDir', 'url':'http://swrmediathek.de/app-2/themen.html', '_type':'dir'})
	l.append({'_name':translation(31039), 'mode':'libSwrSearch', '_type':'dir'})
	return l

def libSwrListDir():
	return libSwrParser.getList(params['url'],'dir','libSwrListVideos')
	
def libSwrListDate():
	return libMediathek.populateDirDate('libSwrListDateVideos')
		
def libSwrListDateVideos():
	return libSwrParser.getDate(params['datum'],'date','libSwrPlay')
	
def libSwrListVideos():
	return libSwrParser.getList(params['url'],'video','libSwrPlay')

def libSwrSearch():
	search_string = libMediathek.getSearchString()
	return libSwrParser.getList('http://swrmediathek.de/app-2/suche/'+search_string,'video','libSwrPlay') if search_string else None  

def libSwrPlay():
	return libSwrParser.getVideo(params['url'])
	
def play(dict):
	return getVideoUrl(dict["url"])
	
def libSwrListLetters():
	libMediathek.populateDirAZ('libSwrListShows',ignore=['#'])
	return []
	
def libSwrListShows():
	return libSwrParser.parseShows()
	

def list():	
	modes = {
	'libSwrListMain': libSwrListMain,
	'libSwrListDir': libSwrListDir,
	'libSwrListDate': libSwrListDate,
	'libSwrListDateVideos': libSwrListDateVideos,
	
	'libSwrListVideos': libSwrListVideos,
	'libSwrSearch': libSwrSearch,
	
	'libSwrPlay': libSwrPlay,
	
	
	'libSwrListLetters': libSwrListLetters,
	'libSwrListShows': libSwrListShows,
	#'libSwrListDateChannels': libSwrListDateChannels,
	}
	
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libSwrListMain')
	if mode == 'libSwrPlay':
		libMediathek.play(libSwrPlay())
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()	