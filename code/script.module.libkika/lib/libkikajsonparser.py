# -*- coding: utf-8 -*-
import sys
import json
import libmediathek3 as libMediathek

baseUrl = 'http://www.kika.de/api/v1/kikaplayer/kikaapp'

def getChannel(cid='1'):
	response = libMediathek.getUrl(baseUrl + '/api/channels/' + cid)
	j = json.loads(response)
	l = []
	for entry in j['result']['serialPrograms']:
		d = {}
		l.append(d)
	return l

def getBrands():#Shows
	response = libMediathek.getUrl(baseUrl+'/api/brands?limit=400&orderBy=title&orderDirection=ASC&showEmptyBrands=false')
	j = json.loads(response)
	l = []
	for entry in j['_embedded']['items']:
		d = {}
		d['name'] = entry['title']
		if 'description' in entry:
			d['plot'] = entry['description']
		d['thumb'] = entry.get('mediumLogoImageUrl', entry.get('smallLogoImageUrl', None))
		d['_fanart'] = entry.get('smallBackgroundImageUrl', entry.get('mediumLogoImageUrl', None))
		d['uri'] = entry['_links']['videos']['href']
		d['mode'] = 'libKikaListVideos'
		d['_type'] = 'dir'
		l.append(d)
	return l

def getVideos(uri='/api/videos?limit=20&orderBy=date&orderDirection=DESC'):
	response = libMediathek.getUrl(baseUrl+uri)
	j = json.loads(response)
	l = []
	for entry in j['_embedded']['items']:
		d = {}
		d['name'] = entry['title']
		embedded = entry.get('_embedded',None)
		if embedded:
			brand = embedded.get('brand',None)
			if brand:
				d['name'] = brand['title'] + ' - ' + d['name']
		d['plot'] = entry['description']
		d['_duration'] = str(entry['duration'])
		d['thumb'] = entry['largeTeaserImageUrl']
		d['_fanart'] = entry['_embedded']['brand']['smallBackgroundImageUrl']
		d['_channel'] = entry['broadcaster']
		#d['_airedISO8601'] = entry['appearDate']
		d['uri'] = entry['_links']['player-assets']['href']
		d['mode'] = 'libKikaPlay'
		d['_type'] = 'video'
		l.append(d)
	return l

def getVideoUrl(uri):
	mediaHLS = []
	mediaMP4 = []
	response = libMediathek.getUrl(baseUrl+uri)
	j = json.loads(response)
	for asset in j.get('hbbtvAssets', []) + j.get('assets',[]):
		url = asset['url']
		if url.startswith('//'):
			url = 'https:' + url
		quality = asset.get('quality',None)
		if quality is None:
			continue 
		elif isinstance(quality, int):
			pass
		else:
			try:
				quality = quality.split(' ')[0];
				if len(quality) == 1:
					quality = ('0','1','2','3','4','5','6','7','8','9').index(quality)
				else:
					quality = ('low','med','high','veryhigh','auto').index(quality)
			except ValueError:
				continue
		isAdaptive = asset.get('isAdaptive',None)
		if isAdaptive is None:
			isAdaptive = (url[-4:].lower() != '.mp4')
		if isAdaptive:
			mediaHLS.append({'url':url, 'type':'video', 'stream':'hls', 'bitrate':quality})
		else:
			mediaMP4.append({'url':url, 'type':'video', 'stream':'mp4', 'bitrate':quality})
	mediaHLS.sort(key = lambda x: x['bitrate'], reverse=True)
	mediaHLS = mediaHLS[0:1]
	mediaMP4.sort(key = lambda x: x['bitrate'], reverse=True)
	ignore_adaptive = libMediathek.getSettingBool('ignore_adaptive')
	if ignore_adaptive and mediaMP4:
		media = mediaMP4
	else: 
		media = mediaHLS + mediaMP4   
	if media: 
		return dict(media = media)
	else: 
		return None
