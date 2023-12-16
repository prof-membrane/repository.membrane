# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek
import re
#import dateutil.parser

base = 'http://www1.wdr.de'


def parseShows(letter):
	l = []
	if (letter in ('a','x','q')):
		pass
	else:
		response = libMediathek.getUrl(base+'/sendungen-'+letter+'-102~_variant-android.mobile')
		items = re.compile('<mp:additionallink>(.+?)</mp:additionallink>', re.DOTALL).findall(response)
		l = []
		if len(items) > 0:
			creator = re.compile('<dc:creator>(.+?)</dc:creator>', re.DOTALL).findall(response)[0]
			for item in items:
				d = {}
				d['name'] = re.compile('<mp:label>(.+?)</mp:label>', re.DOTALL).findall(item)[0]
				if len(l) != 0 and d['name'] == l[-1]['name']: continue
				tmpstr = re.compile('<mp:link>(.+?)</mp:link>', re.DOTALL).findall(item)[0].split('/')[-1]
				if '~' not in tmpstr: continue
				d['id'],extension = tmpstr.split('~')
				#libMediathek.log(d['id'])
				#libMediathek.log(re.compile('<mp:link>(.+?)</mp:link>', re.DOTALL).findall(item)[0])
				d['_channel'] = creator
				d['thumb'] = _chooseThumb(re.compile('<mp:image>(.+?)</mp:image>', re.DOTALL).findall(item))
				d['_type'] = 'dir'
				if extension.endswith('rss'):
					d['grepShowFromVideo'] = 'True'
				d['mode'] = 'libWdrListVideos'
				l.append(d)
	return l

def parseVideos(id,type=None,grepShowFromVideo=False):
	if grepShowFromVideo:
		url = 'http://www1.wdr.de/Medien/mediathek/video/sendungen-a-z/'+id+'~_variant-android.rss'
		response = libMediathek.getUrl(url)
		url = re.compile('<link>(.+?)</link>').findall(response)[0]
	else:
		url = 'http://www1.wdr.de/'+id+'~_variant-android.mobile'
	response = libMediathek.getUrl(url)
	items = re.compile('<item>(.+?)</item>', re.DOTALL).findall(response)
	l = []
	for item in items:

		d = {}
		dctype = re.compile('<dc:type>(.+?)</dc:type>', re.DOTALL).findall(item)[0]
		if 'Video' in dctype:# or (dctype == 'Sportnachricht - sportschau.de' and '<title>' in item):
			d['name'] = re.compile('<title>(.+?)</title>', re.DOTALL).findall(item)[0]
			d['url'] = re.compile('<link>(.+?)</link>', re.DOTALL).findall(item)[0]
			mediagroup = re.compile('<media:group>(.+?)</media:group>', re.DOTALL).findall(item)[0]
			try:
				d['_duration'],d['m3u8'] = re.compile('<media:content duration="(.+?)".+?url="(.+?)"', re.DOTALL).findall(mediagroup)[0]
			except:
				libMediathek.log(item)
				# war: d['name'] = '##################'+ re.compile('<title>(.+?)</title>', re.DOTALL).findall(item)[0]
				continue
			if '<content:encoded>' in item:
				d['plot'] = re.compile('<content:encoded>(.+?)</content:encoded>', re.DOTALL).findall(item)[0].replace('\n ','\n')
			d['_channel'] = re.compile('<dc:creator>(.+?)</dc:creator>', re.DOTALL).findall(item)[0]
			d['_tvshowtitle'] = re.compile('<mp:topline>(.+?)</mp:topline>', re.DOTALL).findall(item)[0]
			if '<mp:expires>' in item:
				d['_ttl'] = re.compile('<mp:expires>(.+?)</mp:expires>', re.DOTALL).findall(item)[0]
			d['thumb'] = _chooseThumb(re.compile('<mp:image>(.+?)</mp:image>', re.DOTALL).findall(item))

			dcdate = re.compile('<dc:date>(.+?)</dc:date>', re.DOTALL).findall(item)[0]#TODO
			d['_airedISO8601'] = dcdate
			if type:
				d['_type'] = type
			else:
				d['_type'] = 'date'
			d['mode'] = 'libWdrPlay'
			l.append(d)
	l.sort(key = lambda x: x.get('_airedISO8601',None), reverse = (type != 'date'))
	return l

def _chooseThumb(thumbs):
	for thumb in thumbs:
		w = re.compile('<mp:width>(.+?)</mp:width>', re.DOTALL).findall(thumb)[0]
		h = re.compile('<mp:height>(.+?)</mp:height>', re.DOTALL).findall(thumb)[0]
		if w == '310' and h == '174':
			return re.compile('<mp:data>(.+?)</mp:data>', re.DOTALL).findall(thumb)[0]
