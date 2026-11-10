#!/usr/bin/python
# -*- coding: utf-8 -*-
import libardjsonparserneu as libArdJsonParserNeu
import libmediathek3 as libMediathek

params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'libArdListMainMobile', *playModes)

def libArdListMainMobile():
	l = []
	translation = libMediathek.getTranslation
	l.append({'sort':'31032', 'name':translation(31032), 'mode':'libArdListChannelShows', '_type':'dir'})
	l.append({'sort':'31033', 'name':translation(31033), 'mode':'libArdListChannelDates', '_type':'dir'})
	l.append({'sort':'31036', 'name':translation(31036), 'mode':'libArdListChannelLivestreams', '_type':'dir'})
	l.append({'sort':'31039', 'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListChannels():
	l = []
	mode = params['mode']
	for i, channel in enumerate(channels):
		d = {}
		if (mode == 'libArdListChannelShows') and (channel[1] & ondemand):
			d['mode'] = 'libArdListShowsByChannel'
		elif (mode == 'libArdListChannelDates') and (channel[1] & bydate):
			d['mode'] = 'libArdListDateByChannel'
		elif (mode == 'libArdListChannelLivestreams') and (channel[1] & (live_byclient + live_byard)):
			d['mode'] = 'libArdListLivestreamsOfChannel'
		else:
			d['mode'] = None
		if d['mode']:
			d['_name'] = channel[0]
			d['_type'] = 'dir'
			d['channel'] = str(i)
			l.append(d)
	return l

def libArdListShowsByChannel():
	return libMediathek.populateDirAZ('libArdListShowVideosOfChannel', ['#'], params['channel'])

def libArdListDateByChannel():
	return libMediathek.populateDirDate('libArdListDateVideosOfChannel', params['channel'])

def libArdListLivestreamsOfChannel():
	channel = channels[int(params['channel'])]
	# Livestreams sind nicht sinnvoll vorsortiert
	libMediathek.sortAZ()
	return libArdJsonParserNeu.parseLivestreams(channel[2], 'ard' if (channel[1] & live_byard) else channel[3])

def libArdListShowVideosOfChannel():
	channel = channels[int(params['channel'])]
	partnerKey = channel[2]
	letter = params['name'].upper()
	return libArdJsonParserNeu.parseAZ(partnerKey, channel[3], letter)

def libArdListDateVideosOfChannel():
	channel = channels[int(params['channel'])]
	partnerKey = channel[2]
	return libArdJsonParserNeu.parseDate(partnerKey, channel[3], params['yyyymmdd'])

def libArdListSearch():
	search_string = libMediathek.getSearchString()
	if search_string:
		return libArdJsonParserNeu.parseSearchAPI(search_string)
	else:
		return None

def libArdListShow():
	return libArdJsonParserNeu.parseShow(params['documentId'])

def libArdPlay():
	result = libArdJsonParserNeu.getVideoUrl(params['url'])
	result = libMediathek.getMetadata(result)
	return result

ondemand =      (1<<0)
bydate =        (1<<1)
live_byclient = (1<<2)
live_byard =    (1<<3)

channels = (
#	(name,            flags,                              partnerKey,     clientKey)
	('Alle Sender',   ondemand + bydate + live_byard,     None,           'ard'),
	('Das Erste',     ondemand + bydate + live_byard,     'das_erste',    'daserste'),
	('BR',            ondemand + bydate + live_byclient,  'br',           'br'),
	('HR',            ondemand + bydate + live_byard,     'hr',           'hr'),
	('MDR',           ondemand + bydate + live_byclient,  'mdr',          'mdr'),
	('NDR',           ondemand + bydate + live_byclient,  'ndr',          'ndr'),
	('Radio Bremen',  ondemand + bydate + live_byard,     'radio_bremen', 'radiobremen'),
	('RBB',           ondemand + bydate + live_byclient,  'rbb',          'rbb'),
	('SR',            ondemand + bydate + live_byard,     'sr',           'sr'),
	('SWR',           ondemand + bydate + live_byclient,  'swr',          'swr'),
	('WDR',           ondemand + bydate + live_byard,     'wdr',          'wdr'),
	('One',           ondemand + bydate + live_byard,     'one',          'one'),
	('ARD-alpha',     ondemand + bydate + live_byard,     'ard-alpha',    'alpha'),
	('Phoenix',       ondemand + bydate + live_byard,     'phoenix',      'phoenix'),
	('Tagesschau24',  ondemand + bydate + live_byclient,  'tagesschau24', 'tagesschau24'),
	('3sat',          bydate + live_byard,                '3sat',         '3sat'),
	('Arte',          bydate + live_byard,                'arte',         'arte'),
	('KiKA',          bydate + live_byard,                'KiKa',         'kika'),
	('Deutsche Welle',live_byard,                         'dw',           None),
)

modes = {
	'libArdListMainMobile':           ( libArdListMainMobile, 'videos' ),
	'libArdListChannelShows':         ( libArdListChannels, 'videos' ),
	'libArdListChannelDates':         ( libArdListChannels, 'videos' ),
	'libArdListChannelLivestreams':   ( libArdListChannels, 'videos' ),
	'libArdListShowsByChannel':       ( libArdListShowsByChannel, 'videos' ),
	'libArdListDateByChannel':        ( libArdListDateByChannel, 'videos' ),
	'libArdListLivestreamsOfChannel': ( libArdListLivestreamsOfChannel, 'videos' ),
	'libArdListShowVideosOfChannel':  ( libArdListShowVideosOfChannel, 'movies' ),
	'libArdListDateVideosOfChannel':  ( libArdListDateVideosOfChannel, 'movies' ),
	'libArdListSearch':               ( libArdListSearch, 'movies' ),
	'libArdListShow':                 ( libArdListShow, 'movies' ),
	'libArdPlay':                     ( libArdPlay, None ),
}

playModes = ('libArdPlay', )
