# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import re
import urllib
from operator import itemgetter
#import xml.etree.ElementTree as ET


def getVideos(url):
	l = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	for video in j['videos']:
		d = {}
		#d['_name'] = video['title']
		if video['subtitle'] != None:
			d['_name'] = video['subtitle']
		else:
			d['_name'] = video['title']

		d['_tvshowtitle'] = video['title']
		if video['imageUrl'] != None:
			d['_thumb'] = video['imageUrl']
		if video['durationSeconds'] != None:
			d['_duration'] = str(video['durationSeconds'])
		if video['teaserText'] != None:
			d['_plotoutline'] = video['teaserText']
			d['_plot'] = video['teaserText']
		if video['fullDescription'] != None:
			d['_plot'] = video['fullDescription']
		elif video['shortDescription'] != None:
			d['_plot'] = video['shortDescription']
		#d['url'] = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/streams/'+video['programId']+'/'+video['kind']+'/'+video['platform']+'/de/DE'
		d['url'] = 'https://api.arte.tv/api/player/v1/config/de/'+video['programId']+'?autostart=0&lifeCycle=1&lang=de_DE&config=arte_tvguide'
		d['mode'] = 'libArtePlay'
		d['_type'] = 'date'
		l.append(d)
	if j['meta']['page'] < j['meta']['pages']:
		d = {}
		d['url'] = url.split('&page=')[0] + '&page=' + str(j['meta']['page'] + 1)
		d['_type'] = 'nextPage'
		d['mode'] = 'libArteListVideos'
		l.append(d)
	return l

def getAZ():
	l = []
	response = libMediathek.getUrl('http://www.arte.tv/hbbtvv2/services/web/index.php/EMAC/teasers/home/de')
	j = json.loads(response)
	for mag in j['teasers']['magazines']:
		d = {}
		d['_name'] = mag['label']['de']
		d['url'] = 'http://www.arte.tv/hbbtvv2/services/web/index.php/' + mag['url'] + '/de'
		d['_type'] = 'dir'
		d['mode'] = 'libArteListVideos'
		l.append(d)
	return l

def getPlaylists():#,playlists, highlights
	l = []
	response = libMediathek.getUrl('http://www.arte.tv/hbbtvv2/services/web/index.php/EMAC/teasers/home/de')
	j = json.loads(response)
	for playlist in j['teasers']['highlights']:
		d = {}
		d['_name'] = playlist['title']
		d['_subtitle'] = playlist['subtitle']
		d['_thumb'] = playlist['imageUrl']
		d['_plot'] = playlist['teaserText']
		d['url'] = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/v3/videos/collection/PLAYLIST/' + playlist['programId'] + '/de'
		d['_type'] = 'dir'
		d['mode'] = 'libArteListVideos'
		l.append(d)
	return l



def getDate(yyyymmdd):
	l = []
	response = libMediathek.getUrl('http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/programs/'+yyyymmdd+'/de')
	j = json.loads(response)
	for program in j['programs']:
		if program['video'] != None:
			d = {}
			#d['_airedtime'] = program['broadcast']['broadcastBeginRounded'].split(' ')[-2][:5]
			s = program['broadcast']['broadcastBeginRounded'].split(' ')[-2].split(':')
			d['_airedtime'] = s[0] + ':' + s[1]
			d['_name'] = program['program']['title']
			#d['url'] = 'http://www.arte.tv/papi/tvguide/videos/stream/player/D/'+program['video']['emNumber']+'_PLUS7-D/ALL/ALL.json'
			#d['url'] = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/streams/'+program['video']['programId']+'/SHOW/ARTEPLUS7/de/DE'
			#d['url'] = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/streams/'+program['video']['programId']+'/'+program['video']['kind']+'/'+program['video']['platform']+'/de/DE'

			d['url'] = 'https://api.arte.tv/api/player/v1/config/de/'+program['video']['programId']+'?autostart=0&lifeCycle=1&lang=de_DE&config=arte_tvguide'
			#d['programId'] = program['video']['programId']

			if program['video']['imageUrl'] != None:
				d['_thumb'] = program['video']['imageUrl']
			if program['video']['durationSeconds'] != None:
				d['_duration'] = str(program['video']['durationSeconds'])
			if program['video']['teaserText'] != None:
				d['_plotoutline'] = program['video']['teaserText']
				d['_plot'] = program['video']['teaserText']
			if program['video']['fullDescription'] != None:
				d['_plot'] = program['video']['fullDescription']
			d['mode'] = 'libArtePlay'
			d['_type'] = 'date'
			l.append(d)
	return l

def getSearch(s):
	l = []
	url = 'http://www.arte.tv/hbbtvv2/services/web/index.php/OPA/v3/videos/search/text/'+urllib.quote_plus(s)+'/de'
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	for video in j['teasers']:
		d = {}
		d['_name'] = video['title']

		d['_tvshowtitle'] = video['title']
		if video['imageUrl'] != None:
			d['_thumb'] = video['imageUrl']
		d['url'] = 'https://api.arte.tv/api/player/v1/config/de/'+video['programId']+'?autostart=0&lifeCycle=1&lang=de_DE&config=arte_tvguide'
		d['mode'] = 'libArtePlay'
		d['_type'] = 'date'
		l.append(d)
	return l
preferences = {
				'ignore':0,
				'FR':1,
				'AUD':2,
				'OV':3,
				'OMU':4,
				'DE':5,}

languages = {
				'FR':'FR',
				'OMU':'DE',
				'DE':'DE'}

bitrates = {
				'EQ':800,
				'HQ':1500,
				'SQ':2200,}

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

lang = {
		'VO':'ov',
		'OmU':'ov',
		'VA':'de',
		'VF':'fr',
		'VA-STA':'de',
		'VF-STF':'fr',

		'VOA':'de',
		'VOF':'fr',
		'VOA-STA':'omu',
		'VOA-STE':'omu',
		'VOF-STA':'omu',
		'VOF-STE':'omu',
		'VAAUD':'aud',
		'VFAUD':'aud',
		'VE[ANG]':'en',
		'VE[ESP]':'es',
		'VE[POL]':'pl',

		'STA':'de',
		'STF':'fr',
		'STMA':'de',
		'STMF':'fr',
		'STE[ANG]':'en',
		'STE[ESP]':'es',
		'STE[POL]':'pl',
}
def getVideoUrl(url):
	d = {}
	d['media'] = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	storedLang = 0
	for stream in j['videoStreams']:
		properties = {}
		properties['url'] = stream['url']
		properties['bitrate'] = bitrates[stream['quality']]

		s = stream['audioCode'].split('-')
		properties['lang'] = lang[s[0]]
		if s[0] == 'VAAUD' or s[0] == 'VFAUD':
			properties['audiodesc'] = True
		if len(s) > 1:
			properties['subtitlelang'] = lang[s[1]]
			if s[1] == 'STMA' or s[1] == 'STMF':
				properties['sutitlemute'] = True

		properties['type'] = 'video'
		properties['stream'] = 'MP4'
		d['media'].append(properties)
	return d

def getVideoUrlWeb(url):
	d = {}
	d['media'] = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	#for caption in j.get('captions',[]):
	#	if caption['format'] == 'ebu-tt-d-basic-de':
	#		d['subtitle'] = [{'url':caption['uri'], 'type':'ttml', 'lang':'de', 'colour':True}]
	#	#elif caption['format'] == 'webvtt':
	#	#	d['subtitle'] = [{'url':caption['uri'], 'type':'webvtt', 'lang':'de', 'colour':False}]
	storedLang = 0
	bitrate = 0
	# oh, this is such bullshit. there are endless and senseless permutations of language/subtitle permutations.
	# i'll have to rewrite this in the future for french and other languages, subtitles, hearing disabled, ...
	# who the hell uses baked in subtitles in 2017?!?!
	result = None
	for key in j['videoJsonPlayer']['VSR']:
		if j['videoJsonPlayer']['VSR'][key]['mediaType'] == 'hls':
			l = lang.get(j['videoJsonPlayer']['VSR'][key]['versionCode'].split('[')[0],'ignore').upper()
			currentLang = preferences.get(l,0)
			currentBitrate = j['videoJsonPlayer']['VSR'][key]['bitrate']
			if currentLang > storedLang or (currentLang == storedLang and currentBitrate > bitrate):
				storedLang = currentLang
				bitrate = currentBitrate
				result = {'url':j['videoJsonPlayer']['VSR'][key]['url'], 'type': 'video', 'stream':'HLS'}

	if result is None:
		return None

	d['media'].append(result)

	d['metadata'] = {}
	d['metadata']['name'] = j['videoJsonPlayer']['VTI']
	if 'VDE' in j['videoJsonPlayer']:
		d['metadata']['plot'] = j['videoJsonPlayer']['VDE']
	elif 'V7T' in j['videoJsonPlayer']:
		d['metadata']['plot'] = j['videoJsonPlayer']['V7T']
	d['metadata']['thumb'] = j['videoJsonPlayer']['VTU']['IUR']
	d['metadata']['duration'] = str(j['videoJsonPlayer']['videoDurationSeconds'])
	return d