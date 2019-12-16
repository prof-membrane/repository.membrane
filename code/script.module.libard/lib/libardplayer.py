#!/usr/bin/python
# -*- coding: utf-8 -*-
# import xbmc
import re
import sys
import json
import urllib
import libmediathek3 as libMediathek

if sys.version_info[0] < 3:
	alt_str_type = unicode
else:
	alt_str_type = bytes

videoQuality = 10000000000000000

def getVideoUrl(url=False,videoID=False):
	if not videoID:
		videoID = url.split('documentId=')[1]
		if '&' in videoID:
			videoID = videoID.split('&')[0]
	if url:
		content = libMediathek.getUrl(url)
		match = re.compile('<div class="box fsk.*?class="teasertext">(.+?)</p>', re.DOTALL).findall(content)
	#if match:
	if False:
		#xbmc.executebuiltin('XBMC.Notification(Info:,'+match[0].strip()+',15000)')
		return False
	else:
		return fetchJsonVideo(videoID)
		#return fetchTvaVideo(videoID)

def fetchJsonVideo(id):
	d = {}
	response = libMediathek.getUrl('http://www.ardmediathek.de/play/media/'+id)
	j = json.loads(response)
	if '_subtitleUrl' in j:
		d['subtitle'] = [{'url':j['_subtitleUrl'], 'type': 'ttml', 'lang':'de'}]
	quality = -1
	for mediaArray in j['_mediaArray']:
		for mediaStreamArray in mediaArray['_mediaStreamArray']:
			currentQuality = mediaStreamArray.get('_quality',-1);
			if (isinstance(currentQuality,str) or isinstance(currentQuality,alt_str_type)): 
				if (currentQuality == 'auto'):
					currentQuality = sys.maxsize
				else: 
					currentQuality = -1
			if currentQuality > quality:
				if isinstance(mediaStreamArray['_stream'],list):
					# xbmc.log('%s' % ( mediaStreamArray['_stream'][0] ), xbmc.LOGFATAL)
					finalUrl = mediaStreamArray['_stream'][0]
					quality = currentQuality
				else:
					# xbmc.log('%s' % ( mediaStreamArray['_stream'] ), xbmc.LOGFATAL)
					finalUrl = mediaStreamArray['_stream']
					quality = currentQuality
	if finalUrl.startswith('//'):
		finalUrl = 'http:' + finalUrl
	if finalUrl.startswith('http://wdradaptiv') or finalUrl.endswith('.mp4'):
		d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'mp4'}]
	else:
		d['media'] = [{'url':finalUrl, 'type': 'video', 'stream':'HLS'}]
	return d

def fetchTvaVideo(id):
	xml = libMediathek.getUrl('http://www.ardmediathek.de/ard/servlet/export/tva/id='+id+'/index.xml')
	if "crid://ard.de/videolive" in xml:
		return False
	#try:
	#	programURL = re.compile('<tva:ProgramURL>(.+?)</tva:ProgramURL>', re.DOTALL).findall(xml)[0]
	#	if programURL.endswith('.mp3'):
	#		return programURL
	#except: pass
	
	match = re.compile('<tva:OnDemandProgram>(.+?)</tva:OnDemandProgram>', re.DOTALL).findall(xml)
	finalUrl = False
	qualityHLS = 0
	for item in match:
		videoUrl = re.compile('<tva:ProgramURL>(.+?)</tva:ProgramURL>', re.DOTALL).findall(item)[0]
		if not 'rtmp://' in videoUrl and not 'rtmpt://' in videoUrl and not 'manifest.f4m' in videoUrl:
			quality = re.compile('<tva:FileFormat href="urn:ard:tva:metadata:cs:ARDFormatCS:(.+?)"/>', re.DOTALL).findall(item)[0]
			if 'smil/master.m3u8' in videoUrl:
				if quality in qualityDictHLS:
					q = qualityDictHLS[quality]
				else:
					q = 1
				if q >= qualityHLS:
					finalUrl = videoUrl
					qualityHLS = q
			else:
				if quality in qualityDict2:
					if qualityDict2[quality] <= videoQuality:
						selectedVideoUrl = videoUrl
	if not finalUrl:
		finalUrl = selectedVideoUrl
		finalUrl = ndrPodcastHack(finalUrl)
		finalUrl = dwHack(finalUrl)
	if finalUrl.startswith('//'):
		finalUrl = 'http:' + finalUrl
	d = {'media': [{'url':finalUrl, 'type': 'video', 'stream':'hls'}]}
	metadata = {}
	try:
		metadata['name'] = re.compile('<tva:Title type="main">(.+?)</tva:Title>', re.DOTALL).findall(xml)[0]
	except:
		pass
	try:
		s = xml.split('<tva:Format href="urn:ard:tva:metadata:cs:ARDFormatCS:2014:4.4.11.0.6"/>')[1]
		metadata['thumb'] = re.compile('<mpeg7:MediaUri>(.+?)</mpeg7:MediaUri>', re.DOTALL).findall(s)[0]
		metadata['plot'] = re.compile('<ard:alternativeText>(.+?)</ard:alternativeText>', re.DOTALL).findall(s)[0]
		metadata['name'] = re.compile('<tva:Title type="main">(.+?)</tva:Title>', re.DOTALL).findall(xml)[0]
	except:
		pass
	d['metadata'] = metadata
	return d

def ndrPodcastHack(url):
	try:
		if url.startswith('http://media.ndr.de/download/podcasts/'):
			#http://media.ndr.de/download/podcasts/minuten805/TV-20160115-1405-2242.h264.mp4
			#http://hls.ndr.de/i/ndr/2016/0115/TV-20160115-1405-2242.,lo,hi,hq,hd,.mp4.csmil/master.m3u8
			
			uri = url.split('/')[-1]
			YYYYMMDD = uri.split('-')[1]
			YYYY = YYYYMMDD[:4]
			MMDD = YYYYMMDD[4:]
			
			return 'http://hls.ndr.de/i/ndr/' + YYYY + '/' + MMDD + '/' + uri.replace('.h264.mp4','.,lo,hi,hq,hd,.mp4.csmil/master.m3u8')
	except: pass
	return url
def dwHack(url):
	try:
		if url.startswith('http://tv-download.dw.de'):
			#return url.replace('_sd.mp4','_hd.mp4')
			return url.replace('_sd.mp4','_hd_dwdownload.mp4')
	except: pass
	return url
### video type to bitrate###
qualityDict = {'2012:1.58': 1620000,
			   '2012:1.83': 47000,
			   '2012:1.54': 608000,
			   '2012:1.28': 0,
			   '2014:1.2.3.14.1': 3814000,
			   '2014:1.2.3.12.2': 1725000,
			   '2014:1.2.3.11.1': 1149000,
			   '2014:1.2.3.9.1': 639000,
			   '2014:1.2.3.7.1': 380000,
			   '2014:1.2.3.6.1': 319000};
###video type to rating###
qualityDict2 = {'2012:1.58': 29,
			   '2012:1.83': 1,
			   '2012:1.54': 9,
			   '2012:1.28': 0,
			   '2014:1.2.3.14.1': 40,
			   '2014:1.2.3.12.2': 30,
			   '2014:1.2.3.11.1': 20,
			   '2014:1.2.3.9.1': 10,
			   '2014:1.2.3.7.1': 8,
			   '2014:1.2.3.6.1': 7};

qualityDictHLS = {'2014:5.2.13.14.1': 100,
				  '2014:5.2.13.12.1': 95,
				  '2012:5.28': 90,
				  '2012:5.10': 50,
				  '2012:1.65': 1,};