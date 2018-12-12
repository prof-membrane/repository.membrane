# -*- coding: utf-8 -*-
import libmediathek3 as libMediathek
import json

baseUrl = 'http://swrmediathek.de'


def getVideo(id):
	d = {}
	response = libMediathek.getUrl(baseUrl + '/AjaxEntry?ekey=' + id)
	j = json.loads(response)
	
	if file.endswith('.m3u8'):
		d['media'] = [{'url':file, 'type':'video', 'stream':'HLS'}]
	elif file.endswith('.m.mp4'):
		s = file.split('/')
		video = 'http://hls-ondemand.swr.de/i/swr-fernsehen/'+s[4]+'/'+s[5]+'/'+s[6]+'.,xl,l,ml,m,sm,s,.mp4.csmil/master.m3u8'
		d['media'] = [{'url':video, 'type':'video', 'stream':'HLS'}]
	elif file.endswith('.mp3'):
		d['media'] = [{'url':file, 'type':'audio', 'stream':'http'}]
		
	
	sub = re.compile("lucy2captionArray\((.+?)\)").findall(response)[0]
	if sub != "''":
		d['subtitle'] = [{'url':sub.replace("'",""), 'type': 'ttml', 'lang':'de'}]
	try:
		name = re.compile("title = '(.+?)'").findall(response)[-1]
		plot = re.compile("descl = '(.+?)'").findall(response)[-1]
		thumb = re.compile("image = '(.+?)'").findall(response)[-1]
		d['metadata'] = {'name':name, 'plot': plot, 'thumb':thumb}
	except: pass	
	return d
 
def startTimeToInt(s):
	HH,MM,SS = s.split(":")
	return int(HH) * 60 + int(MM)