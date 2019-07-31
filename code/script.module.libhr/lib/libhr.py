# -*- coding: utf-8 -*-
import sys
import urllib
import xbmc
import bs4 as bs
import libmediathek3 as libMediathek
import libhrshows

base = 'https://www.hr-fernsehen.de'
import libhrparser as libHrParser


translation = libMediathek.getTranslation

ardhack = True


def isHessenschau(url):
	return url.startswith('https://www.hessenschau.de')

def libHrListMain():
	l = []
	l.append({'_name':translation(31032), 'mode':'libHrListShows','_type':'dir'})
	# l.append({'_name':translation(31033), 'mode':'libHrListDate','_type':'dir'})
	return l

def libHrListDate():
	l = [
		{'_name':xbmc.getLocalizedString(11), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/montag-video-100.html'},
		{'_name':xbmc.getLocalizedString(12), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/dienstag-video-100.html'},
		{'_name':xbmc.getLocalizedString(13), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/mittwoch-video-100.html'},
		{'_name':xbmc.getLocalizedString(14), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/donnerstag-video-100.html'},
		{'_name':xbmc.getLocalizedString(15), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/freitag-video-100.html'},
		{'_name':xbmc.getLocalizedString(16), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/samstag-video-100.html'},
		{'_name':xbmc.getLocalizedString(17), 'mode':'libHrListDateVideos','_type':'dir', 'url': base + '/sonntag-video-100.html'},
	]
	return l

def libHrListDateVideos():
	return libHrParser.getDate(params['url'])

"""
def libHrListDate():
	return libMediathek.populateDirDate('libHrListDateVideos')

def libHrListDateVideos():
	return libHrParser.getDate(params['yyyymmdd'])
"""

def libHrListShows():
	# return libhrshows.shows
	l = []
	response = libMediathek.getUrl(base + '/sendungen-a-z/index.html')
	soup = bs.BeautifulSoup(response, 'html.parser')
	articles = soup.findAll('div', {'class': 'c-teaser__content'})
	for article in articles:
		name = article.find('span', {'class': 'c-teaser__headline'})
		href = article.find('a', {'class': 'c-teaser__headlineLink'})
		if name and href:
			d = {}
			href_str = href.attrs['href']
			if href_str.startswith(base):
				d['showid'] = href_str.replace('/index.html','/sendungen/index.html')
			elif isHessenschau(href_str):
				d['showid'] = href_str
			else:
				continue
			d['name'] = name.text.strip()
			d['mode'] = 'libHrListEpisodes'
			d['_type'] = 'dir'
			thumb = article.find('img', {'class': 'image ar__content'})
			if thumb:
				d['_thumb'] = thumb.attrs['src']
			l.append(d)
	return l

def libHrListEpisodes():
	return libHrParser.getEpisodes(params['showid'], None if isHessenschau(params['showid']) else params['name'])

def libHrPlay():
	return libHrParser.getVideo(params['url'])
	url = params['url']
	if ardhack:#ugly hack to get better quality videos
		s = params['url'].split('/')
		testurl = 'http://www.hr.gl-systemhaus.de/mp4/ARDmediathek/' + s[-2] + '/' + s[-1]
		id = int(testurl[-10:-4]) + 1
		testurl = testurl[:-10] + str(id) + '_webl_ard.mp4'
		try:
			headUrl(testurl)
			url = testurl
		except: pass
	d = {}
	d['media'] = []
	d['media'].append({'url':url, 'type': 'video', 'stream':'HLS'})

	#the libmediathek3 ttml parser can't handle this file now :(
	if 'subUrl' in params:
		d['subtitle'] = [{'url':params['subUrl'], 'type': 'ttml', 'lang':'de'}]
	return d

def headUrl(url):#TODO: move to libmediathek3
	libMediathek.log(url)
	import urllib2
	req = urllib2.Request(url)
	req.get_method = lambda : 'HEAD'
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0')

	response = urllib2.urlopen(req)
	info = response.info()
	response.close()
	return info

def list():
	modes = {
		'libHrListMain': libHrListMain,
		'libHrListDate': libHrListDate,
		'libHrListDateVideos': libHrListDateVideos,
		'libHrListShows': libHrListShows,
		'libHrListEpisodes': libHrListEpisodes,
		'libHrPlay': libHrPlay,
	}

	global params
	params = libMediathek.get_params()
	global pluginhandle
	pluginhandle = int(sys.argv[1])
	# mode = params.get('mode','libHrListMain')
	mode = params.get('mode','libHrListShows')
	if mode == 'libHrPlay':
		libMediathek.play(libHrPlay())
	else:
		l = modes.get(mode)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()
