# -*- coding: utf-8 -*-
import sys
import libbrjsonparser as libBrJsonParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'libBrListMain', 'libBrPlay', 'libBrPlayOld')

def getDate(date,channel='BR'):
	return libBrJsonParser.parseDate(date,channel)

def getVideoUrl(url):
	return libBrJsonParser.parseVideo(url)

def libBrListMain():
	l = []
	l.append({'name':translation(31030), 'mode':'libBrListNew', '_type':'dir'})
	l.append({'name':translation(31032), 'mode':'libBrListSeries', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libBrListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libBrListBoards', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libBrListCategories', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libBrListSearch', '_type':'dir'})
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

def libBrListGenres():
	return libBrJsonParser.parseGenres()
def libBrListGenre():
	return libBrJsonParser.parseGenre(params['id'])

def libBrListSections():
	libMediathek.sortAZ()
	return libBrJsonParser.parseSections()
def libBrListSection():
	return libBrJsonParser.parseSection(params['id'])

def libBrListChannel():
	l = []
	l.append({'_name':'BR', 'mode':'libBrListChannelDate','channel':'BR_Fernsehen', '_type':'dir'})
	l.append({'_name':'ARD-Alpha', 'mode':'libBrListChannelDate','channel':'ARD_alpha', '_type':'dir'})
	return l

def libBrListChannelDate():
	return libMediathek.populateDirDate('libBrListChannelDateVideos',params['channel'])

def libBrListChannelDateVideos():
	return libBrJsonParser.parseDate(params['yyyymmdd'],params['channel'])

def libBrListSearch():
	search_string = libMediathek.getSearchString()
	return libBrJsonParser.parseSearch(search_string) if search_string else None

def libBrPlay():
	result = libBrJsonParser.parseVideo(params['id'])
	result = libMediathek.getMetadata(result)
	return result

def libBrPlayOld():
	result = libBrJsonParser.parseVideoOld(params['url'])
	result = libMediathek.getMetadata(result)
	return result

modes = {
	'libBrListMain':              ( libBrListMain, 'videos' ),
	'libBrListNew':               ( libBrListNew, 'movies' ),
	'libBrListSeries':            ( libBrListSeries, 'videos' ),
	'libBrListEpisodes':          ( libBrListEpisodes, 'movies' ),
	'libBrListBoards':            ( libBrListBoards, 'videos' ),
	'libBrListBoard':             ( libBrListBoard, 'movies' ),
	'libBrListCategories':        ( libBrListCategories, 'videos' ),
	'libBrListCategorie':         ( libBrListCategorie, 'movies' ),
	'libBrListGenres':            ( libBrListGenres, 'videos' ),
	'libBrListGenre':             ( libBrListGenre, 'movies' ),
	'libBrListSections':          ( libBrListSections, 'videos' ),
	'libBrListSection':	          ( libBrListSection, 'movies' ),
	'libBrListChannel':           ( libBrListChannel, 'videos' ),
	'libBrListChannelDate':       ( libBrListChannelDate, 'videos' ),
	'libBrListChannelDateVideos': ( libBrListChannelDateVideos, 'movies' ),
	'libBrListSearch':            ( libBrListSearch, 'movies' ),
	'libBrPlay':                  ( libBrPlay, None ),
	'libBrPlayOld':               ( libBrPlayOld, None ),
}
