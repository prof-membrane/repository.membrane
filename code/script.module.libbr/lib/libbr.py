# -*- coding: utf-8 -*-
import sys
import urllib
import libbrjsonparser as libBrJsonParser
import libmediathek3 as libMediathek
from datetime import date, timedelta

translation = libMediathek.getTranslation

def getDate(date,channel='BR'):
	return libBrJsonParser.parseDate(date,channel)
def search(searchString):
	return libBrJsonParser.search(searchString)
def getVideoUrl(url):
	return libBrJsonParser.parseVideo(url)
"""
def play(dict):
	url,sub = getVideoUrl(dict["url"])
	#listitem = xbmcgui.ListItem(label=video["name"],thumbnailImage=video["thumb"],path=url)
	#listitem = xbmcgui.ListItem(label=dict["name"],path=url)
	listitem = xbmcgui.ListItem(label='TODO',path=url)
	xbmc.Player().play(url, listitem)	
"""

	
def libBrListMain():
	#libBrJsonParser.getIntrospection()
	l = []
	l.append({'name':translation(31031), 'mode':'libBrListNew', '_type':'dir'})
	l.append({'name':translation(31032), 'mode':'libBrListSeries', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libBrListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libBrListBoards', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libBrListCategories', '_type':'dir'})
	#l.append({'name':'Genres', 'mode':'libBrListGenres', '_type':'dir'})
	#l.append({'name':'#sections', 'mode':'libBrListSections', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libBrSearch', '_type':'dir'})
	return l
	
	
	
def libBrListNew():
	return libBrJsonParser.parseNew()
		
		

def libBrListSeries():
	libMediathek.sortAZ()
	return libBrJsonParser.parseSeries()	
def libBrListEpisodes():
	return libBrJsonParser.parseEpisodes(params['id'])

def libBrListBoards():
	return libBrJsonParser.parseBoards()	
def libBrListBoard():
	return libBrJsonParser.parseBoard(params['boardId'])

def libBrListCategories():
	return libBrJsonParser.parseCategories()
def libBrListCategorie():
	return libBrJsonParser.parseCategorie(params['id'])

#cat
def libBrListGenres():
	return libBrJsonParser.parseGenres()
def libBrListGenre():
	return libBrJsonParser.parseGenre(params['id'])
	
def libBrListSections():
	libMediathek.sortAZ()
	return libBrJsonParser.parseSections()
def libBrListSection():
	return libBrJsonParser.parseSection(params['id'])

def libBrListVideos2():
	return libBrJsonParser.parseLinks(params['url'])

	
def libBrListChannel():
	l = []
	l.append({'_name':'ARD-Alpha', 'mode':'libBrListChannelDate','channel':'ARD_alpha', '_type':'dir'})
	l.append({'_name':'BR', 'mode':'libBrListChannelDate','channel':'BR_Fernsehen', '_type':'dir'})
	return l

def libBrListChannelDate():
	return libMediathek.populateDirDate('libBrListChannelDateVideos',params['channel'])
	
def libBrListChannelDateVideos():
	#xdatum = date.today() - timedelta(int(params['datum']))
	return libBrJsonParser.parseDate(params['yyyymmdd'],params['channel'])#params['datum'] =yyyy-mm-dd
	#return libBrJsonParser.parseDate(datum.strftime('%Y-%m-%d'),params['channel'])#params['datum'] =yyyy-mm-dd
	
def libBrSearch():
	search_string = libMediathek.getSearchString()
	return libBrJsonParser.parseSearch(search_string) if search_string else None
	#return libBrListSearch(search_string)

def libBrListSearch(searchString=False):
	if not searchString:
		searchString = params['searchString']
	return search(searchString)
	
def libBrPlay():
	return libBrJsonParser.parseVideo(params['id'])
def libBrPlayOld():
	return libBrJsonParser.parseVideoOld(params['url'])
	
	
def list():	
	modes = {
	'libBrListMain': libBrListMain,
	'libBrListNew': libBrListNew,
	'libBrListSeries': libBrListSeries,
	'libBrListEpisodes': libBrListEpisodes,
	'libBrListBoards': libBrListBoards,
	'libBrListBoard': libBrListBoard,
	'libBrListCategories': libBrListCategories,
	'libBrListCategorie': libBrListCategorie,
	'libBrListGenres': libBrListGenres,
	'libBrListGenre': libBrListGenre,
	'libBrListSections': libBrListSections,
	'libBrListSection': libBrListSection,
	'libBrListVideos2': libBrListVideos2,
	'libBrListChannel': libBrListChannel,
	'libBrListChannelDate': libBrListChannelDate,
	'libBrListChannelDateVideos': libBrListChannelDateVideos,
	'libBrSearch': libBrSearch,
	'libBrListSearch': libBrListSearch,
	'libBrPlay': libBrPlay,
	'libBrPlayOld': libBrPlayOld
	}
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libBrListMain')
	if mode == 'libBrPlay':
		libMediathek.play(libBrPlay())
	elif mode == 'libBrPlayOld':
		libMediathek.play(libBrPlayOld())
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()	
	