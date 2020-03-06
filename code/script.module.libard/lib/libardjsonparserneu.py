#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import re
import libmediathek3 as libMediathek

if sys.version_info[0] < 3: # for Python 2
	alt_str_type = unicode
	from urllib import urlencode
else: # for Python 3
	alt_str_type = bytes
	from urllib.parse import urlencode
	from functools import reduce

baseUrlJson = 'https://api.ardmediathek.de/public-gateway?'
baseUrlHtml = 'http://www.ardmediathek.de/ard/player/'

keyOperationName = 'operationName'
keyVariables = 'variables'
keyExtensions = 'extensions'
extensions = '{"persistedQuery":{"version":1,"sha256Hash":"%s"}}'
pageNames = ('defaultPage','defaultPage','showPage','programPage','playerPage')
pageIndexDefaultPage = 0
pageIndexLivestream = 1
pageIndexShowPage = 2
pageIndexProgramPage = 3
pageIndexPlayerPage = 4


def deep_get(dictionary, keys, default=None):
	return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split('.'), dictionary)

def parseAZ(channelKey, clientKey, getLivestream=False):
	pageIndex = pageIndexLivestream if getLivestream else pageIndexDefaultPage
	variables = '{"client":"%s","name":"home","personalized":false}'
	sha256Hash = '9995d49ccbd97dfb67357e9e3505e4f022e405d0ad23fc3d21dd36c2e2de7bb8'
	queryParams = {}
	queryParams[keyOperationName] = pageNames[pageIndex]
	queryParams[keyVariables] = variables % clientKey
	queryParams[keyExtensions] = extensions % sha256Hash
	url = baseUrlJson + urlencode(queryParams)
	partnerKey = channelKey
	channelKey = None
	return parse(pageIndex, channelKey, partnerKey, url)

def parseShow(showId):
	pageIndex = pageIndexShowPage
	variables = '{"client":"ard","showId":"%s","pageNumber":0}'
	sha256Hash = '85a89bbc543e4054aa600e4209faeb625d566c5aec44c37d6f7c231785c0d0e6'
	queryParams = {}
	queryParams[keyOperationName] = pageNames[pageIndex]
	queryParams[keyVariables] = variables % showId
	queryParams[keyExtensions] = extensions % sha256Hash
	url = baseUrlJson + urlencode(queryParams)
	return parse(pageIndex, None, None, url)

def parseDate(channelKey, clientKey, date):
	pageIndex = pageIndexProgramPage
	variables = '{"client":"%s","startDate":"%s"}'
	sha256Hash = 'b3f152bfb679d8246594cf7f807860acdb1bf5479801dcace1307d6f6e2a2e23'
	queryParams = {}
	queryParams[keyOperationName] = pageNames[pageIndex]
	queryParams[keyVariables] = variables % (clientKey, date) # date = YYYY-MM-DD
	queryParams[keyExtensions] = extensions % sha256Hash
	url = baseUrlJson + urlencode(queryParams)
	partnerKey = channelKey
	if channelKey:
		channelKey = re.sub('[^A-Za-z0-9]+', '', channelKey)
	return parse(pageIndex, channelKey, partnerKey, url)

def getVideoUrl(clipId):
	pageIndex = pageIndexPlayerPage
	variables = '{"client":"ard","clipId":"%s","deviceType":"mobi"}'
	sha256Hash = '893d15418a9fa569150f104722867e0f6cf39afd443cd53a33aa500e094e0032'
	queryParams = {}
	queryParams[keyOperationName] = pageNames[pageIndex]
	queryParams[keyVariables] = variables % clipId
	queryParams[keyExtensions] = extensions % sha256Hash
	url = baseUrlJson + urlencode(queryParams)
	return parseVideo(pageIndex, url)

def parseVideo(pageIndex, url):
	finalUrl = None
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	mediaArray = deep_get(j, 'data.' + pageNames[pageIndex] + '.mediaCollection._mediaArray')
	if mediaArray:
		mediaStreamArray = mediaArray[0].get('_mediaStreamArray',None)
		if mediaStreamArray:
			return extractBestQuality(mediaStreamArray, lambda x: x[0])
	return None

def parseSearchHtml(url):
	l = []
	response = libMediathek.getUrl(url)
	split = response.split('window.__APOLLO_STATE__');
	if (len(split) > 1):
		json_str = split[1]
		start = 0
		while json_str[start] in (' ','='):
			start += 1
		end = start
		while True:
			while json_str[end] != ';':
				end += 1
			if json_str[end+1:].lstrip().startswith('</script>'): break
			else: end += 1
		json_str = json_str[start:end]
		j = json.loads(json_str)
		for item in j.values():
			if isinstance(item,dict) and (item.get('type',None) == 'ondemand'):
				id = item.get('id',None)
				name = item['shortTitle']
				if id and name:
					d ={}
					d['documentId'] = id
					d['url'] = baseUrlHtml + id
					d['duration'] = str(item.get('duration',None))
					d['name'] = name
					d['plot'] = item.get('longTitle',None)
					d['date'] = item.get('broadcastedOn',None)
					thumb_id = '$Teaser:' + id
					thumb_item = j.get(thumb_id + '.images.aspect16x9',None)
					if not thumb_item:
						thumb_item = j.get(thumb_id + '.images.aspect1x1',None)
					if not thumb_item:
						thumb_item = j.get(thumb_id + '.images.aspect16x7',None)
					if thumb_item and (thumb_item.get('__typename',None) == 'Image'):
						thumb_src = thumb_item.get('src','')
						thumb_src = thumb_src.replace('{width}','1024')
						d['thumb'] = thumb_src
					d['_type'] = 'video'
					d['mode'] = 'libArdPlayHtml'
					l.append(d)
	return l

def getVideoUrlHtml(url):
	response = libMediathek.getUrl(url)
	split = response.split('window.__APOLLO_STATE__');
	if (len(split) > 1):
		json_str = split[1]
		start = 0
		while json_str[start] in (' ','='):
			start += 1
		end = start
		while True:
			while json_str[end] != ';':
				end += 1
			if json_str[end+1:].lstrip().startswith('</script>'): break
			else: end += 1
		json_str = json_str[start:end]
		j = json.loads(json_str)
		return extractBestQuality(j.values(), lambda x: x[x['type']][0])
	return None

def extractBestQuality(streams, fnGetFinalUrl):
	finalUrl = None
	ignore_adaptive = libMediathek.getSettingBool('ignore_adaptive')
	quality = -1
	for item in streams:
		if isinstance(item,dict) and (item.get('__typename',None) == 'MediaStreamArray'):
			currentQuality = item.get('_quality',-1);
			if isinstance(currentQuality,str) or isinstance(currentQuality,alt_str_type):
				if currentQuality == 'auto':
					currentQuality = 0 if ignore_adaptive else sys.maxsize
				else:
					currentQuality = int(currentQuality)
			if currentQuality > quality:
				stream = item.get('_stream',None)
				if stream:
					finalUrl = fnGetFinalUrl(stream)
					quality = currentQuality
	if finalUrl:
		d = {}
		if finalUrl.startswith('//'):
			finalUrl = 'http:' + finalUrl
		if finalUrl.startswith('http://wdradaptiv') or finalUrl.endswith('.mp4'):
			d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'mp4'}]
		else:
			d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'HLS'}]
		return d
	return None

def parse(pageIndex, channelKey, partnerKey, url):
	result = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	data = j.get('data',None)
	if data:
		page = data.get(pageNames[pageIndex],None)
		if page:
			widgets = [page] if pageIndex == pageIndexShowPage else page.get('widgets',[])
			for widget in widgets:
				if (channelKey is None) or (channelKey == widget.get('channelKey',None)):
					teasers = widget.get('teasers',None)
					if teasers:
						for teaser in teasers:
							type = teaser['type']
							publicationService = teaser.get('publicationService',None)
							if (
							 	type in ('live','ondemand','broadcastMainClip','show')
							 	and
								(type == 'live') == (pageIndex == pageIndexLivestream)
								and
								((partnerKey is None) or (publicationService and (partnerKey == publicationService.get('partner',None))))
							):
								documentId = deep_get(teaser, 'links.target.id')
								name = teaser['shortTitle']
								if documentId and name:
									d = {}
									d['documentId'] = documentId
									d['name'] = name
									d['plot'] = teaser.get('longTitle',None)
									if (pageIndex == pageIndexProgramPage) and (partnerKey is None) and publicationService:
										d['name'] = publicationService['name'] + ' - ' + d['name']
									duration = teaser.get('duration', None)
									if duration:
										d['_duration'] = str(duration)
									thumb = deep_get(teaser, 'images.aspect16x9.src')
									if not thumb:
										thumb = deep_get(teaser, 'images.aspect1x1.src')
									if not thumb:
										thumb = deep_get(teaser, 'images.aspect16x7.src')
									if thumb:
										d['thumb'] = (thumb.split('?')[0]).replace('{width}','1024')
									if type == 'show':
										d['_type'] = 'dir'
										d['mode'] = 'libArdListShow'
									else:
										if pageIndex == pageIndexProgramPage:
											airedtime = libMediathek.str_to_airedtime(teaser.get('broadcastedOn', None))
											if airedtime:
												d['_airedtime'] = airedtime.strftime('%H:%M')
												d['name'] = '(' + d['_airedtime'] + ') ' + d['name']
										d['_type'] = 'live' if pageIndex == pageIndexLivestream else 'video'
										d['mode'] = 'libArdPlay'
									result.append(d)
	return result

