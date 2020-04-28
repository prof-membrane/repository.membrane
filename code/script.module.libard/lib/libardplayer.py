#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import libmediathek3 as libMediathek


def getVideoUrlClassic(url=False,videoID=False):
	if not videoID:
		videoID = url.split('documentId=')[1]
		if '&' in videoID:
			videoID = videoID.split('&')[0]
	return fetchJsonVideo(videoID)

def fetchJsonVideo(id):
	media = []
	response = libMediathek.getUrl('http://www.ardmediathek.de/play/media/'+id)
	j = json.loads(response)
	for mediaArray in j['_mediaArray']:
		for stream in mediaArray['_mediaStreamArray']:
			if isinstance(stream['_stream'],list):
				url = stream['_stream'][0]
			else:
				url = stream['_stream']
			if url.startswith('//'):
				url = 'http:' + url
			quality = stream.get('_quality',-1);
			if quality == 'auto':
				media.insert(0,{'url':url, 'type':'video', 'stream':'HLS'})
			elif url[-4:].lower() == '.mp4':
				try:
					quality = int(quality)
				except ValueError:
					pass
				else:
					media.append({'url':url, 'type':'video', 'stream':'mp4', 'bitrate':quality})
	ignore_adaptive = libMediathek.getSettingBool('ignore_adaptive')
	while ignore_adaptive and len(media) > 1 and media[0]['stream'] == 'HLS':
		del media[0]
	if media:
		result = dict(media = media)
		if '_subtitleUrl' in j:
			result['subtitle'] = [{'url':j['_subtitleUrl'], 'type':'ttml', 'lang':'de'}]
 		return result
	else: 
		return None
