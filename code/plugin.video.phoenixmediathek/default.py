# -*- coding: utf-8 -*-
import libmediathek3 as libMediathek
import resources.lib.jsonparser as jsonParser

params = libMediathek.get_params() 

def list():	
	libMediathek.list(modes, 'main', 'play')

def main():
	return jsonParser.parseMain()

def listVideos():
	return jsonParser.parseVideos(params['id'])

def play():
	result = jsonParser.getVideoUrl(params['smubl'])
	result = libMediathek.getMetadata(result)
	return result

modes = {
	'main': main,
	'listVideos': listVideos,
	'play': play
}	

list()