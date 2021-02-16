# -*- coding: utf-8 -*-
import sys
from datetime import date, timedelta
import libwdrparser as libWdrParser
import libwdrjsonparser as libWdrJsonParser
import libwdrrssparser as libWdrRssParser
import libwdrrssandroidparser as libWdrRssAndroidParser
import libwdrhtmlparser as libWdrHtmlParser
import libmediathek3 as libMediathek

ignoreLetters=['#']

translation = libMediathek.getTranslation
params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'libWdrListMain', 'libWdrPlay', 'libWdrPlayJs')

def libWdrListMain():
	libMediathek.searchWorkaroundRemove()
	l = []
	#l.append({'_name':translation(31030), 'mode':'libWdrListFeed', 'url':'http://www1.wdr.de/mediathek/video/sendungverpasst/sendung-verpasst-100~_format-mp111_type-rss.feed', '_type':'dir'})
	#l.append({'_name':translation(31030), 'mode':'libWdrListVideos', 'id':'sendung-verpasst-100', '_type':'dir'})
	l.append({'_name':translation(31032), 'mode':'libWdrListLetters', '_type':'dir'})
	#l.append({'_name':translation(31033), 'mode':'libWdrListDate', '_type':'dir'})
	#l.append({'name':'Videos in Gebärdensprache', 'mode':'libWdrListFeed', 'url':'http://www1.wdr.de/mediathek/video/sendungen/videos-dgs-100~_format-mp111_type-rss.feed', '_type':'dir'})
	#l.append({'name':'Videos mit Untertiteln', 'mode':'libWdrListFeed', 'url':'http://www1.wdr.de/mediathek/video/sendungen/videos-untertitel-100~_format-mp111_type-rss.feed', '_type':'dir'})
	l.append({'_name':translation(31039), 'mode':'libWdrListSearch', '_type':'dir'})
	return l

def libWdrListLetters():
	return libMediathek.populateDirAZ('libWdrListShows',ignoreLetters)

def libWdrListShows():
	#return libWdrParser.parseShows('http://www1.wdr.de/mediathek/video/sendungen-a-z/sendungen-'+params['name'].lower()+'-102.html')
	return libWdrRssAndroidParser.parseShows(params['name'].lower())

def libWdrListVideos():
	#return libWdrRssParser.parseVideos(params['url'])
	#return libWdrRssAndroidParser.parseVideos(params['id'])

	url = 'http://www1.wdr.de/'+params['id']+'~_variant-android.mobile'
	if 'grepShowFromVideo' in params:
		return libWdrRssAndroidParser.parseVideos(url,'video',grepShowFromVideo=True)
	else:
		return libWdrRssAndroidParser.parseVideos(url,'video')

def libWdrListFeed():
	return libWdrRssParser.parseFeed(params['url'])

def libWdrListDate():
	return libMediathek.populateDirDate('libWdrListDateVideos')

def libWdrListDateVideos():
	if 'datum' in params:
		day = date.today() - timedelta(int(params['datum']))
		ddmmyyyy = day.strftime('%d%m%Y')
	else:
		ddmmyyyy = libMediathek.dialogDate()
	url = 'http://www1.wdr.de/mediathek/video/sendungverpasst/sendung-verpasst-100~_tag-'+ddmmyyyy+'_variant-android.mobile'
	#return libWdrRssParser.parseFeed(url,'video')
	return libWdrRssAndroidParser.parseVideos(url,'date')

def libWdrListSearch():
	search_string = params.get('searchString', None)
	if search_string is None:
		search_string = libMediathek.getSearchString()
	return libWdrHtmlParser.parse(
		"http://www1.wdr.de/mediathek/video/suche/avsuche100~suche_parentId-videosuche100.html?pageNumber=1&sort=date&q="+search_string\
	) if search_string else None

def libWdrPlay():
	if 'm3u8' in params:
		result = {}
		result['media'] = []
		#d['media'].append({'url':params['m3u8'], 'type': 'video', 'stream':'hls'})
		result['media'].append({'url':params['m3u8'], 'type': 'video', 'stream':'mp4'})
	else:
		result = libWdrParser.parseVideo(params['url'])
	result = libMediathek.getMetadata(result)
	return result

def libWdrPlayJs():
	result = libWdrParser.parseVideoJs(params['url'])
	result = libMediathek.getMetadata(result)
	return result

modes = {
	'libWdrListMain': libWdrListMain,
	'libWdrListLetters': libWdrListLetters,
	'libWdrListShows': libWdrListShows,
	'libWdrListVideos': libWdrListVideos,
	'libWdrListFeed': libWdrListFeed,
	'libWdrListDate': libWdrListDate,
	'libWdrListDateVideos': libWdrListDateVideos,
	'libWdrListSearch': libWdrListSearch,
	'libWdrPlay': libWdrPlay,
	'libWdrPlayJs': libWdrPlayJs,
}
