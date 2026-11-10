#!/usr/bin/python
# -*- coding: utf-8 -*-
import libzdfjsonparserneu as libZdfJsonParserNeu
import libmediathek3 as libMediathek

params = libMediathek.get_params()

def list():
	return libMediathek.list(modes, 'libZdfListMainMobile', *playModes)

def libZdfListMainMobile():
	l = []
	flavour = ' / Mobile'
	translation = libMediathek.getTranslation
	l.append({'sort':'31033'+flavour, 'name':translation(31033)+flavour, 'mode':'libZdfListChannelDates', '_type':'dir'})
	l.append({'sort':'31034', 'name':translation(31034), 'mode':'libZdfListRubrics', '_type':'dir'})
	l.append({'sort':'31036', 'name':translation(31036), 'mode':'libZdfListLivestreams', '_type':'dir'})
	l.append({'sort':'31039'+flavour, 'name':translation(31039)+flavour, 'mode':'libZdfListSearch', '_type':'dir'})
	return l

def libZdfListChannelDates():
	l = []
	for i, channel in enumerate(channels):
		if channel[1] & bydate:
			l.append (dict (mode = 'libZdfListDateByChannel', _name = channel[0], _type = 'dir', channel = str(i)))
	return l

def libZdfListDateByChannel():
	return libMediathek.populateDirDate('libZdfListDateVideosOfChannel', params['channel'])

def libZdfListDateVideosOfChannel():
	channelIndex = int(params['channel'])
	channel = channels[channelIndex]
	# return libZdfJsonParserNeu.parseDate(channel[2], params['yyyymmdd'])
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
	result = dict (media = [{'url':params['url'], 'type':'video', 'stream':params['stream']}])
	result = libMediathek.getMetadata(result)
	return result

def libZdfPlayNeu():
	result = libZdfJsonParserNeu.parseVideo(params['url'])
	result = libMediathek.getMetadata(result)
	return result


bydate =        (1<<0)
live =          (1<<1)

channels = (
#	(name             flags           channel )
	('Alle Sender',   bydate,         None    ),
	('ZDF',           bydate + live,  '1'     ),
	('ZDFinfo',       bydate + live,  '3'     ),
	('ZDFneo',        bydate + live,  '2'     ),
	('3sat',          bydate + live,  '8'     ),
	('KI.KA',         bydate + live,  '5'     ),
	('PHOENIX',       live,           None    ),
	('arte',          live,           None    ),
)

modes = {
	'libZdfListMainMobile':         ( libZdfListMainMobile, 'videos' ),
	'libZdfListChannelDates':       ( libZdfListChannelDates, 'videos' ),
	'libZdfListDateByChannel':      ( libZdfListDateByChannel, 'videos' ),
	'libZdfListDateVideosOfChannel':( libZdfListDateVideosOfChannel, 'movies' ),
	'libZdfListLivestreams':        ( libZdfListLivestreams, 'videos' ),
	'libZdfListRubrics':            ( libZdfListRubrics, 'videos' ),
	'libZdfListCategory':           ( libZdfListCategory, 'movies' ),
	'libZdfListSearch':             ( libZdfListSearch, 'movies' ),
	'libZdfPlayLivestream':         ( libZdfPlayLivestream, None ),
	'libZdfPlayNeu':                ( libZdfPlayNeu, None ),
}

playModes = ('libZdfPlayNeu', 'libZdfPlayLivestream')