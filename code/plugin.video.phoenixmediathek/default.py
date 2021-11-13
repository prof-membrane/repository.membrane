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

# list()
# return

import xbmc
import xbmcgui

libMediathek.endOfDirectory()
dialog = xbmcgui.Dialog()
title = 'Phoenix Mediathek'
text = 'Die Inhalte dieser Mediathek sind seit 13.11.2021 ausschließlich über die ARD-Mediathek abrufbar.'
dialog.ok(title, text)
xbmc.executebuiltin('XBMC.ActivateWindow(Home)')
