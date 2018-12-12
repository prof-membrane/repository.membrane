# -*- coding: utf-8 -*-	
import libmdrmetaparser as libMdrMetaParser
import libmdrhtmlparser as libMdrHtmlParser
import libmediathek3 as libMediathek

translation = libMediathek.getTranslation
id = 'script.module.libmdr'

def libMdrListMain():
	l = []
	l.append({'_name':translation(31030), 'mode':'libMdrListPlus', 'url':'http://www.mdr.de/mediathek/mediathek-neu-100-meta.xml', '_type':'dir'})
	l.append({'_name':translation(31031), 'mode':'libMdrListPlus', 'url':'http://www.mdr.de/mediathek/mediathek-meistgeklickt-100-meta.xml', '_type':'dir'})
	l.append({'_name':translation(31032), 'mode':'libMdrListShows', '_type':'dir'})
	l.append({'_name':translation(31033), 'mode':'libMdrListDate', '_type':'dir'})
	l.append({'_name':translation(31034), 'mode':'libMdrListRubrics', '_type':'dir'})
	l.append({'_name':translation(31039), 'mode':'libMdrListSearch', '_type':'dir'})
	return l

def libMdrListRubrics():
	"""
	{'_name':translation(32000, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/reportage/mediathek-reportagen-dokumentationen-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32001, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/sport/mediathek-sport-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32002, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/sachsen/mediathek-sachsen-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32003, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/sachsen-anhalt/mediathek-sachsen-anhalt-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32004, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/thueringen/mediathek-thueringen-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32005, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/kinder/mediathek-kinder-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32006, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/film-serie/mediathek-film-serien-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32007, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/magazine/mediathek-magazine-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	{'_name':translation(32008, id),'mode':'libMdrListHtml','url':'http://www.mdr.de/mediathek/themen/nachrichten/mediathek-nachrichten-100_box--5390492834412829556_zc-4e12cc21.html', '_type':'dir'},
	"""
	l = [
	{'_name':translation(32000, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/reportage/mediathek-reportagen-dokumentationen-100-meta.xml', '_type':'dir'},
	{'_name':translation(32001, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/sport/mediathek-sport-100-meta.xml', '_type':'dir'},
	{'_name':translation(32002, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/sachsen/mediathek-sachsen-100-meta.xml', '_type':'dir'},
	{'_name':translation(32003, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/sachsen-anhalt/mediathek-sachsen-anhalt-100-meta.xml', '_type':'dir'},
	{'_name':translation(32004, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/thueringen/mediathek-thueringen-100-meta.xml', '_type':'dir'},
	{'_name':translation(32005, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/kinder/mediathek-kinder-100-meta.xml', '_type':'dir'},
	{'_name':translation(32006, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/film-serie/mediathek-film-serien-100-meta.xml', '_type':'dir'},
	{'_name':translation(32007, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/magazine/mediathek-magazine-100-meta.xml', '_type':'dir'},
	{'_name':translation(32008, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/themen/nachrichten/mediathek-nachrichten-100-meta.xml', '_type':'dir'},
	{'_name':translation(32009, id),'mode':'libMdrListPlus','url':'http://www.mdr.de/mediathek/livestreams/mdr-plus/mediathek-mdrplus-100-meta.xml', '_type':'dir'},
	]
	return l

def libMdrBroadcast():
	return libMdrMetaParser.parseBroadcast(params['url'])
			
def libMdrListShows():#
	libMediathek.sortAZ()
	return libMdrMetaParser.parseShows()

def libMdrListPlus():#
	return libMdrMetaParser.parseMdrPlus(params['url'])
	
def libMdrListVideos():#
	return libMdrMetaParser.parseVideos(params['url'])
	
def libMdrListDate():
	return libMediathek.populateDirDate('libMdrListDateVideos')
	
def libMdrListDateVideos():
	return libMdrHtmlParser.parseDate(params['datum'])
	
def libMdrListSearch():
	search_string = libMediathek.getSearchString()
	return libMdrHtmlParser.getSearch(search_string)
	
def libMdrPlay():
	return libMdrMetaParser.parseVideo(params['url'])
	
	
def list():	
	modes = {
	'libMdrListMain': libMdrListMain,
	'libMdrBroadcast': libMdrBroadcast,
	'libMdrListRubrics': libMdrListRubrics,
	
	
	'libMdrListShows': libMdrListShows,
	'libMdrListPlus': libMdrListPlus,
	'libMdrListVideos': libMdrListVideos,
	'libMdrListDate': libMdrListDate,
	'libMdrListDateVideos': libMdrListDateVideos,
	#'libMdrListDateChannels': libMdrListDateChannels,
	'libMdrListSearch': libMdrListSearch,
	'libMdrPlay': libMdrPlay
	}
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','libMdrListMain')
	if mode == 'libMdrPlay':
		libMediathek.play(libMdrPlay())
	else:
		l = modes.get(mode)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()
