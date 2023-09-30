#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from datetime import datetime
import bs4 as bs
import libmediathek3 as libMediathek


base = 'https://www.3sat.de'
api_base = 'https://api.3sat.de'
playerId = 'ngplayer_2_3'
thumbnail1_types = ['is-desktop', 'is-mobile']
thumbnail2_types = ['is-16-9', 'is-8-9']
preferred_thumbnail_type = 0 # => Desktop
preferred_resolutions = [['384w', '768w', '1280w', '1920w', '2400w'], ['240w', '640w', '1152w']]


def chooseImage(pictureList, thumbnail_type):
	if not (pictureList is None):
		for pictureItem in pictureList:
			if hasattr(pictureItem,'attrs') and (thumbnail_type[preferred_thumbnail_type] in pictureItem.attrs.get('class', [])):
				pictureSources = pictureItem.attrs.get('data-srcset', None)
				if not (pictureSources is None):
					pictures = pictureSources.split(',')
					for index, item in enumerate(pictures):
						pictures[index] = item.split(' ')
					for resolution in preferred_resolutions[preferred_thumbnail_type]:
						for picture in pictures:
							if len(picture) > 1 and picture[1] == resolution:
								return picture[0]
				# Fallback
				pictureSource = pictureItem.attrs.get('data-src', None)
				return pictureSource
	return None


def getDate(date_str):
	l = []
	url = base + '/programm?airtimeDate=' + date_str
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response, 'html.parser')
	articles = soup.findAll('article', {'class': 'is-video'})
	for article in articles:
		d = {}
		name = article.find('h3')
		if not (name is None):
			d['_type'] = 'date'
			d['mode'] = 'lib3satHtmlPlay'
			d['name'] = name.text
			airedtime_begin = libMediathek.str_to_airedtime(article.attrs.get('data-airtime-begin', None))
			if not (airedtime_begin is None):
				airedtime = datetime (airedtime_begin.year, airedtime_begin.month, airedtime_begin.day, airedtime_begin.hour, int(airedtime_begin.minute / 5) * 5)
				d['_airedtime'] = airedtime.strftime('%H:%M')
				airedtime_end = libMediathek.str_to_airedtime(article.attrs.get('data-airtime-end', None))
				if not (airedtime_end is None):
					d['duration'] = str((airedtime_end - airedtime_begin).seconds)
			plot = article.find('p', {'class': 'teaser-epg-text'})
			if not (plot is None):
				d['plot'] = plot.text
			picture = article.find('picture')
			if not (picture is None):
				d['thumb'] = chooseImage(picture.contents, thumbnail1_types)
			url = article.find('a', {'data-link': (lambda x: not(x is None))})
			if not (url is None) and not (url.attrs is None):
				href = url.attrs.get('href', None)
				if not (href is None):
					d['url'] = base + href
			l.append(d)
	return l


def getAZ(url):
	l = []
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response, 'html.parser')
	articles = soup.findAll('article')
	for article in articles:
		d = {}
		name_link = article.find('a',  {'class': 'teaser-title-link'})
		if not (name_link is None) and not (name_link.attrs is None):
			href = name_link.attrs.get('href', None)
			name_attr = article.find('p',  {'class': 'a--headline'})
			if len(name_attr) > 0 and not (href is None):
				name = name_attr.text
				d['_type'] = 'video'
				d['mode'] = 'lib3satHtmlPlay'
				d['name'] = name
				d['plot'] = name
				d['url'] = base + href
				picture = article.find('picture')
				if not (picture is None):
					d['thumb'] = chooseImage(picture.contents, thumbnail2_types)
				l.append(d)
	return l


def grepItem(target):
	if target['profile'] == 'http://zdf.de/rels/not-found':
		return False
	if not ('contentType' in target):
		return False
	d = {}
	d['name'] = target['title']
	d['plot'] = target['teasertext']
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
	# import xbmc
	# xbmc.log('api_token %s, url = %s' % (api_token, url), xbmc.LOGFATAL)
	header = { 'Api-Auth' : 'Bearer ' + api_token }
	response = libMediathek.getUrl(url,header)
	return response


def getVideoUrl(url, api_token):
	media = []
	response = getU(url,api_token)
	j = json.loads(response)
	for item in j['priorityList']:
		if (item['formitaeten'][0].get('type',None) == 'h264_aac_ts_http_m3u8_http' 
			or 
			item['formitaeten'][0].get('mimeType',None) == 'application/x-mpegURL'
		): 
			for streams in item['formitaeten'][0]['qualities']:
				if streams['quality'] == 'auto':
					media.insert(0, {'url':streams['audio']['tracks'][0]['uri'], 'type': 'video', 'stream':'hls'})
		elif (item['formitaeten'][0].get('type',None) == 'h264_aac_mp4_http_na_na'
			or  
			item['formitaeten'][0].get('mimeType',None) == 'video/mp4'
		):
			for streams in item['formitaeten'][0]['qualities']:
				try:
					quality = ('low','med','high','veryhigh').index(streams['quality'])
				except ValueError:
					pass
				else:
					media.append({'url':streams['audio']['tracks'][0]['uri'], 'type':'video', 'stream':'mp4', 'bitrate':quality})
	ignore_adaptive = libMediathek.getSettingBool('ignore_adaptive')
	while ignore_adaptive and len(media) > 1 and media[0]['stream'] == 'hls':
		del media[0]
	if media: 
		result = dict(media = media)
		for caption in j.get('captions',[]):
			if caption['format'] == 'ebu-tt-d-basic-de':
				result['subtitle'] = [{'url':caption['uri'], 'type':'ttml', 'lang':'de', 'colour':True}]
		return result
	else: 
		return None


def lib3satHtmlPlay(url):
	result = None
	if url is None:
		params = libMediathek.get_params()
		url = params['url']
	response = libMediathek.getUrl(url)
	soup = bs.BeautifulSoup(response, 'html.parser')
	playerbox = soup.find('div', {'class': 'b-playerbox'})
	if not (playerbox is None) and (hasattr(playerbox,'attrs')):
		jsb_str = playerbox.attrs.get('data-zdfplayer-jsb', None)
		if not (jsb_str is None):
			jsb = json.loads(jsb_str)
			content_link = jsb['content']
			api_token = jsb['apiToken']
			content_response = getU(content_link, api_token)
			target = json.loads(content_response)
			j = grepItem(target)
			result = getVideoUrl(j['url'], api_token)
	return result
