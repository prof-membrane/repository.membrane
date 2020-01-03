# -*- coding: utf-8 -*-
import sys
import json
import libmediathek3 as libMediathek

if sys.version_info[0] < 3: # for Python 2
	from HTMLParser import HTMLParser
else: # for Python 3
	from html.parser import HTMLParser

pluginpath = 'plugin://script.module.libArd/'

def parse(url):
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	
def parseDate(url):
	l = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	j1 = j["sections"][-1]["modCons"][0]["mods"][0]["inhalte"]
	for entry in j1:
		j2 = entry["inhalte"]
		for entry in j2:
			d = {}
			d["_airedtime"] = entry["dachzeile"]
			d["name"] = '(' + d["_airedtime"] + ') ' + entry["ueberschrift"]
			duration = 0
			for j3 in entry["inhalte"]:
				if runtimeToInt(j3["unterzeile"]) > duration:
					duration = runtimeToInt(j3["unterzeile"])
					d["plot"] = HTMLParser().unescape(j3["ueberschrift"])
					thumb = j3["bilder"][0]["schemaUrl"].replace("##width##","1024")
					d["thumb"] = thumb.split("?")[0]
					d["url"] = j3["link"]["url"]
					d["documentId"] = j3["link"]["url"].split("player/")[1].split("?")[0]
					d["_duration"] = str(runtimeToInt(j3["unterzeile"]))
					d["_type"] = 'video'
					d['mode'] = 'libArdPlay'
			l.append(d)
	return l
		
def parseAZ(letter='A'):
	if letter == "0-9":
		letter = '#'
	l = []
	response = libMediathek.getUrl("http://www.ardmediathek.de/appdata/servlet/tv/sendungAbisZ?json")
	j = json.loads(response)
	j1 = j["sections"][0]["modCons"][0]["mods"][0]["inhalte"]
	for entries in j1:
		#if entry["ueberschrift"] == letter.upper():
		if True:
			for entry in entries["inhalte"]:
				d = {}
				ueberschrift = entry["ueberschrift"]
				unterzeile = entry["unterzeile"]
				dachzeile = entry["dachzeile"]
				dachzeile = dachzeile.split(' ')[0]
				thumb = entry["bilder"][0]["schemaUrl"].replace("##width##","1024")
				thumb = thumb.split("?")[0]
				url = entry["link"]["url"]

				if sys.version_info[0] < 3: # for Python 2
					ueberschrift = ueberschrift.encode('utf-8')
					unterzeile = unterzeile.encode('utf-8')
					dachzeile = dachzeile.encode('utf-8')
					thumb = thumb.encode('utf-8')
					url = url.encode('utf-8')

				d["name"] = ueberschrift
				d["plot"] = HTMLParser().unescape(ueberschrift)
				d["_channel"] = unterzeile 
				d["_entries"] = int(dachzeile)
				d["thumb"] = thumb 
				d["url"] = url
				d['mode'] = 'libArdListVideos'
				d["_type"] = 'dir'

				l.append(d)


	return l
	
def parseVideos(url):
	l = []
	response = libMediathek.getUrl(url)
	j = json.loads(response)
	#j1 = j["sections"][-1]["modCons"][-1]["mods"][-1]
	#j1 = j["sections"][-1]["modCons"][-1]["mods"][-1]
	j1 = j["sections"][-1]["modCons"][-1]["mods"][-1]
	
	for j2 in j1["inhalte"]:
		d = {}
		if "ueberschrift" in j2:
			ueberschrift = j2["ueberschrift"]
			if sys.version_info[0] < 3: # for Python 2
				ueberschrift = ueberschrift.encode('utf-8')
			d["name"] = ueberschrift
			d["plot"] = HTMLParser().unescape(ueberschrift)
			if 'Hörfassung' in d["name"] or 'Audiodeskription' in d["name"]:
				d["name"] = d["name"].replace(' - Hörfassung','').replace(' - Audiodeskription','')
				d["name"] = d["name"].replace(' (mit Hörfassung)','').replace(' (mit Audiodeskription)','')
				d["name"] = d["name"].replace(' mit Hörfassung','').replace(' mit Audiodeskription','')
				d["name"] = d["name"].replace(' (Hörfassung)','').replace(' (Audiodeskription)','')
				d["name"] = d["name"].replace(' Hörfassung','').replace(' Audiodeskription','')
				d["name"] = d["name"].replace('Hörfassung','').replace('Audiodeskription','')
				d["name"] = d["name"].strip()
				if d["name"].endswith(' -'):
					d["name"] = d["name"][:-2]
				d["name"] = d["name"] + ' - Hörfassung'
				d["_audioDesc"] = True
				
		if "unterzeile" in j2:
			d["_duration"] = str(runtimeToInt(j2["unterzeile"]))
		if "bilder" in j2:
			thumb = j2["bilder"][0]["schemaUrl"].replace("##width##","1024")
			thumb = thumb.split("?")[0]
			if sys.version_info[0] < 3: # for Python 2
				thumb = thumb.encode('utf-8')
			d["thumb"] = thumb
		if "teaserTyp" in j2:
			if j2["teaserTyp"] == "PermanentLivestreamClip" or j2["teaserTyp"] == "PodcastClip":
				continue
			elif j2["teaserTyp"] == "OnDemandClip":
				d["_type"] = 'video'
				d['mode'] = 'libArdPlay'
			elif j2["teaserTyp"] == "Sammlung":
				d["_type"] = 'dir'
				d['mode'] = 'libArdListVideos'
			else:
				libMediathek.log('json parser: unknown item type: ' + j2["teaserTyp"])
				d["_type"] = 'dir'
				d['mode'] = 'libArdListVideos'
				
		if "link" in j2:
			url = j2["link"]["url"]
			documentId = j2["link"]["url"].split("/player/")[-1].split("?")[0]
			if sys.version_info[0] < 3: # for Python 2
				url = url.encode('utf-8')
				documentId = documentId.encode('utf-8')
			d["url"] = url
			d["documentId"] = documentId
		if "dachzeile" in j2:
			dachzeile = j2["dachzeile"]
			if sys.version_info[0] < 3: # for Python 2
				dachzeile = dachzeile.encode('utf-8')
			d["_releasedate"] = dachzeile
		if 'ut' in j2['kennzeichen']:
			d["_subtitle"] = True
		if 'geo' in j2['kennzeichen']:
			d['_geo'] = 'DACH'
		if 'fsk6' in j2['kennzeichen']:
			d['_mpaa'] = 'FSK6'
		if 'fsk12' in j2['kennzeichen']:
			d['_mpaa'] = 'FSK12'
		if 'fsk16' in j2['kennzeichen']:
			d['_mpaa'] = 'FSK16'
		if 'fsk18' in j2['kennzeichen']:
			d['_mpaa'] = 'FSK18'
		#d["_pluginpath"] = pluginpath
		
		
		l.append(d)
	
	aktiv = False
	for buttons in j1['buttons']:
		if buttons["label"]["text"] == "Seiten":
			for button in buttons["buttons"]:
				if aktiv:
					d = {}
					d["url"] = button["buttonLink"]["url"]
					d["type"] = 'nextPage'
					d['mode'] = 'libArdListVideos'
					l.append(d)
				aktiv = button['aktiv']
	return l
	
	
def runtimeToInt(runtime):
	try:
		if '|' in runtime:
			for s in runtime.split('|'):
				if 'Min' in s:
					runtime = s
		if '<br>' in runtime:
			runtime = runtime.split('<br>')[0]
		t = runtime.replace('Min','').replace('min','').replace('.','').replace(' ','').replace('|','').replace('UT','')
		HHMM = t.split(':')
		if len(HHMM) == 1:
			return int(HHMM[0])*60
		else:
			return int(HHMM[0])*60 + int(HHMM[1])
	except: 
		return ''