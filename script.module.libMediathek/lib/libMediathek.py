# -*- coding: utf-8 -*-
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import urllib
import sys
import json
import _libMediathekUtils as _utils
import time
import socket

from datetime import date, timedelta

startTime = int(round(time.time() * 1000))
def log(message = False):
	xbmc.log('Unithek Log: '+str(message))
def logTime():
	xbmc.log('libm Log: Runtime '+str(int(round(time.time() * 1000)) - startTime)+'ms')
logTime()
def ttml2Srt(url):
	import libMediathekTtml2Srt
	return libMediathekTtml2Srt.newSubtitle(url)
listCacheFile = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'cache.json').decode('utf-8')
cacheInfosFile = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'cacheinfos.json').decode('utf-8')
profilePath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode('utf-8')
_utils.f_mkdir(profilePath)
hideAudioDisa = True
icon = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')+'/icon.png').decode('utf-8')
fanart = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')+'/fanart.jpg').decode('utf-8')
translation = xbmcaddon.Addon(id='script.module.libMediathek').getLocalizedString

def checkIfCachedVersionIsAvailable():
	try:#TODO investigate
		j = _retrieveJson(cacheInfosFile)
		if sys.argv[2] == j.get('path','') and j.get('page',1) > 1:
			return True
		else: return False
	except: return False
	
def retrieveCached():
	xbmc.log('########## USING CACHED VERSION')
	for dict in _retrieveJson(listCacheFile):
		addEntry(dict)
		
def addE(dict,wnd):#not working properly :(
			
	u = _buildUri(dict)
	ilabels = {
		"Title": cleanString(dict.get('name','')),
		"Plot": cleanString(dict.get('plot','')),
		"Plotoutline": cleanString(dict.get('plot','')),
		"Duration": dict.get('duration',''),
		"Mpaa": dict.get('mpaa','')
		}
	ok=True
	liz=xbmcgui.ListItem(cleanString(dict.get('name','')), iconImage="DefaultFolder.png", thumbnailImage=dict.get('thumb',icon))
	liz.setInfo( type="Video", infoLabels=ilabels)
	liz.setProperty('fanart_image',dict.get('fanart',dict.get('thumb',fanart)))
	if 'type' in dict and dict['type'] == 'video':
		liz.setProperty('IsPlayable', 'true')
	wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
	wnd.getControl(wnd.getFocusId()).addItem(liz)
	
def addEntries(l,page=-1):
	"""
	liz=xbmcgui.ListItem('TEST', iconImage="DefaultFolder.png")
	wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
	a = wnd.getControl(wnd.getFocusId())
	#a = wnd.getControl(wnd.getFocus())
	#a = wnd.getControl(wnd.getFocusId()).getListItem(1)
	log('#################wnd')
	xbmc.log(str(xbmcgui.getCurrentWindowId()))
	xbmc.log(str(wnd))
	
	log(str(wnd.getControl(wnd.getFocusId()).size()))
	log(str(a))
	log(str(a.getSelectedItem()))
	a.addItem('test')
	xbmc.sleep(2000)
	a.addItem('test2')
	#"""
	
	"""
	s = socket.socket()         # Create a socket object
	host = 'localhost' # Get local machine name
	port = 12345    
	
	dump = json.dumps(l+[{'page': '1'}])
	s.connect((host,port))
	s.send(dump)
	s.close()
	return
	#"""
	if True:
		return _buildDir(l)
	log("###########handle")
	log(str(sys.argv[1]))
	log("###########listsize")
	try:
		wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
		a = wnd.getControl(wnd.getFocusId()).getSelectedPosition()
		log(str(a))
		#d = dir(wnd.getControl(wnd.getFocusId()))
		#for i in d:
		#	log(str(i))
		log(str(wnd.getControl(wnd.getFocusId()).size()))
	except:
		pass
	logTime()
	if page == 1:
		saveCache = True
	elif page > 1:
		j = _retrieveJson(listCacheFile)[:-1]
		l = j + l
		saveCache = True
	else:
		saveCache = False
	log('logging dir build time')
	logTime()
	#for dict in l:
	#	addE(dict)
	_buildDir(l)
	log('finished')
	logTime()
	cacheInfo = {}
	cacheInfo['path'] = sys.argv[2]
	cacheInfo['page'] = page
	
		
	if page == 1:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))	
		try:
			xbmc.sleep(50)
			wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
			wnd.getControl(wnd.getFocusId()).selectItem(0)
			xbmc.log(str(wnd.getControl(wnd.getFocusId()).getSelectedPosition()))
		except: pass
	elif page > 1:
		try:
			log('...')
			#xbmc.executebuiltin("XBMC.Container.Update()")
			#wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
			#xbmcplugin.endOfDirectory(int(sys.argv[1]), updateListing = True, cacheToDisc = False)
			#xbmc.sleep(100)
			#wnd.getControl(wnd.getFocusId()).selectItem(0)
			#wnd.getControl(wnd.getFocusId()).selectItem(len(j)+1)
		except: pass
	else:
		xbmcplugin.endOfDirectory(int(sys.argv[1]))	
		
	if saveCache:
		_saveJson(listCacheFile,l)
	_saveJson(cacheInfosFile,cacheInfo)
	log('addentries ends')
	logTime()
def _saveJson(f,j):
	data = json.dumps(j)
	_utils.f_write(f,data)
def _retrieveJson(f):
	data = _utils.f_open(f)
	return json.loads(data)
"""	
def _buildDir2(l):
	wnd = xbmcgui.Window(xbmcgui.getCurrentWindowId())
	a = wnd.getControl(wnd.getFocusId())
	lists = []
	ok = False
	for dict in l:
		for key in dict:#sigh
			if isinstance(dict[key], unicode):
				dict[key] = dict[key].encode('utf-8')
		#xbmc.log(str(dict))
		if 'type' in dict and dict['type'] == 'nextPage':
			dict['name'] = translation(31040)
		if isinstance(dict["name"], unicode):
			dict["name"] = dict["name"].encode('utf-8')
		dict["name"] = cleanString(dict["name"])
		#dict["name"] = dict["name"].replace('&amp;','&')
		#if hideAudioDisa:
		#	if 'Hörfassung' in dict["name"] or 'Audiodeskription' in dict["name"]:
		#		return False
				
		u = _buildUri(dict)
		ilabels = {
			"Title": cleanString(dict.get('name','')),
			"Plot": cleanString(dict.get('plot','')),
			"Plotoutline": cleanString(dict.get('plot','')),
			"Duration": dict.get('duration',''),
			"Mpaa": dict.get('mpaa','')
			}
		ok=True
		liz=xbmcgui.ListItem(cleanString(dict.get('name','')), iconImage="DefaultFolder.png", thumbnailImage=dict.get('thumb',icon))
		#liz.setInfo( type="Video", infoLabels={ "Title": cleanString(dict.get('name','')) , "Plot": cleanString(dict.get('plot','')) , "Plotoutline": cleanString(dict.get('plot','')) , "Duration": dict.get('duration','') } )
		liz.setInfo( type="Video", infoLabels=ilabels)
		liz.setProperty('fanart_image',dict.get('fanart',dict.get('thumb',fanart)))
		
		if dict.get('type',None) == 'video' or dict.get('type',None) == 'live':
			liz.setProperty('IsPlayable', 'true')
			lists.append([u,liz,False])
		elif 'type' in dict and dict['type'] == 'nextPage':
			#lists.append([u,liz,True])
			lists.append([u,liz,False])
		else:
			lists.append([u,liz,True])
		a.addItem(liz)
	#a.addItems(lists)
	#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )		
	return ok
"""
def _buildDir(l):
	lists = []
	ok = False
	for dict in l:
		for key in dict:#sigh
			if isinstance(dict[key], unicode):
				dict[key] = dict[key].encode('utf-8')
		#xbmc.log(str(dict))
		if 'type' in dict and dict['type'] == 'nextPage':
			dict['name'] = translation(31040)
			dict['mode'] = get_params()['mode']
		if isinstance(dict["name"], unicode):
			dict["name"] = dict["name"].encode('utf-8')
		dict["name"] = cleanString(dict["name"])
		if 'type' in dict and dict['type'] == 'date' and 'airedtime' in dict:
			dict["name"] = '(' + str(dict["airedtime"]) + ') ' + dict["name"]
		elif 'type' in dict and dict['type'] == 'date' and 'time' in dict:
			dict["name"] = '(' + str(dict["date"]) + ') ' + dict["name"]
		#dict["name"] = dict["name"].replace('&amp;','&')
		#if hideAudioDisa:
		#	if 'Hörfassung' in dict["name"] or 'Audiodeskription' in dict["name"]:
		#		return False
				
		u = _buildUri(dict)
		ilabels = {
			"Title": cleanString(dict.get('name','')),
			"Plot": cleanString(dict.get('plot','')),
			"Plotoutline": cleanString(dict.get('plot','')),
			"Duration": dict.get('duration',''),
			"Mpaa": dict.get('mpaa',''),
			"Aired": dict.get('aired',''),
			"Studio": dict.get('channel',''),
			}
		if 'episode' in dict: 
			ilabels['Episode'] = dict['episode']
		if 'Season' in dict: 
			ilabels['Season'] = dict['season']
		if 'tvshowtitle' in dict: 
			ilabels['tvshowtitle'] = dict['tvshowtitle']
			ilabels['tagline'] = dict['tvshowtitle']
			ilabels['album'] = dict['tvshowtitle']
		ok=True
		#liz=xbmcgui.ListItem(cleanString(dict.get('name','')), iconImage="DefaultFolder.png", thumbnailImage=dict.get('thumb',icon))
		liz=xbmcgui.ListItem(cleanString(dict.get('name','')))
		#liz.setInfo( type="Video", infoLabels={ "Title": cleanString(dict.get('name','')) , "Plot": cleanString(dict.get('plot','')) , "Plotoutline": cleanString(dict.get('plot','')) , "Duration": dict.get('duration','') } )
		liz.setInfo( type="Video", infoLabels=ilabels)
		#if 'hasSubtitle' in dict:
		liz.addStreamInfo('subtitle', {'language': 'deu'})
		#if True:
			#liz.addStreamInfo('subtitle',{'language':'de'})
		#liz.setProperty('fanart_image',dict.get('fanart',dict.get('thumb',fanart)))
		#try:
		art = {}
		art['thumb'] = dict.get('thumb')
		art['landscape'] = dict.get('thumb')
		#art['poster'] = dict.get('thumb')
		art['fanart'] = dict.get('fanart',dict.get('thumb',fanart))
		art['icon'] = dict.get('channelLogo','')
		#art.append({'landscape': dict.get('thumb')})
		#art.append({'fanart': dict.get('fanart',dict.get('thumb',fanart))})
		#xbmc.log(str(art))
		liz.setArt(art)
		#except: pass
		if 'type' in dict:
			if dict.get('type',None) == 'video' or dict.get('type',None) == 'live' or dict.get('type',None) == 'date':
				xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )
				liz.setProperty('IsPlayable', 'true')
				lists.append([u,liz,False])
			elif 'type' in dict and dict['type'] == 'nextPage':
				#lists.append([u,liz,True])
				lists.append([u,liz,True])
			elif dict['type'] == 'shows':
				#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )
				xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="tvshows" )
				lists.append([u,liz,True])
			else:
				xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="files" )
				lists.append([u,liz,True])
		else:
			#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="files" )
			lists.append([u,liz,True])
	xbmcplugin.addDirectoryItems(int(sys.argv[1]), lists)
	#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )		
	return ok

def addEntry(dict):	
	for key in dict:#sigh
		if isinstance(dict[key], unicode):
			dict[key] = dict[key].encode('utf-8')
	#xbmc.log(str(dict))
	if 'type' in dict and dict['type'] == 'nextPage':
		dict['name'] = translation(31040)
	if isinstance(dict["name"], unicode):
		dict["name"] = dict["name"].encode('utf-8')
	dict["name"] = cleanString(dict["name"])
	if 'type' in dict and dict['type'] == 'date' and 'time' in dict:
		dict["name"] = '(' + dict["time"] + ') ' + dict["name"]
	#dict["name"] = '(' + dict["time"] + ') ' + dict["name"]
	#dict["name"] = dict["name"].replace('&amp;','&')
	#if hideAudioDisa:
	#	if 'Hörfassung' in dict["name"] or 'Audiodeskription' in dict["name"]:
	#		return False
			
	u = _buildUri(dict)
	ilabels = {
		"Title": cleanString(dict.get('name','')),
		"Plot": cleanString(dict.get('plot','')),
		"Plotoutline": cleanString(dict.get('plot','')),
		"Duration": dict.get('duration',''),
		"Mpaa": dict.get('mpaa','')
		}
	ok=True
	liz=xbmcgui.ListItem(cleanString(dict.get('name','')), iconImage="DefaultFolder.png", thumbnailImage=dict.get('thumb',icon))
	#liz.setInfo( type="Video", infoLabels={ "Title": cleanString(dict.get('name','')) , "Plot": cleanString(dict.get('plot','')) , "Plotoutline": cleanString(dict.get('plot','')) , "Duration": dict.get('duration','') } )
	liz.setInfo( type="Video", infoLabels=ilabels)
	liz.setProperty('fanart_image',dict.get('fanart',dict.get('thumb',fanart)))
	xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content="episodes" )
	if 'type' in dict and (dict['type'] == 'video' or dict['type'] == 'date'):
		liz.setProperty('IsPlayable', 'true')
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
	elif 'type' in dict and dict['type'] == 'nextPage':
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	else:
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		
	return ok
	
def _buildUri(dict):
	u = dict.get('pluginpath',sys.argv[0])+'?'
	i = 0
	for key in dict.keys():
		if i > 0:
			u += '&'
		if isinstance(dict[key], basestring):
			dict[key] = dict[key]#.encode('utf8')
		else:
			dict[key] = str(dict[key])
		u += key + '=' + urllib.quote_plus(dict[key])
		i += 1
	return u
	

def cleanString(s):
  s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#034;", "\"").replace("&#039;", "'").replace("&quot;", "\"").replace("&szlig;", "ß").replace("&ndash;", "-")
  s = s.replace("&Auml;", "Ä").replace("&Uuml;", "Ü").replace("&Ouml;", "Ö").replace("&auml;", "ä").replace("&uuml;", "ü").replace("&ouml;", "ö").replace("&eacute;", "é").replace("&egrave;", "è")
  s = s.replace("&#x00c4;","Ä").replace("&#x00e4;","ä").replace("&#x00d6;","Ö").replace("&#x00f6;","ö").replace("&#x00dc;","Ü").replace("&#x00fc;","ü").replace("&#x00df;","ß")
  s = s.replace("&apos;","'").strip()
  return s

	
def pvrCheckStartTimeIsComparable(a,b):
	n = abs(a-b)
	if n <= 15:
		return True
	else:
		return False
def pvrCheckIfMovie(name):
	if name.startswith("Fernsehfilm Deutschland"):
		return True
	else:
		return False
def pvrCheckDurationIsComparable(a,b,maxDeviation = 10):
	deviation = abs((a * 100) / b - 100)
	if deviation <= maxDeviation:
		return True
	else:
		return False

def pvrCheckNameIsComparable(a,b):
	if a == b:
		return True
	else:
		return _wordRatio(a,b)
	
def _wordRatio(a,b,maxRatio=0.7):
	xbmc.log(a)
	xbmc.log(b)
	i = 0
	aSplit = a.split(" ")
	bSplit = b.split(" ")
	for word in aSplit:
		if word in bSplit:
			i += 1
	ratio = i / len(aSplit) 
	if ratio >= maxRatio:
		return True
	else: return False
	
def get_params():
	param={}
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]= urllib.unquote_plus(splitparams[1])

	return param
	
	

weekdayDict = { '0': translation(31013),#Sonntag
				'1': translation(31014),#Montag
				'2': translation(31015),#Dienstag
				'3': translation(31016),#Mittwoch
				'4': translation(31017),#Donnerstag
				'5': translation(31018),#Freitag
				'6': translation(31019),#Samstag
			  }
	
def populateDirAZ(mode,ignore=[]):
	dict = {}
	dict['mode'] = mode
	if not '#' in ignore:
		dict['name'] = "#"
		dict['type'] = 'dir'
		addEntry(dict)
	letters = [chr(i) for i in xrange(ord('a'), ord('z')+1)]
	for letter in letters:
		if not letter in ignore:
			letter = letter.upper()
			dict['name'] = letter
			addEntry(dict)
	
def populateDirDate(mode,img=False):
	dict = {}
	dict['mode'] = mode
	dict['type'] = 'dir'
	dict['name'] = translation(31020)
	dict['datum']  = '0'
	if img: dict['thumb']  = img[7]
	addEntry(dict)
	dict['name'] = translation(31021)
	dict['datum']  = '1'
	if img: dict['thumb']  = img[8]
	addEntry(dict)
	i = 2
	while i <= 6:
		day = date.today() - timedelta(i)
		dict['name'] = weekdayDict[day.strftime("%w")]
		dict['datum']  = str(i)
		if img: dict['thumb']  = img[int(day.strftime("%w"))]
		addEntry(dict)
		i += 1

def setView(viewMode):
	skin_used = xbmc.getSkinDir()
	if skin_used == 'skin.confluence':
		xbmc.executebuiltin('Container.SetViewMode(500)') # "Thumbnail" view
	elif skin_used == 'skin.aeon.nox':
		xbmc.executebuiltin('Container.SetViewMode(512)') # "Info-wall" view.
	elif skin_used == 'skin.estuary':
		if viewMode == 'video':
			return
		elif viewMode == 'shows':
			xbmc.executebuiltin('Container.SetViewMode(502)') # "Info-wall" view.