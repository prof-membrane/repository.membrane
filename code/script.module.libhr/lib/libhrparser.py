# -*- coding: utf-8 -*-
import xbmc
import json
import re
from urllib2 import HTTPError
import bs4 as bs
import libmediathek3 as libMediathek
from libhr import base


def getDate(url):
	response = libMediathek.getUrl(url)
	section = re.compile('<section class="c-teaserGroup -s100">(.+?)</section>', re.DOTALL).findall(response)[0]
	articles = re.compile('<article.+?>(.+?)</article>', re.DOTALL).findall(section)
	l = []
	for article in articles:
		#TODO: date
		d = {}
		d['url'] = re.compile('<a href="(.+?)"', re.DOTALL).findall(article)[0]
		d['_name'] = re.compile('<span class="c-teaser__headline text__headline">(.+?)</span>', re.DOTALL).findall(article)[0].strip()
		d['_thumb'] = re.compile('<img.+?src="(.+?)"', re.DOTALL).findall(article)[0]
		d['_type'] = 'video'
		d['mode'] = 'libHrPlay'
		l.append(d)
	return l

def getEpisodes(showid, showname = None):
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
				lambda(tag):
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
				d['_name'] = (
					showname.decode('utf-8') + ' vom ' + j['mediaMetadata']['agf']['airdate'] if showname
					else j['mediaMetadata']['agf']['title']
				)
				teaser = article.find('span', {'class': 'c-teaser__underline'})
				if teaser:
					d['_plot'] = teaser.text.strip() 
				d['_thumb'] = j['previewImageUrl']['s']
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