#!/usr/bin/python
# -*- coding: utf-8 -*-
import libardjsonparserneu as libArdJsonParserNeu
import libmediathek3 as libMediathek

def list():
	return libMediathek.list(modesNeu, 'libArdListMainNeu', 'libArdPlay', 'libArdPlayHtml')

def libArdListMainNeu():
	l = []
	translation = libMediathek.getTranslation
	l.append({'name':translation(31032), 'mode':'libArdListChannelShows', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannelDates', '_type':'dir'})
	l.append({'name':translation(31036), 'mode':'libArdListChannelLivestreams', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListChannels():
	l = []
	params = libMediathek.get_params()
	mode = params['mode']
	for i, channel in enumerate(channels):
		d = {}
		if (mode == 'libArdListChannelShows') and (channel[1] & ondemand):
			d['mode'] = 'libArdListShowsByChannel'
		elif (mode == 'libArdListChannelDates') and (channel[1] & bydate):
			d['mode'] = 'libArdListDateByChannel'
		elif (mode == 'libArdListChannelLivestreams') and (channel[1] & (live_byclient + live_byard)):
			d['mode'] = 'libArdListLivestreamsByChannel'
		else:
			d['mode'] = None
		if d['mode']:
			d['_name'] = channel[0]
			d['_type'] = 'dir'
			d['channel'] = str(i)
			l.append(d)
	return l

def libArdListShowsByChannel():
	params = libMediathek.get_params()
	return libMediathek.populateDirAZ('libArdListChannelShowVideos', [], params['channel'])

def libArdListDateByChannel():
	params = libMediathek.get_params()
	return libMediathek.populateDirDate('libArdListChannelDateVideos', params['channel'])

def libArdListLivestreamsByChannel():
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	# Livestreams sind nicht sinnvoll vorsortiert
	libMediathek.sortAZ()
	return libArdJsonParserNeu.parseLivestreams(channel[2], 'ard' if (channel[1] & live_byard) else channel[3])

def libArdListChannelShowVideos():
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	letter = params['name'].upper()
	if letter == '#':
		letter = '09'
	return libArdJsonParserNeu.parseAZ(channel[3], letter)

def libArdListChannelDateVideos():
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	partnerKey = channel[2]
	# "Alle Sender nach Datum" ist nicht sinnvoll vorsortiert
	if partnerKey is None:
		libMediathek.sortAZ()
	return libArdJsonParserNeu.parseDate(partnerKey, channel[3], params['yyyymmdd'])

def libArdListSearch():
	search_string = libMediathek.getSearchString(do_quote=False)
	if search_string:
		return libArdJsonParserNeu.parseSearchHtml('http://www.ardmediathek.de/ard/search/'+search_string)
	else:
		return None

def libArdListShow():
	params = libMediathek.get_params()
	return libArdJsonParserNeu.parseShow(params['documentId'])

def libArdPlay():
	params = libMediathek.get_params()
	result = libArdJsonParserNeu.getVideoUrl(params['documentId'])
	result = libMediathek.getMetadata(result)
	return result

def libArdPlayHtml():
	params = libMediathek.get_params()
	result = libArdJsonParserNeu.getVideoUrlHtml(params['url'])
	result = libMediathek.getMetadata(result)
	return result

ondemand =      (1<<0)
bydate =        (1<<1)
live_byclient = (1<<2)
live_byard =    (1<<3)

channels = (
#	(name,            flags,                              partnerKey,     clientKey)
	('Alle Sender',   ondemand + bydate + live_byard,     None,           'ard'),
	('Das Erste',     ondemand + bydate + live_byclient,  'das_erste',    'daserste'),
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
	('ARD-alpha',     ondemand + bydate + live_byard,     'ard-alpha',    'ardalpha'),
	('Phoenix',       ondemand + bydate + live_byard,     'phoenix',      'phoenix'),
	('Tagesschau24',  ondemand + bydate + live_byclient,  'tagesschau24', 'tagesschau24'),
	('3sat',          live_byard,                         '3sat',         None),
	('Arte',          live_byard,                         'arte',         None),
	('KiKA',          live_byard,                         'KiKa',         None),
	('Deutsche Welle',live_byard,                         'dw',           None),
)

modesNeu = {
	'libArdListMainNeu':              libArdListMainNeu,
	'libArdListChannelShows':         libArdListChannels,
	'libArdListChannelDates':         libArdListChannels,
	'libArdListChannelLivestreams':   libArdListChannels,
	'libArdListShowsByChannel':       libArdListShowsByChannel,
	'libArdListDateByChannel':        libArdListDateByChannel,
	'libArdListLivestreamsByChannel': libArdListLivestreamsByChannel,
	'libArdListChannelShowVideos':    libArdListChannelShowVideos,
	'libArdListChannelDateVideos':    libArdListChannelDateVideos,
	'libArdListSearch':               libArdListSearch,
	'libArdListShow':                 libArdListShow,
	'libArdPlay':                     libArdPlay,
	'libArdPlayHtml':                 libArdPlayHtml,
}
