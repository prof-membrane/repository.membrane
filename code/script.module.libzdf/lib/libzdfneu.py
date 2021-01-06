#!/usr/bin/python
# -*- coding: utf-8 -*-
import libzdfjsonparserneu as libZdfJsonParserNeu
import libmediathek3 as libMediathek

params = libMediathek.get_params()

def list():
	return libMediathek.list(modesNeu, 'libZdfListMainNeu', 'libZdfPlayNeu', 'libZdfPlayLivestream')

def libZdfListMainNeu():
	l = []
	translation = libMediathek.getTranslation
	l.append({'name':translation(31033), 'mode':'libZdfListChannelDates', '_type':'dir'})
	l.append({'name':translation(31036), 'mode':'libZdfListLivestreams', '_type':'dir'})
	l.append({'name':translation(31034), 'mode':'libZdfListRubrics', '_type':'dir'})
	l.append({'name':translation(31039), 'mode':'libZdfListSearch', '_type':'dir'})
	return l

def libZdfListChannelDates():
	l = []
	for i, channel in enumerate(channels):
		if channel[1] & bydate:
			l.append (dict (mode = 'libZdfListDateByChannel', _name = channel[0], _type = 'dir', channel = str(i)))
	return l

def libZdfListDateByChannel():
	return libMediathek.populateDirDate('libZdfListChannelDateVideos', params['channel'])

def libZdfListChannelDateVideos():
	channelIndex = int(params['channel'])
	channel = channels[channelIndex]
	return libZdfJsonParserNeu.parseDate(None if channelIndex == 0 else channel[0], params['yyyymmdd'])

def libZdfListLivestreams():
	return libZdfJsonParserNeu.parseLivestreams()

def libZdfListRubrics():
	return libZdfJsonParserNeu.parseRubrics()

def libZdfListCategory():
	params = libMediathek.get_params()
	return libZdfJsonParserNeu.parseCategory(params['url'])

def libZdfListSearch():
	search_string = libMediathek.getSearchString()
	if search_string:
		return libZdfJsonParserNeu.parseSearch(search_string)
	else:
		return None

def libZdfPlayLivestream():
	return dict (media = [{'url':params['url'], 'type':'video', 'stream':params['stream']}])

def libZdfPlayNeu():
	result = libZdfJsonParserNeu.parseVideo(params['url'])
	result = libMediathek.getMetadata(result)
	return result


bydate =        (1<<0)
live =          (1<<1)

channels = (
#	(name,            flags)
	('Alle Sender',   bydate),
	('ZDF',           bydate + live),
	('ZDFinfo',       bydate + live),
	('ZDFneo',        bydate + live),
	('3sat',          live),
	('KI.KA',         live),
	('PHOENIX',       live),
	('arte',          live),
)

modesNeu = {
	'libZdfListMainNeu':              libZdfListMainNeu,
	'libZdfListChannelDates':         libZdfListChannelDates,
	'libZdfListDateByChannel':        libZdfListDateByChannel,
	'libZdfListChannelDateVideos':    libZdfListChannelDateVideos,
	'libZdfListLivestreams':          libZdfListLivestreams,
	'libZdfListRubrics':              libZdfListRubrics,
	'libZdfListCategory':             libZdfListCategory,
	'libZdfListSearch':               libZdfListSearch,
	'libZdfPlayLivestream':           libZdfPlayLivestream,
	'libZdfPlayNeu':                  libZdfPlayNeu,
}

