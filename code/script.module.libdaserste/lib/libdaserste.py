# -*- coding: utf-8 -*-
import sys
import urllib
import libdaserstejsonparser as libDasErsteJsonParser
import libmediathek3 as libMediathek
from datetime import date, timedelta

translation = libMediathek.getTranslation
#http://www.daserste.de/dasersteapp/app/daserste/mehr/index.json
#http://www.daserste.de/dasersteapp/app/index~categories.json
#http://www.daserste.de/dasersteapp/app/index~series.json
#http://www.daserste.de/dasersteapp/app/index~series_plain-false.json
#http://www.daserste.de/dasersteapp/app/index~program_pd20161010.json
#http://www.daserste.de/dasersteapp/app/daserste/start/index.json

#http://www.daserste.de/dasersteapp/app/index~categories_pageSize-20_catVideo-Film.json
#http://www.daserste.de/dasersteapp/app/index~categories_series-akteex.json
#http://www.daserste.de/dasersteapp/app/index~categories_series-tatort.json
#http://www.daserste.de/dasersteapp/app/index~series_serial-akteex_types-sendung,sendebeitrag_pageNumber-0.json
#types: making%5BU%5Dof,support,interview,trailer,bestof,precap,recap

#http://www.daserste.de/dasersteapp/wer-weiss-denn-sowas-folge-75-100~full.json
#http://www.daserste.de/dasersteapp/die-realistin-folge-60-100~full.json
#http://www.daserste.de/dasersteapp/Folge-60-die-realistin-100~full.json

	
def libDasErsteListMain():
	l = []
	l.append({'name':translation(31032), 'mode':'libDasErsteListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libDasErsteListDate', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libDasErsteListCategories', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libDasErsteSearch', '_type':'dir'})
	return l
	
def libDasErsteListShows():
	return libDasErsteJsonParser.getAZ()

def libDasErsteListCategories():
	return libDasErsteJsonParser.getCategories()
	
def libDasErsteListVideos():
	return libDasErsteJsonParser.getVideos(params['url'])
	
def libDasErsteListDate():
	return libMediathek.populateDirDate('libDasErsteListDateVideos')
	
def libDasErsteListDateVideos():
	datum = date.today() - timedelta(int(params['datum']))
	return libDasErsteJsonParser.getDate(datum.strftime('%Y%m%d'))
	
def libDasErsteSearch():
	search_string = libMediathek.getSearchString()
	return libDasErsteListSearch(search_string) if search_string else None

def libDasErsteListSearch(searchString=False):
	if not searchString:
		searchString = params['searchString']
	return libDasErsteJsonParser.getSearch(searchString)
	
def libDasErstePlay():
	vid = libDasErsteJsonParser.getVideo(params['url'])
	libMediathek.log(str(vid))
	return vid
	

	
def list():	
	modes = {
	'libDasErsteListMain':		libDasErsteListMain,
	'libDasErsteListShows':		libDasErsteListShows,
	'libDasErsteListCategories':libDasErsteListCategories,
	'libDasErsteListVideos':	libDasErsteListVideos,
	'libDasErsteListDate':		libDasErsteListDate,
	'libDasErsteListDateVideos':libDasErsteListDateVideos,
	'libDasErsteSearch':		libDasErsteSearch,
	'libDasErsteListSearch':	libDasErsteListSearch,
	'libDasErstePlay':			libDasErstePlay,
	}
	views = {
	'libDasErsteListShows': 'shows',
	'libDasErsteListVideos': 'videos',
	'libDasErsteListDate': 'videos',
	'libDasErsteListDateVideos': 'videos',
	'libDasErsteListSearch': 'videos'
	}
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libDasErsteListMain')
	if mode == 'libDasErstePlay':
		libMediathek.play(libDasErstePlay())
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()	