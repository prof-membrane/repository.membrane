# -*- coding: utf-8 -*-
import json
import urllib
import time

import libmediathek3 as libMediathek
import libbrgraphqlqueries
import libbrgraphqlqueriesnew as queries

graphqlUrl = 'https://proxy-base.master.mango.express/graphql'
header = {'Content-Type':'application/json'	, 'Accept-Encoding':'gzip, deflate'}
	
	
def parseSeries():
	p = json.dumps({'query': queries.getQuerySeries()})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['allSeries']['edges']:
		d = {}
		node = edge['node']
		d['_name'] = node['title']
		d['_tvshowtitle'] = node['kicker']
		d['_plotoutline'] = node['kicker']
		d['_plot'] = node['kicker']
		if node['shortDescription'] != None:
			d['_plotoutline'] = node['shortDescription']
			d['_plot'] = node['shortDescription']
		if node['description'] != None:
			d['_plot'] = node['description']
		try:
			d['_thumb'] = node['defaultTeaserImage']['imageFiles']['edges'][0]['node']['publicLocation']
		except: pass
		#libMediathek.log(d['_thumb'])
		d['_type'] = 'dir'
		d['id'] = node['id']
		d['mode'] = 'libBrListEpisodes'
		l.append(d)
	return l	
	
def parseEpisodes(id):
	#variables = {'id':id,"itemCount":0,"clipCount":0,"previousEpisodesFilter":{"essences":{"empty":{"eq":False}},"broadcasts":{"empty":{"eq":False},"start":{"lte":"2017-09-13T17:00:28.592Z"}}},"clipsOnlyFilter":{"broadcasts":{"empty":{"eq":True}},"essences":{"empty":{"eq":False}}}}
	#variables = {'id':id,'day':"2018-05-27T17:30:00.000Z"}
	#variables = {'id':id,'day':time.strftime('%Y-%m-%dT%H:%M:%S.000Z',time.now())}
	variables = {'id':id,'day':time.strftime('%Y-%m-%dT%H:%M:%S.000Z')}
	p = json.dumps({'query': queries.getQueryEpisodes(), 'variables':variables})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	j = json.loads(response)
	print response
	l = []
	for edge in j['data']['viewer']['series']['episodes']['edges']:
		d = {}
		node = edge['node']
		d = _buildVideoDict(node)
		l.append(d)
	return l
	
	
	
def parseBoards():
	boards = [
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-film-krimi',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-kabarett-comedy',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-doku-reportage',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-news-politik',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-natur-tiere',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-wissen',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-berge',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-kultur',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-heimat',
		'Board:http://ard.de/ontologies/mangoLayout#discover2',
		'Board:http://ard.de/ontologies/mangoLayout#discover1',
		'Board:http://ard.de/ontologies/mangoLayout#entdecken-kinder',]
		
	variables = {'nodes':boards}
	p = json.dumps({'query': libbrgraphqlqueries.getCats(), 'variables':variables})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for node in j['data']['nodes']:
		d = {}
		d['_name'] = node['title'].title()
		if 'shortDescription' in node and node['shortDescription'] != None:
			d['_plotoutline'] = node['shortDescription']
			d['_plot'] = node['shortDescription']
		if 'description' in node and node['description'] != None:
			d['_plot'] = node['description']
		d['boardId'] = node['id']
		d['_type'] = 'dir'
		d['mode'] = 'libBrListBoard'
		l.append(d)
	return l
	
def parseBoard(boardId):
	variables = {'boardId':boardId}
	p = json.dumps({'query': queries.getQueryBoard(), 'variables':variables})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['board']['sections']['edges']:
		for edge2 in edge['node']['contents']['edges']:
			d = _buildVideoDict(edge2['node']['represents'])
			l.append(d)
	return l

def parseCategories():
	p = json.dumps({'query': queries.getQueryCategories()})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['allCategories']['edges']:
		d = {}
		node = edge['node']
		d['_name'] = node['label']
		d['id'] = node['id']
		d['_type'] = 'dir'
		d['mode'] = 'libBrListCategorie'
		l.append(d)
	return l
	
def parseCategorie(categorie):
	#filter = {'filter':{'categories':{'contains':categorie}}}
	#{"filter": {"categories": {"contains": "av:http://ard.de/ontologies/categories#gesundheit"}}}
	filter = {"categories": {"contains": categorie}}
	#filter = '{filter:{categories:{contains:'+categorie+'}}}'
	return _parseAllClips(filter)

def parseGenres():
	p = json.dumps({'query': queries.getQueryGenres()})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['allGenres']['edges']:
		d = {}
		node = edge['node']
		d['_name'] = node['label']
		d['id'] = node['id']
		d['_type'] = 'dir'
		d['mode'] = 'libBrListGenre'
		l.append(d)
	return l
	
def parseGenre(genre):
	filter = {'genres':{'contains':genre}}
	return _parseAllClips(filter)
	
def parseSections():
	p = json.dumps({'query': queries.getQuerySections()})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['allSections']['edges']:
		d = {}
		node = edge['node']
		if node['title'] == None:
			d['_name'] = 'None'
		else:
			d['_name'] = node['title']
		d['id'] = node['id']
		d['_type'] = 'dir'
		d['mode'] = 'libBrListSection'
		l.append(d)
	return l
	
def parseSection(id):
	variables = {'id':id}
	p = json.dumps({'query': queries.getQuerySection(), 'variables':variables})
	libMediathek.log(p)
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['section']['contents']['edges']:
		d = _buildVideoDict(edge['node']['represents'])
		l.append(d)
	return l
	
#channels:
#ARD_alpha
#BR_Fernsehen
#BRde
def parseDate(day,channel):
	variables = {"slots": ["MORNING","NOON","EVENING","NIGHT"], "day": day, "broadcasterId":"av:http://ard.de/ontologies/ard#"+channel}
	p = json.dumps({'query': queries.getQueryDate(), 'variables':variables})
	libMediathek.log(p)
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for epg in j['data']['viewer']['allLivestreams']['edges'][0]['node']['epg']:
		broadcastEvent = epg['broadcastEvent']
		publicationOf = broadcastEvent['publicationOf']
		if len(publicationOf['essences']['edges']) != 0:
			d = _buildVideoDict(publicationOf)
			d['_airedtime'] = broadcastEvent['start'][11:16]
			d['_type'] = 'date'
			l.append(d)
	return l
	
def parseSearch(term):
	filter = {"term":term,"audioOnly":{"eq":False},"essences":{"empty":{"eq":False}},"status":{"id":{"eq":"av:http://ard.de/ontologies/lifeCycle#published"}}}
	return _parseAllClips(filter)
	
	
def parseVideo(id):
	variables = {'clipId':id}
	#variables = {'clipId':'av:5896c99cab0d0d001203ea82'}
	#variables = {'clipId':'av:5a3caa4ec96563001843d591'}
	p = json.dumps({'query': queries.getQueryVideo(), 'variables':variables})
	libMediathek.log(p)
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []	
	node = j['data']['viewer']['clip']['videoFiles']['edges'][0]['node']
	d = {}
	d['media'] = []
	d['media'].append({'url':node['publicLocation'], 'stream':'HLS'})
	try:
		sub = node['subtitles']['edges'][0]['node']['timedTextFiles']['edges'][0]['node']['publicLocation']
		d['subtitle'] = [{'url':sub, 'type': 'ttml', 'lang':'de'}]
	except: pass
	return d
	
def _parseAllClips(filter):
	variables = {'filter':filter}
	p = json.dumps({'query': queries.getQueryAllClips(), 'variables':variables})
	libMediathek.log(p)
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['allClips']['edges']:
		d = _buildVideoDict(edge['node'])
		l.append(d)
	return l
	
	
	
def _buildVideoDict(node):
	d = {}
	d['_name'] = node['title']
	d['_tvshowtitle'] = node['kicker']
	d['_plotoutline'] = node['kicker']
	d['_plot'] = node['kicker']
	if node['shortDescription'] != None and node['shortDescription'] != '':
		d['_plotoutline'] = node['shortDescription']
		d['_plot'] = node['shortDescription']
	if node['description'] != None and node['description'] != '':
		d['_plot'] = node['description']
	if 'duration' in node:
		d['_duration'] = str(node['duration'])
	try:
		d['_thumb'] = node['defaultTeaserImage']['imageFiles']['edges'][0]['node']['publicLocation'] + '?w=600&q=70'
	except: pass
	#libMediathek.log(d['_thumb'])
	d['_type'] = 'video'
	d['id'] = node['id']
	d['mode'] = 'libBrPlay'
	return d
	
	
	
	
	
	
	
def parseNew(boardId='l:http://ard.de/ontologies/mangoLayout#mainBoard_web',itemCount=50):
	#variables = {'boardId':boardId,"itemCount":itemCount}
	variables = {'boardId':boardId}
	#p = json.dumps({'query': libbrgraphqlqueries.getStart(), 'variables':variables})
	p = json.dumps({'query': queries.getQueryBoard(), 'variables':variables})
	libMediathek.log(p)
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
	j = json.loads(response)
	l = []
	for edge in j['data']['viewer']['board']['stageTeaserSection']['edges'][1]['node']['verticalSectionContents']['edges']:
		d = {}
		node = edge['node']['represents']
		d['_name'] = node['title']
		d['_tvshowtitle'] = node['kicker']
		d['_plotoutline'] = node['kicker']
		d['_plot'] = node['kicker']
		if node['shortDescription'] != None:
			d['_plotoutline'] = node['shortDescription']
			d['_plot'] = node['shortDescription']
		if node['description'] != None:
			d['_plot'] = node['description']
		d['_duration'] = str(node['duration'])
		d['_thumb'] = node['defaultTeaserImage']['imageFiles']['edges'][0]['node']['publicLocation']
		#libMediathek.log(d['_thumb'])
		d['_type'] = 'video'
		d['id'] = node['id']
		d['mode'] = 'libBrPlay'
		l.append(d)
	return l
		
def search(searchString):
	j = _parseMain()
	url = j["_links"]["search"]["href"].replace('{term}',urllib.quote_plus(searchString))
	return parseLinks(url)
	
def parseLinks(url):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	l = []
	if not '_embedded' in j:
		return l
	for show in j["_embedded"]["teasers"]:
		d = {}
		d['url'] = show["_links"]["self"]["href"]
		d['_name'] = show["topline"]
		if 'headline' in show:
			d['_name'] += ' - ' + show['headline']
			d['_tvshowtitle'] = show['topline']
			
		d['_subtitle'] = show["topline"]
		d['_plot'] = show["teaserText"]
		d['_channel'] = show["channelTitle"]
		duration = show['documentProperties']["br-core:duration"].split(':')
		d['_duration'] = str(int(duration[0]) * 3600 + int(duration[1]) * 60 + int(duration[2]))
		
		if 'image512' in show["teaserImage"]["_links"]:
			d['_thumb'] = show["teaserImage"]["_links"]["image512"]["href"]
		elif 'image256' in show["teaserImage"]["_links"]:
			d['_thumb'] = show["teaserImage"]["_links"]["image256"]["href"]
		try:
			if show['hasSubtitle']:
				d['_hasSubtitle'] = 'true'
				#d['plot'] += '\n\nUntertitel'
		except:pass
		d['_type'] = 'video'
		d['mode'] = 'libBrPlayOld'
		
		l.append(d)
	try:
		d = {}
		d['_type'] = 'nextPage'
		d['url'] = j['_embedded']['_links']['next']['href']
		l.append(d)
	except: pass
	return l
			
	
def parse(url):
	l = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)

def startTimeToInt(s):
	HH,MM,SS = s.split(":")
	return int(HH) * 60 + int(MM)
	
	
	
def getIntrospection():
	p = json.dumps({'query': libbrgraphqlqueries.getIntrospectionQuery()})
	response = libMediathek.getUrl(graphqlUrl,header,post=p)
	libMediathek.log(response)
