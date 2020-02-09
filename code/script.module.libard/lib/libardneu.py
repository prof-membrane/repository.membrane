#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from datetime import date, timedelta

import libardjsonparser as libArdJsonParser
import libardjsonparserneu as libArdJsonParserNeu
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
params = libMediathek.get_params()

def list():
	return libMediathek.list(modesNeu, 'libArdListMainNeu', 'libArdPlayNeu')

def libArdListMainNeu():
	l = []
	l.append({'name':translation(31032), 'mode':'libArdListChannelLetters', '_type':'dir'})
	l.append({'name':translation(31033), 'mode':'libArdListChannelDate', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libArdListSearch', '_type':'dir'})
	return l

def libArdListSearch():
	search_string = libMediathek.getSearchString(do_quote=False)
	if search_string:
		return libArdJsonParser.parseSearch('http://www.ardmediathek.de/ard/search/'+search_string)
	else:
		return None

def libArdPlayNeu():
	result = libArdJsonParser.getVideoUrlNeu(params['url'])
	result = libMediathek.getMetadata(result)
	return result

def libArdListChannels():
	l = []
	mode = params['mode']
	for i, channel in enumerate(channelsNeu):
		d = {}
		d['_name'] = channel[0]
		d['_type'] = 'dir'
		d['channel'] = str(i)
		if mode == 'libArdListChannelLetters':
			d['mode'] = 'libArdListLettersByChannel'
		elif mode == 'libArdListChannelDate':
			d['mode'] = 'libArdListDateByChannel'
		else:
			d['mode'] = None
		l.append(d)
	return l

def libArdListLettersByChannel():
	return libMediathek.populateDirAZ('libArdListChannelShows',[],params['channel'])

def libArdListDateByChannel():
	return libMediathek.populateDirDate('libArdListChannelDateVideos',params['channel'])

def libArdListChannelShows():
	return libArdJsonParserNeu.parseAZ(params['channel'],params['name'])

def libArdListChannelDateVideos():
	return libArdJsonParserNeu.parseDate(params['channel'],params['yyyymmdd'])

def libArdPlay():
	result = libArdJsonParserNeu.getVideoUrl(params['url'])
	result = libMediathek.getMetadata(result)
	return result

channelsNeu = [
	('Alle Sender',None),
	('Das Erste',None),
	('BR',None),
	('HR',None),
	('MDR',None),
	('NDR',None),
	('Radio Bremen',None),
	('RBB',None),
	('SR',None),
	('SWR',None),
	('WDR',None),
	('One',None),
	('ARD-alpha',None),
	('Phoenix',None),
	('Tagesschau24',None),
]

modesNeu = {
	'libArdListMainNeu':          libArdListMainNeu,
	'libArdListSearch':           libArdListSearch,
	'libArdPlayNeu':              libArdPlayNeu,
	'libArdListChannelLetters':   libArdListChannels,
	'libArdListChannelDate':      libArdListChannels,
	'libArdListLettersByChannel': libArdListLettersByChannel,
	'libArdListDateByChannel':    libArdListDateByChannel,
	'libArdListChannelShows':     libArdListChannelShows,
	'libArdListChannelDateVideos':libArdListChannelDateVideos,
	'libArdPlay':                 libArdPlay,
}
