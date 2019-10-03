# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek

base = 'https://sr-mediathek.de/API'
#base = 'http://dev.sr-mediathek.sr-multimedia.de/API'

def getShows():
	url = base + '/sendereihe.json.js.php?az=1'
	l = []
	l += _getShowsSubset(url)
	l += _getShowsSubset(url+'&offset=50')
	l += _getShowsSubset(url+'&offset=100')
	return l
	
def _getShowsSubset(url):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for item in j:
		d = {}
		d['_name'] = item['s_name']
		d['_entries'] = item['s_anzahl']
		#d['s_id'] = item['s_id']
		d['_plot'] = item['s_beschreibung']
		d['urlargs'] = json.dumps({'az': '1','sendereihe': item['s_id']})
		d['_thumb'] = 'http://sr-mediathek.de/img/sendungen/'+item['s_id']+'~_v-sr_169_600.jpg'
		d['mode'] = 'libSrListVideos'
		d['_type'] = 'dir'
		if item['s_anzahl'] != '0':
			l.append(d)
	return l
	

def getTopics():
	#url = 'https://dev.sr-mediathek.sr-multimedia.de/API/themen.json.js.php'
	url = base + '/themen.json.js.php'
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for item in j:
		d = {}
		d['_name'] = item['t_name']
		d['_entries'] = item['t_anzahl']
		d['urlargs'] = json.dumps({'thema': item['t_kurz']})
		d['_plot'] = item['t_name']
		#d['_thumb'] = 'http://sr-mediathek.de/img/sendungen/'+item['t_kurz']+'~_v-sr_169_600.jpg'
		d['mode'] = 'libSrListVideos'
		d['_type'] = 'dir'
		if item['t_anzahl'] != '0':
			l.append(d)
	return l
	
	
"""
def getVideos(s_id):
	url = 'http://hbbtv.sr-mediathek.de/inc/sendungJSON.php?sid=' + s_id
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for entry in j:
		vid = _getDictVideos(entry)
		l.append(vid)
	return l
"""	
def getDate(day):
	response = libMediathek.getUrl('http://hbbtv.sr-mediathek.de/inc/SndvrpJSON.php')
	j = json.loads(response)
	l = []
	key = None
	if isinstance(j,list) or (isinstance(j,dict) and (int(day) in j)):
		key = int(day)
	elif isinstance(j,dict) and (day in j):
		key = day
	if not (key is None):
		for entry in j[key]:
			vid = _getDictVideos(entry,'date')
			l.append(vid)
	return l[::-1]
	
"""
def _getDictShows(jsonDict):
	d = {}
	d['_name'] = jsonDict['s_name']
	d['_entries'] = jsonDict['s_anzahl']
	d['s_id'] = jsonDict['s_id']
	d['_plot'] = jsonDict['s_beschreibung']
	d['_thumb'] = jsonDict['bild']
	d['mode'] = 'libSrListVideos'
	d['_type'] = 'dir'
	
	return d
"""
	
def _getDictVideos(jsonDict,type='video'):
	d = {}
	d['_name'] = jsonDict['ueberschrift']
	#d['url'] = 'http://sr_hls_od-vh.akamaihd.net/i/' + jsonDict['media_url_firetv']
	d['id'] = jsonDict['id']
	d['_plot'] = jsonDict['kompletttext']
	d['_mpaa'] = jsonDict['fsk']
	d['_thumb'] = jsonDict['bild']
	d['_aired'] = jsonDict['start'][:4] + '-' + jsonDict['start'][4:6] + '-' + jsonDict['start'][6:8]
	d['_airedtime'] = jsonDict['start'][8:10] + ':' + jsonDict['start'][10:12]
	#d['start'] = jsonDict['start']
	if 'playtime_hh' in jsonDict:
		d['_duration'] = str(int(jsonDict['playtime_hh']) * 3600 + int(jsonDict['playtime_mm']) * 60 + int(jsonDict['playtime_ss']))
	d['mode'] = 'libSrPlay'
	d['_type'] = type
	
	return d

def getSearch(a):
	libMediathek.log(a)
	urlargs = json.loads(a)
	i = 0
	args = ''
	for arg in urlargs:
		if i == 0:
			args += '?'
		else:
			args += '&'
		args += arg + '=' + urlargs[arg]
		i += 1
		
	url = 'https://www.sr-mediathek.de/API/suche.json.js.php'+args
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	for item in j:
		d = {}
		d['_name'] = item['ueberschrift']
		d['_plot'] = item['teasertext']
		d['id'] = item['id']
		if 'playtime_hh' in item:
			d['_duration'] = str(int(item['playtime_hh']) * 3600 + int(item['playtime_mm']) * 60 + int(item['playtime_ss']))
		d['_thumb'] = item['bild']
		if 'start' in item:
			d['_aired'] = item['start'][:4] + '-' + item['start'][4:6] + '-' + item['start'][6:8]
			d['_airedtime'] = item['start'][8:10] + ':' + item['start'][10:12]
		d['mode'] = 'libSrPlay'
		d['_type'] = 'video'
		l.append(d)
	return l
	
def getVideoUrl(id):
	response = libMediathek.getUrl('https://www.sr-mediathek.de/sr_player/mc.php?id='+id)
	j = json.loads(response)
	url = j['_mediaArray'][1]['_mediaStreamArray'][0]['_stream']
	d = {}
	d['media'] = []
	if j['_type'] == 'audio':
		d['media'].append({'url':url, 'stream':'MP4'})
	else:
		d['media'].append({'url':url, 'stream':'HLS'})
	return d