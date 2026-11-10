#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import date, timedelta
import lib3sathtmlparser as lib3satHtmlParser
import libmediathek3 as libMediathek

params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'lib3satHtmlListMain', 'lib3satHtmlPlay')


def lib3satHtmlListMain():
	l = []
	translation = libMediathek.getTranslation
	l.append({'name':translation(31032), 'mode':'lib3satHtmlListLetters', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'lib3satHtmlListDate', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'lib3satHtmlListSearch', '_type':'dir'})
	return l


def lib3satHtmlListLetters():
	# URL z.B.: https://www.3sat.de/sendungen-a-z?group=a
	mode = 'lib3satHtmlListShows'
	l = libMediathek.populateDirAZ(mode, ['#'])
	d = {}
	d['mode'] = mode
	d['name'] = '0-9'
	d['_type'] = 'dir'
	l.append(d)
	return l


def lib3satHtmlListDate():
	# URL z.B.: https://www.3sat.de/programm?airtimeDate=2019-06-21
	l = libMediathek.populateDirDate('lib3satHtmlListDateVideos')
	return l


def lib3satHtmlListDateVideos():
	if 'datum' in params:
		day = date.today() - timedelta(int(params['datum']))
		yyyy_mm_dd = day.strftime('%Y-%m-%d')
	else:
		ddmmyyyy = libMediathek.dialogDate()
		yyyy_mm_dd = ddmmyyyy[4:8] + '-' + ddmmyyyy[0:2] + '-' + ddmmyyyy[2:4]
	l = lib3satHtmlParser.getDate(yyyy_mm_dd)
	return l


def lib3satHtmlListShows():
	libMediathek.sortAZ()
	url = params.get('url', None)
	if not url:
		url = lib3satHtmlParser.base + '/sendungen-a-z?group=' + params['name'].lower()
	l = lib3satHtmlParser.getAZ(url)
	return l


def lib3satHtmlListSearch():
	search_string = libMediathek.getSearchString()
	if search_string:
		url = lib3satHtmlParser.base + '/suche?q=' +search_string
		l = lib3satHtmlParser.getAZ(url)
		return l
	else:
		return None


def lib3satHtmlPlay(url = None):
	result = lib3satHtmlParser.lib3satHtmlPlay(url)
	result = libMediathek.getMetadata(result)
	return result


modes = {
	'lib3satHtmlListMain':      ( lib3satHtmlListMain, 'videos' ),
	'lib3satHtmlListLetters':   ( lib3satHtmlListLetters, 'videos' ),
	'lib3satHtmlListDate':      ( lib3satHtmlListDate, 'videos' ),
	'lib3satHtmlListDateVideos':( lib3satHtmlListDateVideos, 'movies' ),
	'lib3satHtmlListShows':     ( lib3satHtmlListShows, 'movies' ),
	'lib3satHtmlListSearch':    ( lib3satHtmlListSearch, 'movies' ),
	'lib3satHtmlPlay':          ( lib3satHtmlPlay, None ),
}
