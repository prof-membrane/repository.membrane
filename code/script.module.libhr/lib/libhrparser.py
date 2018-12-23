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
			d['_name'] = re.compile('<span class="c-teaser__headline text__headline">(.+?)</span>', re.DOTALL).findall(item)[0].strip()  
			underlines = re.compile('<span class="c-teaser__underline text__underline">(.+?)</span>', re.DOTALL).findall(item)
			if (len(underlines) > 0):
				d['_name'] = d['_name'] + ' | ' + underlines[0].strip()
			d['_thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(item)[0]
			d['_type'] = 'video'
			d['mode'] = 'libHrPlay'
			l.append(d)
	#TODO: Bottom
	return l
	
def getVideo(url):
	d = {}
	d['media'] = []
	response = libMediathek.getUrl(url)
	video_str = re.compile("<div.+?data-hr-video-(player|adaptive)='(.+?)'.+?>", re.DOTALL).findall(response)[0]
	if (len(video_str) == 2):
		json_str = video_str[1].replace("&quot;", "\"")
		j = json.loads(json_str)
		if video_str[0] == 'adaptive':
			url = j['adaptiveStreamingUrl']
			d['media'].append({'url':url, 'type': 'video', 'stream':'HLS'})
		else: # video_str[0] == 'player'
			metadata = j['mediaMetadata']
			agf = metadata['agf'] 
			url = agf['uurl']
			if url.startswith('//'):
				url = 'http:' + url
			elif not (url.startswith('http://') or url.startswith('https://')):
				url = 'http://hr-a.akamaihd.net/video/' + url
			d['media'].append({'url':url, 'type': 'video', 'stream':'mp4'})
	return d