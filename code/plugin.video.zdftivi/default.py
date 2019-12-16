# -*- coding: utf-8 -*-
import libmediathek3 as libMediathek
import libzdf

translation = libMediathek.translation

def main():
	libzdf.params = {}
	libzdf.params['url'] = 'https://api.zdf.de/content/documents/kindersendungen-a-z-100.json?profile=default'
	#libzdf.params['mode'] = 'libZdfListShows'
	return libzdf.libZdfListShows()
	l = []
	l.append({'_name':'az', 'mode':'libZdfListShows', 'url':'https://api.zdf.de/content/documents/kindersendungen-a-z-100.json?profile=default', '_type':'dir'})#Live
	l.append({'_name':'date', 'mode':'libZdfListChannelDate', 'channel':'KI.KA', '_type':'dir'})
	l.append({'_name':'date2', 'mode':'libZdfListPage', 'url':'https://api.zdf.de/content/documents/zdftivi-fuer-kinder-100.json?profile=default', '_type':'dir'})#Live
	#l.append({'_name':'date', 'mode':'libZdfListPage', 'url':'https://api.zdf.de/content/documents/zdftivi-sendung-verpasst-100.json?profile=default&airtimeBegin=2018-02-20T05%3A30%3A00%2B02%3A00&airtimeEnd=2018-02-24T05%3A29%3A00%2B02%3A00', '_type':'dir'})#Live
	return l

modes = {
'main': main,
}
	
def list():	
	global params
	params = libMediathek.get_params()
	mode = params.get('mode','main')
	if mode.startswith('libZdf'):
		libzdf.list()
	else:
		l = modes.get(mode)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()	
list()