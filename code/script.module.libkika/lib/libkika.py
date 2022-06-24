# -*- coding: utf-8 -*-
import sys
import urllib
import libkikajsonparser as libKikaJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
params = libMediathek.get_params() 

def list():
	return libMediathek.list(modes, 'libKikaListMain', 'libKikaPlay')

def libKikaListMain():
	l = []
	l.append({'name':translation(31030), 'mode':'libKikaListVideos', '_type':'dir', 'uri':'/api/videos?limit=20&orderBy=date&orderDirection=DESC'})
	l.append({'name':translation(31032), 'mode':'libKikaListShows', '_type':'dir'})
	#l.append({'name':translation(31033), 'mode':'libKikaListDate', '_type':'dir'})
	#l.append({'name':translation(31039), 'mode':'libKikaSearch', '_type':'dir'})
	return l

#def libKikaListDate():
	#return libMediathek.populateDirDate('libKikaListDateVideos')

#def libKikaListDateVideos():
#	return libKikaJsonParser.getVideos('http://itv.mit-xperts.com/kikamediathek/kika/api.php/videos/hbbtv/suche/hbbtv-search-100-hbbtv.json?day=-'+params['datum'],type='date')

def libKikaListShows():
	libMediathek.sortAZ()
	return libKikaJsonParser.getBrands()

def libKikaListVideos():
	return libKikaJsonParser.getVideos(params['uri'])

def libKikaPlay():
	result = libKikaJsonParser.getVideoUrl(params['uri'])
	result = libMediathek.getMetadata(result)
	return result

#def libKikaSearch():
#	search_string = libMediathek.getSearchString()
#	return libKikaJsonParser.getVideos('http://itv.mit-xperts.com/kikamediathek/kika/api.php/videos/hbbtv/suche/hbbtv-search-100-hbbtv.json?searchText='+search_string)

modes = {
	'libKikaListMain':  ( libKikaListMain, 'videos' ),
	'libKikaListShows': ( libKikaListShows, 'videos' ),
	'libKikaListVideos':( libKikaListVideos, 'movies' ),
	'libKikaPlay':      ( libKikaPlay, None ),
}
