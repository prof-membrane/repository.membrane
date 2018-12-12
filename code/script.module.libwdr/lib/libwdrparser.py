# -*- coding: utf-8 -*-
import json
import re
#import dateutil.parser
import libmediathek3 as libMediathek
base = 'http://www1.wdr.de'

def parseShows(url):
	response = libMediathek.getUrl(url)
	uls = re.compile('<ul  class="list">(.+?)</ul>', re.DOTALL).findall(response)
	l = []
	for ul in uls:
		lis = re.compile('<li >(.+?)</li>', re.DOTALL).findall(ul)
		for li in lis:
			d = {}
			uri = re.compile('href="(.+?)"', re.DOTALL).findall(li)[0]
			if uri != 'http://www.wdrmaus.de/':
				d['url'] = base + uri
				d['_name'] = re.compile('<span>(.+?)</span>', re.DOTALL).findall(li)[0]
				try:
					thumb = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(li)[0].replace('~_v-ARDKleinerTeaser.jpg','~_v-original.jpg').replace('http//www','http://www')
					if thumb.startswith('http'):
						d['_thumb'] = thumb
					else:
						d['_thumb'] = base + thumb
				except: pass
				d['_channel'] = 'WDR'
				d['_type'] = 'dir'
				d['mode'] = 'libWdrListVideos'
				
				l.append(d)
		
	return l
	
def parseVideos(url):
	response = libMediathek.getUrl(url)
	typeA = re.compile('<div class="box".+?<a(.+?)>(.+?)</a>.+?<a(.+?)>(.+?)</a>', re.DOTALL).findall(response)
	l = []
	for href,show,href2,stuff in typeA:
		if '<div class="media mediaA video">' in stuff:
			d = {}
			d['url'] = base + re.compile('href="(.+?)"', re.DOTALL).findall(href2)[0]
			if '<h4' in stuff:
				d['_name'] = re.compile('<h4.+?>.+?<span class="hidden">Video:</span>(.+?)<', re.DOTALL).findall(stuff)[0].strip()
			else:
				d['_name'] = show.strip()
			if '<img' in stuff:
				d['_thumb'] = base + re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(stuff)[0]
			d['_plot'] = re.compile('<p class="teasertext">(.+?)<', re.DOTALL).findall(stuff)[0]
			#TODO duration, ut
			d['_type'] = 'video'
			d['mode'] = 'libWdrPlay'
			
			l.append(d)
	return l
	
def parseVideo(url,signLang=False):
	response = libMediathek.getUrl(url)
	#libMediathek.log(response)
	j = json.loads(re.compile('<a href="javascript:void\(0\);" class="mediaLink video" data-extension=\'(.+?)\'', re.DOTALL).findall(response)[0])
	url = j['mediaObj']['url']
	return parseVideoJs(url,signLang)
	
def parseVideoJs(url,signLang=False):
	response = libMediathek.getUrl(url)
	import json
	j = json.loads(response[38:-2])
	
	videos = []
	subUrlTtml = False
	for type in j['mediaResource']:
		if type == 'dflt' or type == 'alt':
			if signLang and 'slVideoURL' in j['mediaResource'][type]:
				videos.append(j['mediaResource'][type]['slVideoURL'])
			else:
				videos.append(j['mediaResource'][type]['videoURL'])
		elif type == 'captionURL':
			subUrlTtml = j['mediaResource']['captionURL']
		elif type == 'captionsHash':
			if 'xml' in j['mediaResource']['captionsHash']:
				subUrlTtml = j['mediaResource']['captionsHash']['xml']
			if 'vtt' in j['mediaResource']['captionsHash']:
				subUrlVtt = j['mediaResource']['captionsHash']['vtt']
			if 'srt' in j['mediaResource']['captionsHash']:
				subUrlSrt = j['mediaResource']['captionsHash']['srt']
	video = False
	for vid in videos:
		if vid.startswith('//'):
			vid = 'http:' + vid
		if vid.endswith('.m3u8'):
			video = vid
		elif vid.endswith('.f4m') and (not video or video.endswith('.mp4')):
			video = vid.replace('manifest.f4m','master.m3u8').replace('adaptiv.wdr.de/z/','adaptiv.wdr.de/i/')
		elif vid.endswith('.mp4') and not video:
			video = vid
	d = {}
	d['media'] = []
	d['media'].append({'url':video, 'type': 'video', 'stream':'mp4'})
	if subUrlTtml:
		if subUrlTtml.startswith('//'):
			subUrlTtml = 'http:' + subUrlTtml
		d['subtitle'] = []
		d['subtitle'].append({'url':subUrlTtml, 'type': 'ttml', 'lang':'de'})
	return d
	
def startTimeToInt(s):
	HH,MM,SS = s.split(":")
	return int(HH) * 60 + int(MM)