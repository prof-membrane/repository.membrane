# -*- coding: utf-8 -*-
import sys
import json
import libmediathek3 as libMediathek
import time
from datetime import datetime

if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus
else: # for Python 3
	from urllib.parse import quote_plus

def getCategories():
	response = libMediathek.getUrl("http://www.daserste.de/dasersteapp/app/index~categories.json")
	j = json.loads(response)
	l = []
	for entry in j['result']:
		d = {}
		d['_name'] = entry['headline']
		try: d['thumb'] = _chooseThumb(entry['teaserImages'][0]['variantes'])
		except: pass #todo: make pretty
		d['url'] = 'http://www.daserste.de/dasersteapp/app/index~categories_pageSize-100_catVideo-'+entry['key']+'.json'
		d['_type'] = 'dir'
		d['mode'] = 'libDasErsteListVideos'
		l.append(d)
	return l


def getChars():
	response = libMediathek.getUrl("http://www.daserste.de/dasersteapp/app/index~series.json")
	j = json.loads(response)
	l = []
	for c in j['result']:
		if not c['hasContent']:
			l.append(c['charIndex'])
	return l


def getAZ():
	response = libMediathek.getUrl("http://www.daserste.de/dasersteapp/app/index~series_plain-false.json")
	j = json.loads(response)
	l = []
	for c in j['result']:
		if c['hasContent']:
			for show in c['content']:
				d = {}
				d['_name'] = show['headline']
				try: d['_thumb'] = _chooseThumb(show['imageUrls'][0]['variantes'])
				except: pass
				#d['url'] = 'http://www.daserste.de/dasersteapp/app/index~categories_series-'+show['serial']+'.json'
				serial = show['serial']
				if sys.version_info[0] < 3: # for Python 2
					serial = serial.encode('utf-8')
				d['url'] = 'http://www.daserste.de/dasersteapp/app/index~series_serial-' + serial + '_types-sendung,sendebeitrag_pageNumber-0_pageSize-100.json'
				d['_type'] = 'dir'
				d['mode'] = 'libDasErsteListVideos'
				l.append(d)
	return l


def getDate(day):
	url = 'http://www.daserste.de/dasersteapp/app/index~program_pd-'+day+'.json'
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for r in j['result']:
		if 'entries' in r:
			for entry in r['entries']:
				if entry['hasVideo']:# or entry['videoAvailableSoon']:
					d = _parseVideo(entry,'date')
					l.append(d)
	return l


def getSearch(s):
	#url = 'http://www.daserste.de/dasersteapp/app/index~program_pd-'+day+'.json'
	url = 'http://www.daserste.de/dasersteapp/index~search_documentTypes-video_s-broadcastDate_dir-desc_f-dateRange_fk-1YEAR%7C14DAYS_searchText-' + quote_plus(s) + '.json'
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for r in j['result']:
		if 'entries' in r:
			for entry in r['entries']:
				d = _parseVideo(entry)
				l.append(d)
	return l


def getVideos(url,type='dir'):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []

	if 'entries' in j:
		for entry in j['entries']:
			if isinstance(entry, dict):
				l.append(_parseVideo(entry))
	return l


def _parseVideo(entry,t='video'):
	d = {}
	#d['plot'] = entry['teaserImages']['caption']
	try: d['_thumb'] = _chooseThumb(entry['teaserImages'][0]['variantes'],True)
	except: pass #todo: make pretty
	if 'serialProgramName' in entry:
		d['_name'] = entry['serialProgramName']
		d['_name'] += ' - '
		d['_name'] += entry['headline']
		d['_name'] = d['_name'].replace('  ',' ')
		d['_tvshowtitle'] = entry['serialProgramName']
	else:
		d['_name'] = entry['headline']
		d['_tvshowtitle'] = entry['headline']
		if 'subheadline' in entry:
			d['_name'] += ' - ' + entry['subheadline']
	if 'teaserTextLong' in entry:
		d['_plot'] = entry['teaserTextLong']
	if 'fskRating' in entry:
		d['_mpaa'] = entry['fskRating'].replace('fsk','FSK ')
	if 'videoDuration' in entry:
		d['_duration'] = str(entry['videoDuration'])
	if 'referenceDate' in entry:
		epoch = entry['referenceDate']/1000
		d['_epoch'] = str(epoch)
		airedtime =  datetime.fromtimestamp(epoch)
		d['_aired'] = airedtime.strftime('%Y-%m-%d')
		d['_airedtime'] = airedtime.strftime('%H:%M')
		if 'serialProgramName' in entry:
			d['_name'] = '(' + d['_aired'] + ') ' + d['_name']
	d['url'] = 'http://www.daserste.de/dasersteapp/' + entry['id'] + '~full.json'
	d['_type'] = t
	d['mode'] = 'libDasErstePlay'

	return d


def getVideo(url):
	videoUrl = None
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	if 'relatedContent' in j:
		for item in j['relatedContent']:
			if item['type'] == 'video':
				id = item['entries'][0]['id']
				response = libMediathek.getUrl('http://www.daserste.de/dasersteapp/' + id + '~full.json')
				j2 = json.loads(response)
				videoUrl = j2['assets'][0]['urls'][0]['url']
				break

	if not videoUrl and 'assets' in j:
		videoUrl = j['assets'][0]['urls'][0]['url']

	if not videoUrl:
		return None

	#else:
	#	response = libMediathek.getUrl('http://www.daserste.de/dasersteapp/' + j['relatedContent'][0]['entries'][0]['id'] + '~full.json')
	#	j = json.loads(response)
	#	videoUrl = j['assets'][0]['urls'][0]['url']
	d = {}
	d['media'] = []
	d['media'].append({'url':videoUrl, 'stream':'HLS'})
	thumb = j['teaserImages'][0]['variantes'][0]['url']
	for possiblethumb in j['teaserImages'][0]['variantes']:
		if possiblethumb['type'] == 'varxl':
			thumb = possiblethumb['url']

	d['metadata'] = {'name':j['serialProgramName'], 'plot': j['teaserTextLong'], 'thumb':thumb, 'duration':str(j['videoDuration'])}
	if 'subtitles' in j:
		d['subtitle'] = []
		d['subtitle'].append({'url':j['subtitles']['subtitleSrt'], 'type':'srt', 'lang':'de'})
		#d['subtitle'].append({'url':j['subtitles']['subtitleWebVTT'], 'type':'webvtt', 'lang':'de'})#breaks the libmediathek parser
	return d


def _chooseThumb(l,video=False):
	t = None
	for d in l:
		if video:
			if d['type'] == 'varm':
				t = d['url']
				if sys.version_info[0] < 3: # for Python 2
					t = t.encode('utf-8')
		else:
			if d['type'] == 'varxl':
				t = d['url']
				if sys.version_info[0] < 3: # for Python 2
					t = t.encode('utf-8')
		if d['type'] == 'varl':
			bak = d['url']
			if sys.version_info[0] < 3: # for Python 2
				bak = bak.encode('utf-8')
	if t == None:
		return bak
	else:
		return t

