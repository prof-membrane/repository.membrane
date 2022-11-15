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

opa_url = 'https://api.arte.tv/api/opa/v3'
opa_token = {"Authorization": "Bearer Nzc1Yjc1ZjJkYjk1NWFhN2I2MWEwMmRlMzAzNjI5NmU3NWU3ODg4ODJjOWMxNTMxYzEzZGRjYjg2ZGE4MmIwOA"}

emac_url = 'https://api.arte.tv/api/emac/v3/' + current_lang + '/web'
emac_token = {"Authorization": "Bearer MWZmZjk5NjE1ODgxM2E0MTI2NzY4MzQ5MTZkOWVkYTA1M2U4YjM3NDM2MjEwMDllODRhMjIzZjQwNjBiNGYxYw"}

magazines_url = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/v3/magazines/' +  current_lang;

stream_params = '&quality=$in:XQ,HQ,SQ&mediaType=hls&language=' + current_lang + '&channel=' + current_lang.upper()


def _parse_data(video, isByDate = False):
	d = {}
	if video['subtitle'] and video['title']:
		d['name'] = video['title'] + ' | ' + video['subtitle']
	elif video['subtitle']:
		d['name'] = video['subtitle']
	else:
		d['name'] = video['title']
	if 'fullDescription' in video and video['fullDescription']:
		d['plot'] = video['fullDescription']
	elif 'description' in video and video['description']:
		d['plot'] = video['description']
	elif video['shortDescription']:
		d['plot'] = video['shortDescription']
	if isByDate and ('broadcastDates' in video):
		d['_airedISO8601'] = video['broadcastDates'][0]
	if 'images' in video and video['images']:
		if video['images']['landscape']:
			max_res = max(video['images']['landscape']['resolutions'], key=lambda item: item['w'])
			d['thumb'] = max_res['url']
		elif video['images']['portrait']:
			max_res = max(video['images']['portrait']['resolutions'], key=lambda item: item['h'])
			d['thumb'] = max_res['url']
	if video['kind'] == "MAGAZINE" or ('isCollection' in video['kind'] and video['kind']['isCollection']):
		d['mode'] = 'libArteListCollection'
		d['documentId'] = video['programId']
		d['url'] = '/programs?programId=' + video['programId'] + '&language=' + current_lang + '&fields=children,programId'
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
	for video in j['data']:
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


def getCollection(url):
	url = opa_url + url
	response = libMediathek.getUrl(url, opa_token)
	j = json.loads(response)
	program_id = j['programs'][0]['programId']
	l = getVideos('/zones/collection_videos?id=' + program_id)
	children = j['programs'][0]['children']
	topics = [item for item in children if (item['kind'] == 'TOPIC' or item['kind'] == 'TV_SERIES')]
	for topic in topics:
		subresponse = libMediathek.getUrl(
			opa_url + '/programs?programId=' + topic['programId'] + '&language=' + current_lang +
			'&fields=title,subtitle,fullDescription,shortDescription,mainImage.url', opa_token
		)
		topic_json = json.loads(subresponse)
		program = topic_json['programs'][0]
		if program['title'] in ('**', '', None):
			break
		d = {}
		d['name'] = program['title']
		if program['subtitle'] != None:
			d['name'] = d['name'] + ' | ' + program['subtitle']
		if program['fullDescription']:
			d['plot'] = program['fullDescription']
		elif program['shortDescription']:
			d['plot'] = program['shortDescription']
		d['thumb'] = program['mainImage']['url']
		d['_type'] = 'dir'
		d['mode'] = 'libArteListVideos'
		d['url'] = '/zones/collection_subcollection?id=' + topic['programId']
		l.append(d)
	return l


def getDate(yyyymmdd):
	l = []
	# this would be the better endpoint, but it's not working: /zones/listing_TV_GUIDE?day=
	url = emac_url + '/TV_GUIDE?day=' + yyyymmdd
	response = libMediathek.getUrl(url, emac_token)
	j = json.loads(response)
	data = j['zones'][1]['data']
	videos = [video for video in data if video['programId']]
	for video in videos:
		l.append(_parse_data(video, True))
	return l


def getSearch(s):
	return getVideos('/zones/listing_SEARCH?limit=99&query=' + s)


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
	'VO':   lambda: 1,                        # Original Voice
	'VE':   lambda: 2,                        # Other Voice
	'VFAUD':lambda: 3 if lang_german else 6,  # Audio Description Francaise
	'VOF':  lambda: 4 if lang_german else 7,  # Original Voice Francaise
	'VF':   lambda: 5 if lang_german else 8,  # Voice Francaise
	nativeVoice:  lambda: 6,                  # Internal use
	'VAAUD':lambda: 6 if lang_german else 3,  # Audio Description Allemande
	'VOA':  lambda: 7 if lang_german else 4,  # Original Voice Allemande
	'VA':   lambda: 8 if lang_german else 5,  # Voice Allemande
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
	url = opa_url + url
	response = libMediathek.getUrl(url, opa_token)
	j = json.loads(response)
	if len(j['videoStreams']) > 0:
		storedLang = 0
		bitrate = 0
		hls_videos = [value for value in j['videoStreams'] if value['mediaType'] == 'hls']
		for video in hls_videos:
			voice_subtitle = video['audioCode'].split('-');
			voice = voice_subtitle[0].split('[')[0]
			subtitle = voice_subtitle[1].split('[')[0] if len(voice_subtitle) > 1 else '';
			currentLang = voices.get(voice, lambda:0)()
			# if currentLang is native language => prefer "no subtitle"
			# if currentLang is foreign language => prefer subtitle in native language
			currentLang = currentLang * 10 + subtitles.get(subtitle, lambda: 9 if (currentLang >= voices[nativeVoice]()) else 0)()
			currentBitrate = video['bitrate']
			if currentLang > storedLang or (currentLang == storedLang and currentBitrate > bitrate):
				storedLang = currentLang
				bitrate = currentBitrate
				result = {'url':video['url'], 'type': 'video', 'stream':'hls'}
		return {'media': [result]} if result else None
	else:
		url = 'https://api.arte.tv/api/player/v2/config/' + current_lang + '/' + documentId
		response = libMediathek.getUrl(url)
		j = json.loads(response)
		storedLang = 0
		bitrate = 0
		hls_videos = [value for value in j['data']['attributes']['streams'] if value['protocol'][0:3] == 'HLS']
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

