# -*- coding: utf-8 -*-
import libmediathek3 as libMediathek
import resources.lib.jsonparser as jsonParser

def main():
	return jsonParser.parseMain()
	
def listVideos():
	return jsonParser.parseVideos(params['id'])
	
def play():
	return jsonParser.getVideoUrl(params['smubl'])


modes = {
'main': main,
'listVideos': listVideos,
'play': play
}	

def list():	
	global params
	params = libMediathek.get_params()
	
	mode = params.get('mode','main')
	if mode == 'play':
		libMediathek.play(play())
	else:
		l = modes.get(mode)()
		libMediathek.addEntries(l)
		libMediathek.endOfDirectory()
list()