# -*- coding: utf-8 -*-
import libmediathek3 as libMediathek
import libzdf

def main():
	# libzdf.params = {}
	# libzdf.params['url'] = 'https://api.zdf.de/content/documents/kindersendungen-a-z-100.json?profile=default'
	# libzdf.params['mode'] = 'libZdfListShows'
	# return libzdf.libZdfListShows()
	l = []
	translation = libMediathek.getTranslation
	l.append({'_name':translation(31032), '_type':'dir', 'mode':'libZdfListShows', 'url':'https://api.zdf.de/content/documents/kindersendungen-a-z-100.json?profile=default'})
	l.append({'_name':translation(31033), '_type':'dir', 'mode':'libZdfListChannelDate', 'channel':'KI.KA'})
	# l.append({'_name':'unknown_1', 'mode':'libZdfListPage', 'url':'https://api.zdf.de/content/documents/zdftivi-fuer-kinder-100.json?profile=default', '_type':'dir'})#Live
	# l.append({'_name':'unknown_2', 'mode':'libZdfListPage', 'url':'https://api.zdf.de/content/documents/zdftivi-sendung-verpasst-100.json?profile=default&airtimeBegin=2018-02-20T05%3A30%3A00%2B02%3A00&airtimeEnd=2018-02-24T05%3A29%3A00%2B02%3A00', '_type':'dir'})#Live
	return l

modes = dict (main = main, **libzdf.modes)

def list():
	return libMediathek.list(modes, 'main', 'libZdfPlay', 'libZdfPlayById')

list()
