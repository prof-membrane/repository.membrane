# -*- coding: utf-8 -*-
import time
import urllib,urllib2,re,random,cookielib,HTMLParser,datetime
import sys
from datetime import date, timedelta

import libardlisting
import libardrssparser
import libardplayer
import libardjsonparser as libArdJsonParser

import libmediathek3 as libMediathek


def getNew():
	return libardlisting.listRSS('http://www.ardmediathek.de/tv/Neueste-Videos/mehr?documentId=21282466&rss=true')

def getMostViewed():
	return libardlisting.listRSS('http://www.ardmediathek.de/tv/Meistabgerufene-Videos/mehr?documentId=21282514&m23644322=quelle.tv&rss=true')

def getSearch(search_string,page=0):
	return libardlisting.listVideos('http://www.ardmediathek.de/suche?searchText='+search_string.replace(" ", "+"))

def getPage(url,page=1):
	return listing.listRSS(url,page)
	
def getVideosJson(url,page = '1'):
	return libArdJsonParser.parseVideos(url)

def getVideosXml(videoId):
	return listing.getVideosXml(videoId)

def parser(data):
	return rssparser.parser(data)
	
translation = libMediathek.getTranslation

channels = {
			  'ARD-alpha':'5868',
			  'BR':'2224',
			  #['Einsfestival', :'673348' ],
			  #['EinsPlus',     :'4178842'],
			  'Das Erste':'208',
			  'HR':'5884',
			  'MDR':'5882',
			  'MDR Thüringen':'1386988',
			  'MDR Sachsen':'1386804',
			  'MDR Sachsen-Anhalt':'1386898',
			  'NDR Fernsehen':'5906',
			  'One':'673348',
			  'RB':'5898',
			  'RBB':'5874',
			  'SR':'5870',
			  'SWR Fernsehen':'5310',
			  'SWR Rheinland-Pfalz':'5872',
			  'SWR Baden-Württemberg':'5904',
			  'tagesschau24':'5878',
			  'WDR':'5902',}
			  
def libArdListMain():
	l = []
	l.append({'name':translation(31030), 'mode':'libArdListVideosSinglePage', 'url':'http://www.ardmediathek.de/tv/Neueste-Videos/mehr?documentId=21282466&rss=true', '_type':'dir'})
	l.append({'name':translation(31031), 'mode':'libArdListVideosSinglePage', 'url':'http://www.ardmediathek.de/tv/Meistabgerufene-Videos/mehr?documentId=21282514&m23644322=quelle.tv&rss=true', '_type':'dir'})
	#l.append({'name':translation(31032), 'mode':'libArdListLetters', '_type':'dir'})
	l.append({'name':translation(31032), 'mode':'libArdListShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannel', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Rubriken/mehr?documentId=21282550&json', '_type':'dir'})
	l.append({'name':translation(31035), 'mode':'libArdListVideos', 'url':'http://www.ardmediathek.de/appdata/servlet/tv/Themen/mehr?documentId=21301810&json', '_type':'dir'})
	#l.append({'name':translation(31039), 'mode':'libArdSearch', '_type':'dir'})
	return l
	
def libArdListVideos():
	return getVideosJson(params['url'])#,page)
		
def libArdListVideosSinglePage():
	page = params.get('page','1')
	items,nextPage = libardlisting.listRSS(params['url'],page)
	return items
	
def libArdListLetters():
	return libMediathek.populateDirAZ('libArdListShows',[])
	
def libArdListShows():
	return libArdJsonParser.parseAZ()
	
def libArdListChannel():
	l = []
	for channel in channels:
		d = {}
		d['_name'] = channel
		d['_type'] = 'dir'
		d['channel'] = channel
		d['mode'] = 'libArdListChannelDate'
		l.append(d)
		
	return l
	
def libArdListChannelDate():
	return libMediathek.populateDirDate('libArdListChannelDateVideos',params['channel'])
	
def libArdListChannelDateVideos():
	url = 'http://appdata.ardmediathek.de/appdata/servlet/tv/sendungVerpasst?json&kanal='+channels[params['channel']]+'&tag='+params['datum']
	return libArdJsonParser.parseDate(url)
	
def libArdSearch():
	search_string = libMediathek.getSearchString()
	libArdListSearch(search_string)
		

def libArdListSearch(searchString):
	list = getSearch(searchString)
	for d in list:
		d['mode'] = 'libArdPlay'
		d['type'] = 'video'
		libMediathek.addEntry(d)
	
def libArdPlay():
	return libardplayer.getVideoUrl(videoID = params['documentId'])

def list():
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libArdListMain')
	if mode == 'libArdPlay':
		libMediathek.play(libArdPlay())
	else:
		l = modes.get(mode,libArdListMain)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()	
	
modes = {
	'libArdListMain':libArdListMain,
	'libArdListVideos':libArdListVideos,
	'libArdListVideosSinglePage':libArdListVideosSinglePage,
	'libArdListLetters':libArdListLetters,
	'libArdListShows':libArdListShows,
	'libArdListChannel':libArdListChannel,
	'libArdListChannelDate':libArdListChannelDate,
	'libArdListChannelDateVideos':libArdListChannelDateVideos,
	'libArdSearch':libArdSearch,
	'libArdListSearch':libArdListSearch,
	'libArdPlay':libArdPlay,
	}