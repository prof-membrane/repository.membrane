# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
base = 'https://www.phoenix.de/response/template/'


def parseMain():
	response = libMediathek.getUrl(base+'vod_main_json')
	j = json.loads(response)
	l = []
	for i,item in enumerate(j['content']['items']):
		if item['videos']:
			d = {}
			d['name'] = item['titel']
			d['plot'] = item['typ']
			d['_type'] = 'dir'
			d['id'] = str(i)
			d['mode'] = 'listVideos'
			l.append(d)
	return l

def parseVideos(id):
	response = libMediathek.getUrl(base+'vod_main_json')
	j = json.loads(response)
	l = []
	if j != None:
		for item in j['content']['items'][int(id)]['videos']:
			d = {}
			d['name'] = item['title']
			if not d['name']:
				d['name'] = item['smubl']
			d['plot'] = item['text_vorspann']
			thumbnail_item = None
			if 'thumbnail_large' in item and item['thumbnail_large']:
				thumbnail_item = item['thumbnail_large']
			elif 'thumbnail_medium' in item and item['thumbnail_medium']:
				thumbnail_item = item['thumbnail_medium']
			if thumbnail_item:
				if 'systemurl' in thumbnail_item and thumbnail_item['systemurl']:
					d['thumb'] = 'https://www.phoenix.de' + thumbnail_item['systemurl']
				elif 'systemurl_gsid' in thumbnail_item and thumbnail_item['systemurl_gsid']:
					d['thumb'] = 'https://www.phoenix.de' + thumbnail_item['systemurl_gsid']
			d['_type'] = 'video'
			d['smubl'] = item['smubl']
			d['mode'] = 'play'
			l.append(d)
	return l

def getVideoUrl(smubl):
	response = libMediathek.getUrl('https://tmd.phoenix.de/tmd/2/ngplayer_2_3/vod/ptmd/phoenix/'+smubl)
	j = json.loads(response)
	for prio in j['priorityList']:
		if prio['formitaeten'][0]['mimeType'] == 'application/x-mpegURL':
			for quality in prio['formitaeten'][0]['qualities']:
				if quality['quality'] == 'auto':
					url = quality['audio']['tracks'][0]['uri']
	d = {}
	d['media'] = []
	d['media'].append({'url':url, 'type': 'video', 'stream':'hls'})
	return d
