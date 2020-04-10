# -*- coding: utf-8 -*-
import sys
import json
import libmediathek3 as libMediathek

baseUrl = 'http://prod.kinderplayer.cdn.tvnext.tv'

def getChannel(cid='1'):
	response = libMediathek.getUrl('http://prod.kinderplayer.cdn.tvnext.tv/api/channels/'+cid)
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
		d['thumb'] = entry['mediumLogoImageUrl']
		d['_fanart'] = entry['smallBackgroundImageUrl']
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
	finalUrl = None
	ignore_adaptive = libMediathek.getSettingBool('ignore_adaptive')
	quality = -1
	response = libMediathek.getUrl(baseUrl+uri)
	j = json.loads(response)
	for asset in j.get('hbbtvAssets', []) + j.get('assets',[]):
		currentQuality = asset.get('quality',-1);
		if not isinstance(currentQuality, int):
			if currentQuality == 'auto':
				currentQuality = 0 if ignore_adaptive else sys.maxsize
			else:
				try:
					currentQuality = ('low','med','high','veryhigh').index(currentQuality)
				except:
					currentQuality = -1
		if currentQuality > quality:
			finalUrl = asset['url']
			quality = currentQuality
	if finalUrl:
		d = {}
		if finalUrl.startswith('//'):
			finalUrl = 'http:' + finalUrl
		if finalUrl.endswith('.mp4'):
			d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'mp4'}]
		else:
			d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'HLS'}]
		return d
	return None
