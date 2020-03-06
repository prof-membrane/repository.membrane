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
		elif (mode == 'libArdListChannelLivestreams') and (channel[1] & livestream):
			d['mode'] = 'libArdPlayLivestreamByChannel'
		else:
			d['mode'] = None
		if d['mode']:
			d['_name'] = channel[0]
			d['_type'] = 'dir'
			d['channel'] = str(i)
			l.append(d)
	return l

def libArdListShowsByChannel():
	libMediathek.sortAZ()
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	return libArdJsonParserNeu.parseAZ(channel[2], channel[3])

def libArdListDateByChannel():
	params = libMediathek.get_params()
	return libMediathek.populateDirDate('libArdListChannelDateVideos', params['channel'])

def libArdPlayLivestreamByChannel():
	libMediathek.sortAZ()
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	return libArdJsonParserNeu.parseAZ(channel[2], channel[3], getLivestream=True)

def libArdListChannelDateVideos():
	libMediathek.sortAZ()
	params = libMediathek.get_params()
	channel = channels[int(params['channel'])]
	return libArdJsonParserNeu.parseDate(channel[2], channel[3], params['yyyymmdd'])

def libArdListSearch():
	search_string = libMediathek.getSearchString(do_quote=False)
	if search_string:
		return libArdJsonParserNeu.parseSearchHtml('http://www.ardmediathek.de/ard/search/'+search_string)
	else:
		return None

def libArdListShow():
	libMediathek.sortAZ()
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

ondemand =   (1<<0)
bydate =     (1<<1)
livestream = (1<<2)

channels = (
#	(name,            flags,                          channelKey,     clientKey)
	('Alle Sender',   ondemand + bydate,              None,           'ard'),
	('Das Erste',     ondemand + bydate + livestream, 'das_erste',    'ard'),
	('BR',            ondemand + bydate + livestream, 'br',           'br'),
	('HR',            ondemand + bydate + livestream, 'hr',           'hr'),
	('MDR',           ondemand + bydate + livestream, 'mdr',          'mdr'),
	('NDR',           ondemand + bydate + livestream, 'ndr',          'ndr'),
	('Radio Bremen',  bydate + livestream,            'radio_bremen', 'ard'),
	('RBB',           ondemand + bydate + livestream, 'rbb',          'rbb'),
	('SR',            ondemand + bydate + livestream, 'sr',           'sr'),
	('SWR',           ondemand + bydate + livestream, 'swr',          'swr'),
	('WDR',           ondemand + bydate + livestream, 'wdr',          'wdr'),
	('One',           ondemand + bydate + livestream, 'one',          'one'),
	('ARD-alpha',     bydate + livestream,            'ard-alpha',    'ard'),
	('Phoenix',       bydate + livestream,            'phoenix',      'ard'),
	('Tagesschau24',  ondemand + bydate + livestream, 'tagesschau24', 'tagesschau24'),
	('3sat',          livestream,                     '3sat',         'ard'),
	('Arte',          livestream,                     'arte',         'ard'),
	('KiKA',          livestream,                     'KiKa',         'ard'),
	('Deutsche Welle',livestream,                     'dw',           'ard'),
)

modesNeu = {
	'libArdListMainNeu':            libArdListMainNeu,
	'libArdListChannelShows':       libArdListChannels,
	'libArdListChannelDates':       libArdListChannels,
	'libArdListChannelLivestreams': libArdListChannels,
	'libArdListShowsByChannel':     libArdListShowsByChannel,
	'libArdListDateByChannel':      libArdListDateByChannel,
	'libArdPlayLivestreamByChannel':libArdPlayLivestreamByChannel,
	'libArdListChannelDateVideos':  libArdListChannelDateVideos,
	'libArdListSearch':             libArdListSearch,
	'libArdListShow':               libArdListShow,
	'libArdPlay':                   libArdPlay,
	'libArdPlayHtml':               libArdPlayHtml,
}
