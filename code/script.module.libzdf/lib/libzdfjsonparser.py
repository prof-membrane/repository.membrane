# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import libzdftokengrabber

base = 'https://api.zdf.de'
playerId = 'ngplayer_2_3'

#headerMenu   = {'Api-Auth': 'Bearer '+tokenMenu}
#headerPlayer = {'Api-Auth': 'Bearer '+tokenPlayer}

def getU(url,Menu=False):
	try:
		header = getHeader(Menu)
		response = libMediathek.getUrl(url,header)
	except:
		(tokenMenu, tokenPlayer) = libzdftokengrabber.grepToken()
		header = getHeader(Menu, tokenMenu, tokenPlayer)
		response = libMediathek.getUrl(url,header)
	return response

def getHeader(Menu, tokenMenu = None, tokenPlayer = None):
	if Menu:
		header = { 'Api-Auth': 'Bearer ' + (tokenMenu if tokenMenu else libMediathek.f_open(libMediathek.pathUserdata('tokenMenu'))) }
	else:
		header = { 'Api-Auth': 'Bearer ' + (tokenPlayer if tokenPlayer else libMediathek.f_open(libMediathek.pathUserdata('tokenPlayer'))) }
	return header

def parsePage(url):
	response = getU(url,True)

	j = json.loads(response)
	if   j['profile'] == 'http://zdf.de/rels/search/result':
		return _parseSearch(j)
	elif j['profile'] == 'http://zdf.de/rels/search/result-page':
		return _parseSearchPage(j)
	elif j['profile'] == 'http://zdf.de/rels/content/page-index':
		return _parsePageIndex(j)
	elif j['profile'] == 'http://zdf.de/rels/content/page-index-teaser':
		return _parseTeaser(j)
	elif j['profile'] == 'http://zdf.de/rels/cmdm/resultpage-broadcasts':
		return _parseBroadcast(j)
	else:
		libMediathek.log('Unknown profile: ' + j['profile'])

def getAZ(url='https://api.zdf.de/content/documents/sendungen-100.json?profile=default'):
	#response = libMediathek.getUrl("https://api.zdf.de/content/documents/sendungen-100.json?profile=default",headerMenu)
	#response = getU("https://api.zdf.de/content/documents/sendungen-100.json?profile=default",True)
	response = getU(url,True)
	j = json.loads(response)
	letters = {}
	l = []
	for brand in j['brand']:
		if 'title' in brand:
			#l = []
			if 'teaser' in brand:
				for teaser in brand['teaser']:
					target = teaser['http://zdf.de/rels/target']
					d = _grepItem(target)
					if d:
						l.append(d)
	return l

def _parseSearch(j):
	l = []
	for module in j['module']:
		for result in module['filterRef']['resultsWithVideo']['http://zdf.de/rels/search/results']:
			target = result['http://zdf.de/rels/target']
			d = _grepItem(target)
			if d:
				d['_views'] = str(result['viewCount'])
				l.append(d)
	return l

def _parseSearchPage(j):
	l = []
	for result in j['http://zdf.de/rels/search/results']:
		target = result['http://zdf.de/rels/target']
		d = _grepItem(target)
		if d:
			l.append(d)
	l.sort(key = lambda x: x['name'])
	return l

def _parsePageIndex(j):
	l = []
	for result in j['module'][0]['filterRef']['resultsWithVideo']['http://zdf.de/rels/search/results']:
		target = result['http://zdf.de/rels/target']
		d = _grepItem(target)
		if d:
			d['_views'] = str(result['viewCount'])
			l.append(d)
	return l

def _parseBroadcast(j):
	l = []
	for broadcast in j['http://zdf.de/rels/cmdm/broadcasts']:
		if 'http://zdf.de/rels/content/video-page-teaser' in broadcast:
			target = broadcast['http://zdf.de/rels/content/video-page-teaser']
			d = _grepItem(target)
			if d:
				#d['airedISO8601'] = broadcast['airtimeBegin']
				if broadcast['effectiveAirtimeBegin'] != None:#TODO: find alternative for videos without this field
					d['_airedISO8601'] = broadcast['effectiveAirtimeBegin']
				d['_type'] = 'date'
				l.append(d)
	return l

def _grepItem(target):
	if target['profile'] == 'http://zdf.de/rels/not-found':
		return False
	if not ('contentType' in target):
		return False
	d = {}
	d['name'] = target['teaserHeadline']
	d['plot'] = target['teasertext']
	d['thumb'] = _chooseImage(target['teaserImageRef'])
	#d['url'] = base + target['http://zdf.de/rels/brand']['http://zdf.de/rels/target']['canonical']
	if target['contentType'] == 'brand' or target['contentType'] == 'category':
		try:
			#d['url'] = base + target['canonical']
			d['url'] = base + target['http://zdf.de/rels/search/page-video-counter-with-video']['self'].replace('&limit=0','&limit=100')
			d['_type'] = 'dir'
			d['mode'] = 'libZdfListPage'
		except: d = False
	elif target['contentType'] == 'clip':
		try:
			d['url'] = base + target['mainVideoContent']['http://zdf.de/rels/target']['http://zdf.de/rels/streams/ptmd-template'].replace('{playerId}',playerId)
			if 'duration' in target['mainVideoContent']['http://zdf.de/rels/target']:
				d['_duration'] = str(target['mainVideoContent']['http://zdf.de/rels/target']['duration'])
			d['_type'] = 'clip'
			#d['_type'] = 'video'
			d['mode'] = 'libZdfPlay'
		except: d = False
	elif target['contentType'] == 'episode':# or target['contentType'] == 'clip':
		try:
			if not target['hasVideo']:
				return False
			#if target['mainVideoContent']['http://zdf.de/rels/target']['showCaption']:
			#	d['suburl'] = base + target['mainVideoContent']['http://zdf.de/rels/target']['captionUrl']
			if 'mainVideoContent' in target:
				content = target['mainVideoContent']['http://zdf.de/rels/target']
			elif 'mainContent' in target:
				content = target['mainContent'][0]['videoContent'][0]['http://zdf.de/rels/target']

			d['url'] = base + content['http://zdf.de/rels/streams/ptmd-template'].replace('{playerId}',playerId)
			if 'duration' in content:
				d['_duration'] = str(content['duration'])
			d['_type'] = 'video'
			d['mode'] = 'libZdfPlay'

			programmeItem = target.get('programmeItem', None)
			if isinstance(programmeItem, list) and len(programmeItem) > 0:
				episode = programmeItem[0].get('http://zdf.de/rels/target', None)
				if episode:
					episodeNumber = episode.get('episodeNumber', None)
					if episodeNumber:
						ep_nr = str(episodeNumber)
						if len(ep_nr) == 1:
							ep_nr = ' ' + ep_nr
						d['name'] = 'Folge ' + ep_nr + ' - ' + d['name']
					season = episode.get('http://zdf.de/rels/cmdm/season', None)
					if season:
						seasonTitle = season.get('seasonTitle', None)
						if seasonTitle:
							d['name'] = str(seasonTitle) + ' - ' + d['name']
						series = season.get('http://zdf.de/rels/cmdm/series',None)
						if series:
							brand = series.get('http://zdf.de/rels/cmdm/brand',None)
							if brand:
								brandName = brand.get('brandName', None)
								if brandName:
									d['name'] = brandName + ' - ' + d['name']
			else:
				brand = target.get('http://zdf.de/rels/brand',None)
				if brand:
					title = brand.get('title',None)
					if title:
						d['name'] = title + ' - ' + d['name']
		except:
			d = False
	else:
		libMediathek.log('Unknown target type: ' + target['contentType'])
		d = False
	return d

def _chooseImage(teaserImageRef,isVideo=False):
	if not isVideo:
		if 'layouts' in teaserImageRef:
			if '384xauto' in teaserImageRef['layouts']:
				return teaserImageRef['layouts']['384xauto']
			elif '1920x1080' in teaserImageRef['layouts']:
				return teaserImageRef['layouts']['1920x1080']

	return ''

def getVideoUrlById(id):
	url = base + '/content/documents/' + id + '.json?profile=player'
	response = getU(url,True)
	j = json.loads(response)
	url = base + j['mainVideoContent']['http://zdf.de/rels/target']['http://zdf.de/rels/streams/ptmd-template'].replace('{playerId}',playerId)
	return getVideoUrl(url)

def getVideoUrl(url):
	media = []
	response = getU(url,False)
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
