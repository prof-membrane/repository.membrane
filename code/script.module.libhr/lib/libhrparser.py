# -*- coding: utf-8 -*-
import xbmc
import json
import libmediathek3 as libMediathek
import re
from operator import itemgetter
#import xml.etree.ElementTree as ET

base = 'http://www.hr-online.de'
	
def getDate(url):
	response = libMediathek.getUrl(url)
	section = re.compile('<section class="c-teaserGroup -s100">(.+?)</section>', re.DOTALL).findall(response)[0]
	articles = re.compile('<article.+?>(.+?)</article>', re.DOTALL).findall(section)
	l = []
	for article in articles:
		#TODO: date
		d = {}
		d['url'] = re.compile('<a href="(.+?)"', re.DOTALL).findall(article)[0]
		d['_name'] = re.compile('<span class="c-teaser__headline text__headline">(.+?)</span>', re.DOTALL).findall(article)[0].strip()
		d['_thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(article)[0]
		d['_type'] = 'video'
		d['mode'] = 'libHrPlay'
		l.append(d)
	return l
	
def getEpisodes(showid):
	response = libMediathek.getUrl('http://hr-fernsehen.de/'+showid+'.html')
	top = re.compile('<div class="c-teaser__lead">(.+?)</article>', re.DOTALL).findall(response)
	l = []
	for item in top:
		if 'zum Video' in item:
			d = {}
			d['url'] = re.compile('<a href="(.+?)"', re.DOTALL).findall(item)[0]
			d['_name'] = re.compile('<span class="c-teaser__underline text__underline">(.+?)</span>', re.DOTALL).findall(item)[0].strip()
			d['_thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(item)[0]
			d['_type'] = 'video'
			d['mode'] = 'libHrPlay'
			l.append(d)
	#TODO: Bottom
	return l
	
def getVideo(url):
	response = libMediathek.getUrl(url)
	
	url = re.compile('<source type="video/mp4" src="(.+?)"', re.DOTALL).findall(response)[0].replace('https://hr-a.akamaihd.net/','http://hrardmediathek-vh.akamaihd.net/i/').replace('512x288-25p-500kbit.mp4',',640x360-25p-1000,1280x720-50p-5000,960x540-50p-1800,512x288-25p-500,480x270-25p-250,320x180-12p-125,kbit.mp4.csmil/master.m3u8')
	#https://hr-a.akamaihd.net/video/as/giraffe/2018_02/hrLogo_180217181425_0195838_512x288-25p-500kbit.mp4
	#http://hrardmediathek-vh.akamaihd.net/i/video/as/allgemein/2018_03/hrLogo_180302141016_0191318_,640x360-25p-1000,1280x720-50p-5000,960x540-50p-1800,512x288-25p-500,480x270-25p-250,320x180-12p-125,kbit.mp4.csmil/master.m3u8
	#http://hrardmediathek-vh.akamaihd.net/  video/as/giraffe/2018_02/hrLogo_180224171205_0195884_,640x360-25p-1000,1280x720-50p-5000,960x540-50p-1800,512x288-25p-500,480x270-25p-250,320x180-12p-125,kbit.mp4.csmil/master.m3u8
	d = {}
	d['media'] = []
	d['media'].append({'url':url, 'type': 'video', 'stream':'HLS'})
	return d