# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import re
import urllib
from operator import itemgetter
import sys
import xbmcplugin
import xbmcaddon


lang_german  = libMediathek.getSetting('lang') in ('de','0','',None)
current_lang = 'de' if lang_german else 'fr'
addon = xbmcaddon.Addon()

opa_url = 'https://www.arte.tv/hbbtvv2/services/web/index.php/OPA/v3/streams/%s/SHOW/%s';

emac_url = 'https://api.arte.tv/api/emac/v3/' + current_lang + '/web/'
emac_token = {"Authorization": "Bearer MWZmZjk5NjE1ODgxM2E0MTI2NzY4MzQ5MTZkOWVkYTA1M2U4YjM3NDM2MjEwMDllODRhMjIzZjQwNjBiNGYxYw"}

player_url = "https://api.arte.tv/api/player/v2/config/%s/%s"
player_token = {"Authorization": "Bearer MzYyZDYyYmM1Y2Q3ZWRlZWFjMmIyZjZjNTRiMGY4MzY4NzBhOWQ5YjE4MGQ1NGFiODJmOTFlZDQwN2FkOTZjMQ"}

magazines_url = 'https://www.arte.tv/hbbtvv2/services/web/index.php/OPA/v3/magazines/' +  current_lang;

stream_params = '&quality=$in:XQ,HQ,SQ&mediaType=hls&language=' + current_lang + '&channel=' + current_lang.upper()


def _parse_data(video, isByDate = False):
	d = {}

	if video['title'] and video.get('subtitle',None):
		d['name'] = video['title'] + ' | ' + video['subtitle']
	elif video.get('subtitle',None):
		d['name'] = video['subtitle']
	else:
		d['name'] = video['title']

	if video.get('fullDescription',None):
		d['plot'] = video['fullDescription']
	elif video.get('description',None):
		d['plot'] = video['description']
	elif video.get('shortDescription',None):
		d['plot'] = video['shortDescription']

	if isByDate and video.get('broadcastDates',None):
		d['_airedISO8601'] = video['broadcastDates'][0]

	if video.get('images',None):
		if video['images'].get('landscape',None):
			max_res = max(video['images']['landscape']['resolutions'], key=lambda item: item['w'])
			d['thumb'] = max_res['url']
		elif video['images'].get('portrait',None):
			max_res = max(video['images']['portrait']['resolutions'], key=lambda item: item['h'])
			d['thumb'] = max_res['url']

	if video['kind'] == "MAGAZINE" or ('isCollection' in video['kind'] and video['kind']['isCollection']):
		d['mode'] = 'libArteListCollection'
		d['documentId'] = video['programId']
		d['url'] = video['programId']
		d['_type'] = 'dir'
	else:
		d['mode'] = 'libArtePlay'
		d['documentId'] = video['programId']
		d['url'] = '/videoStreams?programId=' + video['programId'] + stream_params + '&kind=' + video['kind']['code']
		d['_type'] = 'date'
		d['_duration'] = video['duration']

	availability_node = video.get('availability',None)
	if availability_node:
		aired_str = availability_node.get('upcomingDate',None)
		if isByDate and (d.get('_airedISO8601',None) == None):
			d['_airedISO8601'] = aired_str
		availability = availability_node.get('label',None)
		if availability:
			d['plot'] = '[COLOR blue]' + availability + ' | [/COLOR]' + d.get('plot','')
		elif aired_str:
			aired_time = libMediathek.str_to_airedtime(aired_str)
			d['plot'] = '[COLOR blue]' + addon.getLocalizedString(32100) + ' ' + aired_time.strftime('%d/%m/%Y') + ' | [/COLOR]' + d.get('plot','')

	return d


def getVideos(url):
	l = []
	url = emac_url + url
	response = libMediathek.getUrl(url, emac_token)
	j = json.loads(response)
	data = j.get('data', [])
	zones = j.get('zones', None)
	if isinstance(zones, list):
		collection_content = [item for item in zones if item.get('code',{}).get('name',None) == 'collection_content']
		collection_subcollection = [item for item in zones if item.get('code',{}).get('name',None) == 'collection_subcollection']
		collection_videos = [item for item in zones if item.get('code',{}).get('name',None) == 'collection_videos']
		for subcollection in collection_subcollection:
			collectionId_subcollectionId = subcollection.get('code',{}).get('id','').split('_')
			if len(collectionId_subcollectionId) == 2:
				subcollection['programId'] = '/data/COLLECTION_SUBCOLLECTION/?collectionId=%s&subCollectionId=%s' % tuple(collectionId_subcollectionId)
				subcollection['kind'] = { 'isCollection': True }
				if collection_content:
					image_data = collection_content[0].get('data', [])
					if image_data:
						subcollection['images'] = image_data[0].get('images',{})
				data.append(subcollection)
		for videos in collection_videos:
			data += videos.get('data',[])
	for video in data:
		l.append(_parse_data(video))
	return l


def getMagazines():
	l = []
	url = magazines_url
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	for video in j['magazines']:
		l.append(_parse_data(video))
	return l


def getCollection(program_id):
	l = getVideos(program_id)
	return l


def getDate(yyyymmdd):
	l = []
	# this would be the better endpoint, but it's not working: /zones/listing_TV_GUIDE?day=
	url = emac_url + '/TV_GUIDE?day=' + yyyymmdd
	response = libMediathek.getUrl(url, emac_token)
	j = json.loads(response)
	data = []
	for zone in j['zones']:
		data += zone['data']
	videos = [video for video in data if video['programId']]
	for video in videos:
		l.append(_parse_data(video, True))
	return l


def getSearch(s):
	return getVideos('/data/SEARCH_LISTING/?query=' + s)


#legend:
#
#VO Original Voice
#VOA Original Voice	Allemande
#VOF Original Voice Francaise
#VA Voice Allemande
#VF Voice Francaise
#VAAUD Audio Description Allemande
#VFAUD Audio Description Francaise
#VE* Other Voice
#
#STA Subtitle Allemande
#STF Subtitle Francaise
#STE* Subtitle Other
#STMA Subtitle Mute Allemande
#STMF Subtitle Mute Francaise
#
#* is always followed by the provided language
#[ANG] English
#[ESP] Spanish
#[POL] Polish
#
#examples:
#VOF-STE[ANG] original audio (french), english subtitles
#VOA-STMA orignal audio (german), with french mute sutitles

# all results equal/above voices[nativeVoice]() indicate native voices
nativeVoice = '__NATIVE_VOICE__'

voices = {
	'VFAUD':lambda: 1 if lang_german else 6,  # Audio Description Francaise
	'VOF':  lambda: 2 if lang_german else 7,  # Original Voice Francaise
	'VF':   lambda: 3 if lang_german else 8,  # Voice Francaise
	'VE':   lambda: 4,                        # Other Voice
	'VO':   lambda: 5,                        # Original Voice
	nativeVoice:  lambda: 5,                  # Internal use
	'VAAUD':lambda: 6 if lang_german else 1,  # Audio Description Allemande
	'VOA':  lambda: 7 if lang_german else 2,  # Original Voice Allemande
	'VA':   lambda: 8 if lang_german else 3,  # Voice Allemande
}

subtitles = {
	'STE':  lambda:-3,                        # Subtitle Other
	'STMF': lambda:-2 if lang_german else 4,  # Subtitle Mute Francaise
	'STF':  lambda:-1 if lang_german else 5,  # Subtitle Francaise
	'STMA': lambda: 4 if lang_german else -2, # Subtitle Mute Allemande
	'STA':  lambda: 5 if lang_german else -1, # Subtitle Allemande
}

qualities = {
	'LQ': 1,
	'MQ': 2,
	'HQ': 3,
	'EQ': 4,
	'SQ': 5,
	'XQ': 6,
}

def getVideoUrl(url, documentId):
	result = None
	prefer_opa_api = libMediathek.getSetting('api') == 'OPAv3'
	getVideoUrl_functions = (getVideoUrl_OPAv3, getVideoUrl_Default) if prefer_opa_api else (getVideoUrl_Default, getVideoUrl_OPAv3)
	for function in getVideoUrl_functions:
		result = function(url, documentId)
		if result:
			break
	return result

def getVideoUrl_OPAv3(url, documentId):
	result = None
	url = opa_url % (documentId, current_lang)
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	storedLang = 0
	bitrate = 0
	hls_videos = j.get('videoStreams',[])
	for video in hls_videos:
		voice_subtitle = video['audioCode'].split('-');
		voice = voice_subtitle[0].split('[')[0]
		subtitle = voice_subtitle[1].split('[')[0] if len(voice_subtitle) > 1 else '';
		currentLang = voices.get(voice, lambda:0)()
		# if currentLang is native language => prefer "no subtitle"
		# if currentLang is foreign language => prefer subtitle in native language
		currentLang = currentLang * 10 + subtitles.get(subtitle, lambda: 9 if (currentLang >= voices[nativeVoice]()) else 0)()
		currentBitrate = qualities.get(video['quality'], 0)
		if currentLang > storedLang or (currentLang == storedLang and currentBitrate > bitrate):
			storedLang = currentLang
			bitrate = currentBitrate
			result = {'url':video['url'], 'type': 'video', 'stream': 'mp4' }
	return {'media': [result]} if result else None

def getVideoUrl_Default(url, documentId):
	result = None
	url = player_url % (current_lang, documentId)
	response = libMediathek.getUrl(url, player_token)
	j = json.loads(response)
	storedLang = 0
	bitrate = 0
	hls_videos = [value for value in j['data']['attributes']['streams'] if 'HLS' in value['protocol']]
	for video in hls_videos:
		if ('versions' in video) and len(video['versions']) > 0:
			voice_subtitle = video['versions'][0]['eStat']['ml5'].split('-');
			voice = voice_subtitle[0].split('[')[0]
			subtitle = voice_subtitle[1].split('[')[0] if len(voice_subtitle) > 1 else '';
		else:
			voice = ''
			subtitle = ''
		currentLang = voices.get(voice, lambda:0)()
		# if currentLang is native language => prefer "no subtitle"
		# if currentLang is foreign language => prefer subtitle in native language
		currentLang = currentLang * 10 + subtitles.get(subtitle, lambda: 9 if (currentLang >= voices[nativeVoice]()) else 0)()
		currentBitrate = qualities.get(video['mainQuality']['code'], 0)
		if currentLang > storedLang or (currentLang == storedLang and currentBitrate > bitrate):
			storedLang = currentLang
			bitrate = currentBitrate
			result = {'url':video['url'], 'type': 'video', 'stream':'hls'}
	return {'media': [result]} if result else None
