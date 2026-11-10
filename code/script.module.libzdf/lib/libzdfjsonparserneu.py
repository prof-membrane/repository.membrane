#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
from datetime import date
import libmediathek3 as libMediathek
import libmediathek3utils as utils
import xbmcaddon


if sys.version_info[0] < 3: # for Python 2
	from urllib import urlencode
else: # for Python 3
	from urllib.parse import urlencode
	from functools import reduce

addon = xbmcaddon.Addon()
baseUrlJson = 'https://zdf-prod-futura.zdf.de/mediathekV2/'


def deep_get(dictionary, keys, default = None):
	return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split('.'), dictionary)


def parseLivestreams():
	result = []
	snapshot_file = 'livestream.json'
	livestream_via_api = libMediathek.getSettingBool('livestream_via_api')
	if livestream_via_api: 
		day = date.today()
		yyyymmdd = day.strftime('%Y-%m-%d')
		url = baseUrlJson + 'live-tv/' + yyyymmdd
		response = libMediathek.getUrl(url)
		# url = (
		# 	"https://api.zdf.de/tmd/2/ngplayer_2_3/live/ptmd/%s"
		# 	 % ["247onAir-201", "247onAir-202", "247onAir-203", "247onAir-204", "247onAir-205", "247onAir-206", "247onAir-207", "247onAir-208"]
		# )  
		# import libzdfjsonparser
		# response = libzdfjsonparser.getU(url)
		j = json.loads(response)
		epgCluster = j.get('epgCluster',None)
		if epgCluster:
			for livestreams in epgCluster:
				item = livestreams.get('liveStream',None)
				if item:
					documentId = item['externalId']
					name = item['titel']
					if documentId and name:
						d = {}
						d['documentId'] = documentId
						d['name'] = name
						formitaeten = parseFormitaeten(item,'live')
						if formitaeten:
							fm0 = formitaeten['media'][0]
							d['url'] = fm0['url']
							d['_type'] = fm0['type']
							d['stream'] = fm0['stream']
						else:
							continue
						d['plot'] = item.get('headline','')
						if d['plot']:
							d['plot'] = '[B]' + d['plot'] + '[/B][CR]'
						d['plot'] = d['plot'] + item.get('beschreibung',None)
						thumb = deep_get(item, 'teaserBild.1280.url')
						if not thumb:
							thumb = deep_get(item, 'teaserBild.768.url')
						if not thumb:
							thumb = deep_get(item, 'teaserBild.640.url')
						if thumb:
							d['thumb'] = thumb
						d['mode'] = 'libZdfPlayLivestream'
						d['live'] = 'true'
						result.append(d)
		utils.f_mkdir(utils.pathUserdata(''))
		if result:
			utils.f_write(utils.pathUserdata(snapshot_file), json.dumps(result))
		else:
			try:
				result = json.loads(utils.f_open(utils.pathUserdata(snapshot_file)))
				for item in result:
					item['name'] += ' (Snapshot)'
			except:
				pass
	else:
		livestream_from_addondata = libMediathek.getSettingBool('livestream_from_addondata')
		if livestream_from_addondata: 
			result = json.loads(utils.f_open(utils.pathUserdata(snapshot_file)))
		else:
			result = json.loads(utils.f_open(utils.pathAddon('/resources/' + snapshot_file)))

	return result


def parseDate(channel, date):
	url = baseUrlJson + 'broadcast-missed/' + date	# date = YYYY-MM-DD
	return parse(url, channel, 'broadcastCluster')


def parseRubrics():
	url = baseUrlJson + 'categories-overview'
	return parse(url, '', 'cluster')


def parseCategory(url):
	return parse(url, '', 'cluster')


def parseSearch(search_string):
	url = baseUrlJson + 'search?contentTypes=episode,clip,brand,match&q=' + search_string 
	return parse(url, '', 'results', isSearch = True)


def parse(url, channel, clusterkey, isSearch = False):
	result = []
	categoriesAllowed = True
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	cluster = j.get(clusterkey,None)
	if cluster:
		for clusterItem in cluster:
			if isSearch or (clusterItem.get('type','').startswith('teaser')):
				if isSearch:
					teaser = [clusterItem]
				else:
					teaser = clusterItem.get('teaser',None)
				if teaser:
					for item in teaser:
						documentId = item['externalId']
						name = item['titel']
						if documentId and name:
							d = {}
							d['documentId'] = documentId
							d['name'] = name
							episodeNumber = item.get('episodeNumber', None)
							if episodeNumber:
								d['name'] = 'Folge ' + str(episodeNumber) + ' - ' + d['name']
							if item.get('seasonNumber', None):
								d['name'] = item.get('headline','') + ' - ' + d['name']
							currentChannel = item.get('channel',None)
							if channel is None:
								if currentChannel:
									# import libzdfneu
									# d['name'] = d['name'] + ' | [COLOR blue]' + next((x[0] for x in libzdfneu.channels if x[2] == currentChannel), '') + '[/COLOR]'
									d['name'] = d['name'] + ' | [COLOR blue]' + currentChannel + '[/COLOR]'
							elif channel:
								if channel != currentChannel:
									continue
							d['url'] = item['url']
							d['plot'] = item.get('headline','')
							if d['plot']:
								d['plot'] = '[B]' + d['plot'] + '[/B][CR]'
							d['plot'] = d['plot'] + item.get('beschreibung','')
							availableTo = item.get('timetolive',None)
							if availableTo:
								d['plot'] = '[COLOR blue]' + addon.getLocalizedString(32013) + ' ' + availableTo.split()[0]  + ' | [/COLOR]' + d.get('plot','')
							if channel == '':
								broadcastedOn = item.get('airtime',None)
								if broadcastedOn:
									d['plot'] = '[COLOR blue]' + addon.getLocalizedString(32012) + ' ' + broadcastedOn.split()[0]  + ' | [/COLOR]' + d.get('plot','')
							duration = item.get('length', None)
							if duration:
								d['_duration'] = str(duration)
							thumb = deep_get(item, 'teaserBild.1280.url')
							if not thumb:
								thumb = deep_get(item, 'teaserBild.768.url')
							if not thumb:
								thumb = deep_get(item, 'teaserBild.640.url')
							if thumb:
								d['thumb'] = thumb
							type = item.get('type',None)
							# "category" "video" "brand" "topic"
							if categoriesAllowed and (type == 'category' or type == 'brand'):
								d['_type'] = 'dir'
								d['mode'] = 'libZdfListCategory'
							elif type == 'video':
								categoriesAllowed = False
								d['_type'] = 'date'
								d['mode'] = 'libZdfPlayNeu'
								airtime = item.get('airtime', None)
								if airtime:
									d['airedtime'] = airtime.split(' ')[1]
							else:
								continue
							result.append(d)
	return result


def parseVideo(url):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	document = j.get('document',None)
	if document:
		media = parseFormitaeten(document,document['type'])
		return media
	else:
		return None


def parseFormitaeten(video,type):
	mediaHLS = []
	mediaMP4 = []
	formitaeten = video.get('formitaeten',None)
	if formitaeten:
		for stream in formitaeten:
			if (stream.get('type',None) == 'h264_aac_ts_http_m3u8_http'
				or
				stream.get('mimeType',None) == 'application/x-mpegURL'
			):
				streamType = 'hls'
				media = mediaHLS
			elif (stream.get('type',None) == 'h264_aac_mp4_http_na_na'
				or
				stream.get('mimeType',None) == 'video/mp4'
			):
				streamType = 'mp4'
				media = mediaMP4
			else:
				continue
			try:
				quality = ('low','med','high','veryhigh','auto').index(stream['quality'])
			except ValueError:
				pass
			else:
				media.append({'url':stream['url'], 'type':type, 'stream':streamType, 'bitrate':quality})
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
