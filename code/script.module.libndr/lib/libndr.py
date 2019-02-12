# -*- coding: utf-8 -*-
import sys
import urllib
import libndrparser as libNdrParser
import libndrjsonparser as libNdrJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
ignoreLetters=['#']



def libNdrListMain():
	l = []
	l.append({'_name':translation(31032), 'mode':'libNdrListDir', '_type':'dir'})
	l.append({'_name':translation(31033), 'mode':'libNdrListDate', '_type':'dir'})
	l.append({'_name':translation(31039), 'mode':'libNdrSearch', '_type':'dir'})
	return l

def libNdrListDir():
	return libNdrParser.parseShows()
	
def libNdrListVideos():
	return libNdrParser.parseVideos(params['url'])
	
def libNdrListDate():
	return libMediathek.populateDirDate('libNdrListDateVideos')
		
def libNdrListDateVideos():
	return libNdrParser.getDate(params['yyyymmdd'])
	

def libNdrSearch():
	search_string = libMediathek.getSearchString()
	return libNdrParser.getSearch(search_string) if search_string else None
	
def libNdrPlay():
	return libNdrJsonParser.getVideo(params['id'])
		
def libNdrListLetters():
	libMediathek.populateDirAZ('libNdrListShows',ignoreLetters)
	return []
	
def libNdrListShows():
	#return libNdrParser.parseShows(params['name'])
	return libNdrParser.parseShows()
	

def list():	
	modes = {
	'libNdrListMain': libNdrListMain,
	'libNdrListDir': libNdrListDir,
	'libNdrListVideos': libNdrListVideos,
	'libNdrListDate': libNdrListDate,
	'libNdrListDateVideos': libNdrListDateVideos,
	
	'libNdrSearch': libNdrSearch,
	
	'libNdrPlay': libNdrPlay,
	
	
	'libNdrListLetters': libNdrListLetters,
	'libNdrListShows': libNdrListShows,
	#'libNdrListDateChannels': libNdrListDateChannels,
	}
	
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libNdrListMain')
	if mode == 'libNdrPlay':
		libMediathek.play(libNdrPlay())
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()
