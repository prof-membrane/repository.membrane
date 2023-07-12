# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime, timedelta
import xbmc
import xbmcvfs
import xbmcgui
import xbmcplugin
import xbmcaddon
import libmediathek3

from libmediathek3utils import clearString
from libmediathek3utils import getSetting
from libmediathek3utils import getTranslation as translation


if sys.version_info[0] < 3: # for Python 2
	from urllib import quote_plus, unquote_plus
	icon = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('icon'))
	fanart = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('fanart'))
else: # for Python 3
	from urllib.parse import quote_plus, unquote_plus
	icon = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('icon'))
	fanart = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('fanart'))

handle = int(sys.argv[1])


def sortAZ():
	xbmcplugin.addSortMethod(handle, xbmcplugin.SORT_METHOD_LABEL)

def addEntries(l):
	lists = []
	doneList = []

	download_dir = getSetting('download_dir')

	for d in l:
		if str(d) in doneList:#primitive methode to filter duplicated entries
			continue
		doneList.append(str(d))

		if '_overridepath' in d:
			u = d['_overridepath']
		else:
			u = _buildUri(d)
		newd = {}
		for key in d:
			if sys.version_info[0] < 3: # for Python 2
				if isinstance(d[key], unicode):
					d[key] = d[key].encode('utf-8', 'ignore')
			if key.startswith('_'):
				newd[key[1:]] = d[key]
			else:
				newd[key] = d[key]
		d = newd

		if 'type' in d and d['type'] == 'nextPage':
			d['name'] = translation(31040)
			if not 'mode' in d:
				d['mode'] = get_params()['mode']
		if sys.version_info[0] < 3: # for Python 2
			if isinstance(d['name'], unicode):
				d['name'] = d['name'].encode('utf-8')
		d['name'] = clearString(d['name'])
		if 'airedISO8601' in d:
			d['aired'],d['airedtime'] = _airedISO8601(d)

		if d.get('type',None) == 'date' and d.get('airedtime',None):
			d['name'] = '[COLOR orange]' + str(d['airedtime']) + '[/COLOR]  ' + d['name']

		ilabels = {
			'Title': clearString(d.get('name','')),
			'Plot': clearString(d.get('plot','')),
			'Plotoutline': clearString(d.get('plot','')),
			'Duration': d.get('duration',''),
			'Mpaa': d.get('mpaa',''),
			'Aired': d.get('aired',''),
			'Studio': d.get('channel',''),
			}
		if 'epoch' in d:
			ilabels['aired'] = time.strftime('%Y-%m-%d', time.gmtime(float(d['epoch'])))
		if 'episode' in d:
			ilabels['Episode'] = d['episode']
		if 'Season' in d:
			ilabels['Season'] = d['season']
		if 'tvshowtitle' in d:
			ilabels['tvshowtitle'] = d['tvshowtitle']
			ilabels['tagline'] = d['tvshowtitle']
			ilabels['album'] = d['tvshowtitle']
		if 'rating' in d:
			ilabels['rating'] = d['rating']
		if 'type' in d and d['type'] != 'nextPage':
			if d['type'] == 'video' or d['type'] == 'live' or d['type'] == 'date' or d['type'] == 'clip':
				ilabels['mediatype'] = 'video'
			elif d['type'] == 'shows' or d['type'] == 'season':
				ilabels['mediatype'] = 'season'
			elif d['type'] == 'episode':
				ilabels['mediatype'] = 'episode'
			elif d['type'] != 'dir':
				ilabels['mediatype'] = 'video'

		ok=True
		liz=xbmcgui.ListItem(clearString(d.get('name','')))
		if d.get('type',None) == 'audio':
			liz.setInfo( type='music', infoLabels=ilabels)
		else:
			liz.setInfo( type='video', infoLabels=ilabels)
		liz.addStreamInfo('subtitle', {'language': 'deu'})
		art = {}
		art['thumb'] = d.get('thumb')
		art['landscape'] = d.get('thumb')
		art['poster'] = d.get('thumb')
		art['fanart'] = d.get('fanart',d.get('thumb',fanart))
		art['icon'] = d.get('channelLogo','')
		liz.setArt(art)

		if 'customprops' in d:
			for prop in d['customprops']:
				liz.setProperty(prop, d['customprops'][prop])

		if d.get('type',None) == 'video' or d.get('type',None) == 'live' or d.get('type',None) == 'date' or d.get('type',None) == 'clip' or d.get('type',None) == 'episode' or d.get('type',None) == 'audio':
			#xbmcplugin.setContent( handle=int( sys.argv[ 1 ] ), content='episodes' )
			liz.setProperty('IsPlayable', 'true')
			if d.get('type',None) == 'live':
				liz.setProperty('starttime','1')
				liz.setProperty('totaltime','1')
			if download_dir and d.get('type',None) in ('video','date'):
				liz.addContextMenuItems([('Download', 'RunPlugin(%s&download_dir=%s)' % (u,quote_plus(download_dir)))])
			lists.append([u,liz,False])
		else:
			lists.append([u,liz,True])

	xbmcplugin.addDirectoryItems(handle, lists)
	xbmcplugin.setContent(handle, content='videos')

def endOfDirectory():
	xbmcplugin.endOfDirectory(handle,cacheToDisc=True)

def _buildUri(d):
	u = d.get('pluginpath',sys.argv[0])+'?'
	i = 0
	for key in d.keys():
		if not key.startswith('_'):
			value = d[key]
			if value:
				if sys.version_info[0] < 3: # for Python 2
					if isinstance(value, unicode):
						value = value.encode('utf-8')
				if i > 0:
					u = u + '&'
				u = u + key + '=' + quote_plus(value)
				i += 1
	return u

def _airedISO8601(d):
	iso = d['airedISO8601']
	tempdate = str_to_airedtime(iso)
	if tempdate:
		return tempdate.strftime('%Y-%m-%d'), tempdate.strftime('%H:%M')
	else:
		return '', ''

def str_to_airedtime(airedtime_str):
	airedtime = None
	if airedtime_str:
		start = airedtime_str.split('+')
		zulutime = 1 if (len(start) == 1) else 0
		formats = [('%Y-%m-%dT%H:%M:%S','%Y-%m-%dT%H:%M:%SZ'),('%Y-%m-%dT%H:%M:%S.%f','%Y-%m-%dT%H:%M:%S.%fZ')]
		for format in formats:
			try:
				airedtime = datetime.strptime(start[0], format[zulutime])
				break
			except TypeError:
				try: # Workaround for known bug in Python Interpreter
					airedtime = datetime(*(time.strptime(start[0], format[zulutime])[0:6]))
					break
				except ValueError:
					pass
			except ValueError:
				pass
		if airedtime and zulutime:
			tz_offset = timedelta (minutes = (time.timezone / -60) + (time.localtime().tm_isdst * 60))
			airedtime += tz_offset
	return airedtime

def getMetadata(result):
	if result:
		metadata = {}
		params = get_params()
		for key in ('name', 'plot', 'thumb', 'live'):
			value = params.get(key, None)
			if value:
				metadata[key] = value
		if metadata:
			result['metadata'] = metadata
	return result

def list(modes, defaultMode, *playModes):
	if playModes: # must contain at least one item
		params = get_params()
		mode = params.get('mode', defaultMode)
		fn = modes.get(mode, None)
		if fn:
			if isinstance(fn, tuple):
				res = fn[0]()
			else:
				res = fn()
			if mode in playModes:
				if res is None:
					dialog = xbmcgui.Dialog()
					title = xbmcaddon.Addon().getAddonInfo('name')
					text = translation(31043)
					dialog.ok(title, text)
					return None
				else:
					libmediathek3.play(res,download_dir=params.get('download_dir',None))
			else:
				if not (res is None):
					addEntries(res)
					if isinstance(fn, tuple):
						xbmcplugin.setContent(handle, content=fn[1])
					endOfDirectory()
			return True # OK
	raise NotImplementedError()


params = None

def get_params():
	global params
	if params is None:
		params = {}
		paramstring = sys.argv[2]
		if len(paramstring) >= 2:
			if paramstring[len(paramstring)-1] == '/':
				paramstring = paramstring[:-1]
			cleanedparams = paramstring.replace('?','')
			pairsofparams = cleanedparams.split('&')
			for keyvalue in pairsofparams:
				splitted = keyvalue.split('=')
				if len(splitted) == 2:
					params[splitted[0]] = unquote_plus(splitted[1])
	return params