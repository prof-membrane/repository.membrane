# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import re
import urllib
from operator import itemgetter
import sys
import xbmcplugin
import time
from datetime import date, datetime, timedelta


pluginhandle = int(sys.argv[1])
lang_german  = xbmcplugin.getSetting(pluginhandle,'lang') in ('de','0','',None)
current_lang = 'de' if lang_german else 'fr'

opa_url = 'https://api.arte.tv/api/opa/v3'
opa_token = {"Authorization": "Bearer Nzc1Yjc1ZjJkYjk1NWFhN2I2MWEwMmRlMzAzNjI5NmU3NWU3ODg4ODJjOWMxNTMxYzEzZGRjYjg2ZGE4MmIwOA"}

emac_url = 'https://api.arte.tv/api/emac/v3/' + current_lang + '/web'
emac_token = {"Authorization": "Bearer MWZmZjk5NjE1ODgxM2E0MTI2NzY4MzQ5MTZkOWVkYTA1M2U4YjM3NDM2MjEwMDllODRhMjIzZjQwNjBiNGYxYw"}

stream_params = '&quality=$in:XQ,HQ,SQ&mediaType=hls&language=' + current_lang + '&channel=' + current_lang.upper()


def str_to_airedtime(airedtime_str):
	if not airedtime_str:	# check for None or empty string
		return None
	start = airedtime_str.split('+')
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
	result = airedtime.strftime('%H:%M')
	return result


def _parse_data(video):
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
	if 'broadcastDates' in video:
		airedtime = str_to_airedtime(video['broadcastDates'][0])
		d['_airedtime'] = airedtime 
		d['name'] = '(' + airedtime + ') ' + d['name']
	if video['images']['landscape']:
		max_res = max(video['images']['landscape']['resolutions'], key=lambda item: item['w'])
		d['thumb'] = max_res['url']
	elif video['images']['portrait']:
		max_res = max(video['images']['portrait']['resolutions'], key=lambda item: item['h'])
		d['thumb'] = max_res['url']
	if video['kind']['isCollection']:
		d['mode'] = 'libArteListCollection'
		d['url'] = '/programs?programId=' + video['programId'] + '&language=' + current_lang + '&fields=children,programId'
		d['_type'] = 'dir'
	else:
		d['url'] = '/videoStreams?programId=' + video['programId'] + stream_params + '&kind=' + video['kind']['code']
		d['mode'] = 'libArtePlay'
		d['_type'] = 'video'
		d['_duration'] = video['duration']
	return d


def getVideos(url):
	l = []
	url = emac_url + url
	response = libMediathek.getUrl(url, emac_token)
	j = json.loads(response)
	for video in j['data']:
		l.append(_parse_data(video))
	return l


def getCollection(url):
	url = opa_url + url
	response = libMediathek.getUrl(url, opa_token)
	j = json.loads(response)
	program_id = j['programs'][0]['programId']
	l = getVideos('/zones/collection_videos?id=' + program_id)
	children = j['programs'][0]['children']
	topics = [item for item in children if item['kind'] == 'TOPIC']
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
		l.append(_parse_data(video))
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

def getVideoUrl(url):
	result = None
	url = opa_url + url
	response = libMediathek.getUrl(url, opa_token)
	j = json.loads(response)
	storedLang = 0
	bitrate = 0
	hls_videos = [value for value in j['videoStreams'] if value['mediaType'] == 'hls']
	for video in hls_videos:
		voice_subtitle = video['audioCode'].split('-');
		voice = voice_subtitle[0].split('[')[0]
		subtitle = voice_subtitle[1].split('[')[0] if len(voice_subtitle) > 1 else '';
		currentLang = voices.get(voice,lambda:0)()
		# if currentLang is native language => prefer "no subtitle"
		# if currentLang is foreign language => prefer subtitle in native language
		currentLang = currentLang * 10 + subtitles.get(subtitle, lambda: 9 if (currentLang >= voices[nativeVoice]()) else 0)()
		currentBitrate = video['bitrate']
		if currentLang > storedLang or (currentLang == storedLang and currentBitrate > bitrate):
			storedLang = currentLang
			bitrate = currentBitrate
			result = {'url':video['url'], 'type': 'video', 'stream':'HLS'}
	return {'media': [result]} if result else None
