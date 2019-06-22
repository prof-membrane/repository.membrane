# -*- coding: utf-8 -*-
import time
import json
# import xbmc
import BeautifulSoup as bs
import libmediathek3 as libMediathek
from datetime import date, datetime, timedelta


base = 'https://www.3sat.de'
api_base = 'https://api.3sat.de'
playerId = 'ngplayer_2_3'
thumbnail1_types = ['is-desktop', 'is-mobile']
thumbnail2_types = ['is-16-9', 'is-8-9']
preferred_thumbnail_type = 0 # => Desktop
preferred_resolutions = [['384w', '768w', '1280w', '1920w', '2400w'], ['240w', '640w', '1152w']]
translation = libMediathek.getTranslation


def list():
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','lib3satHtmlListMain')
	# xbmc.log('%s' % mode, xbmc.LOGFATAL)
	if mode == 'lib3satHtmlPlay':
		media = modes.get(mode)()
		if media is None:
			return False
		else:
			libMediathek.play(media)
	else:
		l = modes.get(mode)()
		if not (l is None):
			libMediathek.addEntries(l)
			libMediathek.endOfDirectory()
	return True


def lib3satHtmlListMain():
	l = []
	l.append({'name':translation(31032), 'mode':'lib3satHtmlListLetters', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'lib3satHtmlListDate', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'lib3satHtmlSearch', '_type':'dir'})
	return l


def lib3satHtmlListLetters():
	# URL z.B.: https://www.3sat.de/sendungen-a-z?group=a
	mode = 'lib3satHtmlListShows'
	l = libMediathek.populateDirAZ(mode, ['#'])
	d = {}
	d['mode'] = mode
	d['name'] = '0-9'
	d['_type'] = 'dir'
	l.append(d)
	return l


def lib3satHtmlListDate():
	# URL z.B.: https://www.3sat.de/programm?airtimeDate=2019-06-21
	l = libMediathek.populateDirDate('lib3satHtmlListDateVideos')
	return l


def chooseImage(pictureList, thumbnail_type):
	if not (pictureList is None):
		pictureList = (
			filter(
				lambda(x):
					hasattr(x,'attrs')
					and
					len(filter(lambda(y): (y[0]=='class') and (y[1].find(thumbnail_type[preferred_thumbnail_type])>=0), x.attrs)) > 0
				, pictureList
			)
		)
		if len(pictureList) > 0:
			pictureSources = filter(lambda(x): x[0]=='data-srcset', pictureList[0].attrs)
			if len(pictureSources) > 0:
				pictures = pictureSources[0][1].split(',')
				for index, item in enumerate(pictures):
					pictures[index] = item.split(' ')
				for resolution in preferred_resolutions[preferred_thumbnail_type]:
					for picture in pictures:
						if len(picture) > 1 and picture[1] == resolution:
							return picture[0]
			pictureSources = filter(lambda(x): x[0]=='data-src', pictureList[0].attrs)
			if len(pictureSources) > 0:
				return pictureSources[0][1]
	return None


def getDate(date_str):
	l = []
	url = base + '/programm?airtimeDate=' + date_str
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response)
	articles = soup.findAll('article', {'class': (lambda(x): x.find('is-video')>=0)})
	for article in articles:
		d = {}
		name = article.find('h3')
		if not (name is None):
			d['_type'] = 'video'
			d['mode'] = 'lib3satHtmlPlay'
			d['_name'] = name.text
			airedtime_begin = None
			airedtime_end = None
			for attr in article.attrs:
				if attr[0] == 'data-airtime-begin' or attr[0] == 'data-airtime-end':
					start = attr[1].split('+')
					zulutime = (len(start) == 1)
					if zulutime:
						format = '%Y-%m-%dT%H:%M:%SZ'
					else:
						format = '%Y-%m-%dT%H:%M:%S'
					try:
						airedtime = datetime.strptime(start[0], format)
					except TypeError:
						airedtime = datetime(*(time.strptime(start[0], format)[0:6]))
					if zulutime:
						tz_offset = timedelta (minutes = (time.timezone / -60) + (time.localtime().tm_isdst * 60))
						airedtime += tz_offset
					if attr[0] == 'data-airtime-begin':
						airedtime_begin = airedtime
						airedtime = datetime (airedtime.year, airedtime.month, airedtime.day, airedtime.hour, (airedtime.minute / 5) * 5)
						d['_airedtime'] = airedtime.strftime('%H:%M')
						d['_name'] = '(' + d['_airedtime'] + ') ' + d['_name']
					else:
						airedtime_end = airedtime
			if not (airedtime_begin is None) and not (airedtime_end is None):
				d['duration'] = str((airedtime_end - airedtime_begin).seconds)
			plot = article.find('p', {'class': 'teaser-epg-text'})
			if not (plot is None):
				d['_plot'] = plot.text
			picture = article.find('picture')
			if not (picture is None):
				d['_thumb'] = chooseImage(picture.contents, thumbnail1_types)
			url = article.find('a', {'data-link': (lambda(x): not(x is None))})
			if not (url is None):
				d['url'] = base + filter(lambda(x): x[0]=='href', url.attrs)[0][1]
			l.append(d)
	return l


def lib3satHtmlListDateVideos():
	if 'datum' in params:
		day = date.today() - timedelta(int(params['datum']))
		yyyy_mm_dd = day.strftime('%Y-%m-%d')
	else:
		ddmmyyyy = libMediathek.dialogDate()
		yyyy_mm_dd = ddmmyyyy[4:8] + '-' + ddmmyyyy[0:2] + '-' + ddmmyyyy[2:4]
	l = getDate(yyyy_mm_dd)
	return l


def getAZ(url):
	l = []
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response)
	articles = soup.findAll('article')
	for article in articles:
		d = {}
		name_link = article.find('a',  {'class': (lambda(x): x.find('teaser-title-link')>=0)})
		if not (name_link is None):
			href_attr = filter(lambda(x): x[0] == 'href', name_link.attrs)
			name_attr = article.find('p',  {'class': (lambda(x): x.find('a--headline')>=0)})
			if len(name_attr) > 0 and len(href_attr) > 0:
				name = name_attr.text
				href = href_attr[0][1]
				d['_type'] = 'video'
				d['mode'] = 'lib3satHtmlPlay'
				d['_name'] = name
				d['_plot'] = name
				d['url'] = base + href
				picture = article.find('picture')
				if not (picture is None):
					d['_thumb'] = chooseImage(picture.contents, thumbnail2_types)
				l.append(d)
	return l


def lib3satHtmlListShows():
	libMediathek.sortAZ()
	url = base + '/sendungen-a-z?group=' + params['name'].lower()
	l = getAZ(url)
	return l


def lib3satHtmlSearch():
	search_string = libMediathek.getSearchString()
	if search_string:
		url = base + '/suche?q=' +search_string
		l = getAZ(url)
		return l
	else:
		return None


def grepItem(target):
	if target['profile'] == 'http://zdf.de/rels/not-found':
		return False
	if not ('contentType' in target):
		return False
	d = {}
	d['_name'] = target['title']
	d['_plot'] = target['teasertext']
	if target['contentType'] == 'clip':
		try:
			d['url'] = api_base + target['mainVideoContent']['http://zdf.de/rels/target']['http://zdf.de/rels/streams/ptmd-template'].replace('{playerId}',playerId)
			if 'duration' in target['mainVideoContent']['http://zdf.de/rels/target']:
				d['_duration'] = str(target['mainVideoContent']['http://zdf.de/rels/target']['duration'])
			d['_type'] = 'clip'
			d['mode'] = 'lib3satHtmlPlay'
		except: d = False
	elif target['contentType'] == 'episode':
		try:
			if 'mainVideoContent' in target:
				content = target['mainVideoContent']['http://zdf.de/rels/target']
			elif 'mainContent' in target:
				content = target['mainContent'][0]['videoContent'][0]['http://zdf.de/rels/target']
			d['url'] = api_base + content['http://zdf.de/rels/streams/ptmd-template'].replace('{playerId}',playerId)
			if 'duration' in content:
				d['_duration'] = str(content['duration'])
			d['_type'] = 'video'
			d['mode'] = 'lib3satHtmlPlay'
		except: d = False
	else:
		log('Unknown target type: ' + target['contentType'])
		d = False
	return d


def getU(url, api_token):
	# xbmc.log('api_token %s, url = %s' % (api_token, url), xbmc.LOGFATAL)
	header = { 'Api-Auth' : 'Bearer ' + api_token }
	response = libMediathek.getUrl(url,header)
	return response


def getVideoUrl(url, api_token):
	d = {}
	d['media'] = []
	response = getU(url,api_token)
	j = json.loads(response)
	for caption in j.get('captions',[]):
		if caption['format'] == 'ebu-tt-d-basic-de':
			d['subtitle'] = [{'url':caption['uri'], 'type':'ttml', 'lang':'de', 'colour':True}]
		#elif caption['format'] == 'webvtt':
		#	d['subtitle'] = [{'url':caption['uri'], 'type':'webvtt', 'lang':'de', 'colour':False}]
	for item in j['priorityList']:
		if item['formitaeten'][0]['type'] == 'h264_aac_ts_http_m3u8_http':
			for quality in item['formitaeten'][0]['qualities']:
				if quality['quality'] == 'auto':
					d['media'].append({'url':quality['audio']['tracks'][0]['uri'], 'type': 'video', 'stream':'HLS'})
	return d


def lib3satHtmlPlay(url = None):
	result = None
	if url is None:
		url = params['url']
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response)
	playerbox = soup.find('div', {'class': (lambda(x): x.find('b-playerbox')>=0)})
	if not (playerbox is None) and (hasattr(playerbox,'attrs')):
		jsb_arr = filter(lambda(x): x[0]=='data-zdfplayer-jsb', playerbox.attrs)
		if len(jsb_arr) > 0:
			json_str = jsb_arr[0][1]
			jsb = json.loads(json_str)
			content_link = jsb['content']
			api_token = jsb['apiToken']
		 	content_response = getU(content_link, api_token)
		 	target = json.loads(content_response)
		 	j = grepItem(target)
		 	result = getVideoUrl(j['url'], api_token)
	return result


modes = {
	'lib3satHtmlListMain': lib3satHtmlListMain,
	'lib3satHtmlListLetters': lib3satHtmlListLetters,
	'lib3satHtmlListDate': lib3satHtmlListDate,
	'lib3satHtmlListDateVideos': lib3satHtmlListDateVideos,
	'lib3satHtmlSearch': lib3satHtmlSearch,
	'lib3satHtmlListShows': lib3satHtmlListShows,
	'lib3satHtmlPlay': lib3satHtmlPlay,
}
