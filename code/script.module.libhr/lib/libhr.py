# -*- coding: utf-8 -*-
import sys
import urllib
import libhrparser as libHrParser
import libmediathek3 as libMediathek
import libhrshows

translation = libMediathek.getTranslation

ardhack = True


def libHrListMain():
	l = []
	l.append({'_name':translation(31032), 'mode':'libHrListShows','_type':'dir'})
	# l.append({'_name':translation(31033), 'mode':'libHrListDate','_type':'dir'})
	return l
	
def libHrListDate():
	l = [
		{'_name':translation(31014), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/montag-video-100.html'},
		{'_name':translation(31015), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/dienstag-video-100.html'},
		{'_name':translation(31016), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/mittwoch-video-100.html'},
		{'_name':translation(31017), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/donnerstag-video-100.html'},
		{'_name':translation(31018), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/freitag-video-100.html'},
		{'_name':translation(31019), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/samstag-video-100.html'},
		{'_name':translation(31013), 'mode':'libHrListDateVideos','_type':'dir', 'url':'http://www.hr-fernsehen.de/sonntag-video-100.html'},
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
	return libhrshows.shows
	
def libHrListEpisodes():
	return libHrParser.getEpisodes(params['showid'])
	
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
	mode = params.get('mode','libHrListMain')
	if mode == 'libHrPlay':
		libMediathek.play(libHrPlay())
	else:
		l = modes.get(mode)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()	
