# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import re
import urllib
import xml.etree.ElementTree as ET
#import dateutil.parser

base = 'http://www.mdr.de'
		
def parseDate(day='0'):
	response = libMediathek.getUrl('http://www.mdr.de/mediathek/fernsehen/index.html')
	url = base + re.compile('<div class="box  cssBroadcastDay.+?href="(.+?)"', re.DOTALL).findall(response)[int(day)]
	
	#url = 'http://www.mdr.de/mediathek/fernsehen/sendung-verpasst--100_date-20161004_inheritancecontext-header_numberofelements-1_zc-65ef7e36.html'
	response = libMediathek.getUrl(url)
	response = response.split('<div class="con">')[-1]
	videos = response.split('<div data-id=')[1:]
	l = []
	for video in videos:
		d = {}
		if "mediathekUrl':''" in video:
			pass
		d['url'] = base + re.compile('href="(.+?)"', re.DOTALL).findall(video)[0].split('_')[0] + '-meta.xml'
		d['_thumb'] = base + re.compile('src="(.+?)"', re.DOTALL).findall(video)[1]
		d['_plot'] = re.compile('<a.+?>(.+?)<', re.DOTALL).findall(video)[2]
		d['_airedtime'] = re.compile('<span class="startTime">(.+?)</span>', re.DOTALL).findall(video)[0]
		sHH,sMM = d['_airedtime'].split(':')
		eHH,eMM = re.compile('<span class="endTime">(.+?)</span>', re.DOTALL).findall(video)[0].split(':')
		d['_duration'] = str((int(eHH) - int(sHH)) * 3600 + (int(eMM) - int(sMM)) * 60)
		d['_name'] = re.compile('<a.+?>(.+?)<', re.DOTALL).findall(video)[1]
		d['mode'] = 'libMdrPlay'
		d['_type'] = 'date'
		l.append(d)
	return l
		
def getSearch(s):
	#https://www.mdr.de/mediathek/suche/mediathek-suche--100-searchResultsDefault.html?start=30&rows=30&page=0&q=wetter&sort=time&filter=&changefilter=&numItems=30
	response = libMediathek.getUrl('https://www.mdr.de/mediathek/suche/mediathek-suche--100-searchResultsDefault.html?start=0&rows=30&page=0&q='+urllib.quote_plus(s)+'&sort=time&filter=&changefilter=&numItems=30')
	
	videos = response.split('<div class="teaser ">')[1:]
	l = []
	for video in videos:
		#libMediathek.log(video)
		d = {}
		d['url'] = base + '/' + re.compile("'playerXml':'(.+?)-avCustom.xml'", re.DOTALL).findall(video)[0].split('/')[-1] + '-meta.xml'
		d['_thumb'] = re.compile('<img class="img ".+?src="(.+?)"', re.DOTALL).findall(video)[0]
		d['_plot'] = re.compile('<p class="teasertext"><.+?>(.+?)<', re.DOTALL).findall(video)[0]
		#d['_airedtime'] = re.compile('<span class="startTime">(.+?)</span>', re.DOTALL).findall(video)[0]
		MM,SS = re.compile('<span class="broadcastDuration">(.+?)</span>', re.DOTALL).findall(video)[0].replace('\n','').split(' ')[0].split(':')
		d['_duration'] = str(int(MM) * 60 + (int(SS)))
		d['_name'] = re.compile('<a.+?>(.+?)<', re.DOTALL).findall(video)[1]
		d['mode'] = 'libMdrPlay'
		d['_type'] = 'video'
		l.append(d)
	return l