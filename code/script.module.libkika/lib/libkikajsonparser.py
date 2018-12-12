# -*- coding: utf-8 -*-
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
		d['_name'] = entry['title']
		if 'description' in entry:
			d['_plot'] = entry['description']
		d['_thumb'] = entry['mediumLogoImageUrl']
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
		d['_name'] = entry['title']
		d['_plot'] = entry['description']
		d['_duration'] = str(entry['duration'])
		d['_thumb'] = entry['largeTeaserImageUrl']
		d['_fanart'] = entry['_embedded']['brand']['smallBackgroundImageUrl']
		d['_channel'] = entry['broadcaster']
		#d['_airedISO8601'] = entry['appearDate']
		d['uri'] = entry['_links']['player-assets']['href']
		d['mode'] = 'libKikaPlay'
		d['_type'] = 'video'
		l.append(d)
	return l
	
def getVideoUrl(uri):
	response = libMediathek.getUrl(baseUrl+uri)
	j = json.loads(response)
	for asset in j['assets']:
		if asset['quality'] == 'Video 2014 | MP4 Web XL | 16:9 | 1280x720':
			url = asset['url']
	d = {'media':[{'url':url, 'type': 'video', 'stream':'HLS'}]}
	return d

	
	
"""
def getShows():
	response = libMediathek.getUrl('http://itv.mit-xperts.com/kikamediathek/kika/api.php/videos/hbbtv/sendungen/sendereihen-hbbtv-100-hbbtv.json')
	j = json.loads(response)
	l = []
	for entry in j['result']['serialPrograms']:
		show = _getShow(entry)
		l.append(show)
	return l
	
def _getShow(jsonDict):
	d = {}
	d['_name'] = jsonDict['headline']
	if 'serialProgramId' in jsonDict:
		d['url'] = 'http://itv.mit-xperts.com/kikamediathek/kika/api.php/videos/hbbtv/suche/hbbtv-search-100-hbbtv.json?serialProgram=' + jsonDict['serialProgramId']
	elif 'bundleUrl' in jsonDict:
		d['url'] = 'http://itv.mit-xperts.com/kikamediathek/kika/api.php' + jsonDict['bundleUrl']
	if 'description' in jsonDict:
		d['_plot'] = jsonDict['description']
	try:
		d['_thumb'] = jsonDict['images'][0]['imageUrls']['varhbbtvm']
	except: pass
	d['mode'] = 'libKikaListVideos'
	d['_channel'] = 'KiKa'
	d['_type'] = 'dir'	
	return d
	
def getVideos(url,type='video'):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for entry in j['result']['videos']:
		vid = _getDictVideos(entry,type)
		l.append(vid)
	return l
	
def _getDictVideos(jsonDict,type='video'):#TODO: ttl
	d = {}
	d['_name'] = jsonDict['headline']
	if 'teaserText' in jsonDict:
		d['_plot'] = jsonDict['teaserText']
	if 'serialProgram' in jsonDict:
		d['_tvshowtitle'] = jsonDict['serialProgram']['serialProgramName']
	HH,MM,SS = jsonDict['videoDuration'].split(':')
	d['_duration'] = str(int(HH) * 3600 + int(MM) * 60 + int(SS))
	d['url'] = 'http://www.kika.de/' + jsonDict['id'] + '-avCustom.xml'
	d['_thumb'] = jsonDict['images'][0]['imageUrls']['varhbbtvm']
	d['_mpaa'] = jsonDict['fskRating']
	if 'referenceDate' in jsonDict:
		d['_airedISO8601'] = jsonDict['referenceDate']
	
	d['mode'] = 'libMdrPlay'
	d['_type'] = type
	
	return d
"""