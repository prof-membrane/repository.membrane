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
			headline = re.compile('<span class="c-teaser__headline text__headline">(.+?)</span>', re.DOTALL).findall(item)[0].strip()
			if headline: 
				d['_name'] = headline  + ' | ' + d['_name']  
			d['_thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(item)[0]
			d['_type'] = 'video'
			d['mode'] = 'libHrPlay'
			l.append(d)
	#TODO: Bottom
	return l
	
def getVideo(url):
	response = libMediathek.getUrl(url)
	json_str = re.compile('<div class="videoElement  ar--16x9 js-loadScript" data-hr-video-adaptive=\'(.+?)\'>', re.DOTALL).findall(response)[0]
	json_str = json_str.replace("&quot;", "\"")
	j = json.loads(json_str)
	d = {}
	d['media'] = []
	url = j['adaptiveStreamingUrl']
	if not url:
		url = j['videoUrl']
		d['media'] = [{'url':url, 'type': 'video', 'stream':'mp4'}]
	else:
		if url.endswith('.mp4'):
			d['media'] = [{'url':url, 'type': 'video', 'stream':'mp4'}]
		else:
			d['media'] = [{'url':url, 'type': 'video', 'stream':'HLS'}]
	return d