# -*- coding: utf-8 -*-
import re
import libmediathek3 as libMediathek

def enrichEpg(l,date):
	epg = []
	newL = []
	response = libMediathek.getUrl('https://www.3sat.de/programm/?viewlong=viewlong&d=20170521')
	response = response.split('<div id="EpgLongView" class="EpgBody">')[1]
	response = response.split('<div id="FlagEpg" class="FlagLoaded">')[0]
	response = response.split('class="EpgItemDay"')[1:]
	for item in response:
		time = re.compile('<div class="EpgTimeDay">(.+?)<', re.DOTALL).findall(item)[0]
		if 'class="EpgTextL"' in item:
			plotS = re.compile('class="EpgTextS">.+?</a>(.+?)</div>', re.DOTALL).findall(item)[0]
			plotL = re.compile('class="EpgTextL">.+?</a>(.+?)</div>', re.DOTALL).findall(item)[0]
		else:
			plotS = re.compile('<h4.+?>(.+?)</h4>', re.DOTALL).findall(item)[0]
			plotL = plotS
			
		plotS = plotS.replace('<br/><br/><br/>',' ').replace('<br/><br/>',' ').replace('<br/>',' ')
		plotL = plotL.replace('<br/><br/><br/>','\n\n').replace('<br/><br/>','\n\n').replace('<br/>','\n')
		epg.append([time,plotL,plotS])
	
	for item in l:
		d = item
		for epgTime,epgPlot,epgPlotShorted in epg:
			if item['_plot'][:-5] in epgPlotShorted:
				d['_plot'] = '###' + epgPlot
				if item['_date'] == '23:59':
					d['_date'] = epgTime
		newL.append(d)
	return newL