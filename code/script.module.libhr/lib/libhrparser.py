# -*- coding: utf-8 -*-
import sys
import json
import re
import bs4 as bs
import libmediathek3 as libMediathek
from libhr import base

if sys.version_info[0] < 3: # for Python 2
	from urllib2 import HTTPError
else: # for Python 3
	from urllib.error import HTTPError

def getDate(url):
	response = libMediathek.getUrl(url)
	section = re.compile('<section class="c-teaserGroup -s100">(.+?)</section>', re.DOTALL).findall(response)[0]
	articles = re.compile('<article.+?>(.+?)</article>', re.DOTALL).findall(section)
	l = []
	for article in articles:
		#TODO: date
		d = {}
		d['url'] = re.compile('<a href="(.+?)"', re.DOTALL).findall(article)[0]
		d['name'] = re.compile('<span class="c-teaser__headline text__headline">(.+?)</span>', re.DOTALL).findall(article)[0].strip()
		d['thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(article)[0]
		d['_type'] = 'video'
		d['mode'] = 'libHrPlay'
		l.append(d)
	return l

def getEpisodes(showid, showname = None):
	if showname and sys.version_info[0] < 3: # for Python 2
		showname = showname.decode('utf-8')
	l = []
	try:
		response = 	libMediathek.getUrl(
			showid if showid.startswith('https://')
			else base + '/sendungen-a-z/'+showid+'.html'
		)
		soup = bs.BeautifulSoup(response, 'html.parser')
		articles = soup.findAll('article')
		for article in articles:
			json_div = article.find(
				lambda tag:
					tag.name == 'div'
					and hasattr(tag,'attrs')
					and isinstance(tag.attrs.get('class'), list)
					and len(tag.attrs.get('class')) > 0
					and tag.attrs.get('class')[0] == 'js-loadScript'
					and tag.attrs.get('data-hr-mediaplayer-loader')
			)
			if json_div:
				d = {}
				j = json.loads (json_div.attrs.get('data-hr-mediaplayer-loader'))
				if 'adaptiveStreamingUrl' in j:
					d['url'] = j['adaptiveStreamingUrl']
				elif 'streamUrl' in j:
					d['url'] = j['streamUrl']
				else:
					continue
				d['name'] = (
					showname + ' vom ' + j['mediaMetadata']['agf']['airdate'] if showname
					else j['mediaMetadata']['agf']['title']
				)
				teaser = article.find('span', {'class': 'c-teaser__underline'})
				if teaser:
					d['plot'] = teaser.text.strip()
				d['thumb'] = j['previewImageUrl']['s']
				d['_type'] = 'video'
				d['mode'] = 'libHrPlay'
				l.append(d)
	except HTTPError as ex:
		if ex.code != 404:
			raise
	return l

def getVideo(url):
	d = {}
	d['media'] = []
	d['media'].append({'url': url, 'type': 'video', 'stream': 'mp4' if url.endswith('.mp4') else 'HLS'})
	return d