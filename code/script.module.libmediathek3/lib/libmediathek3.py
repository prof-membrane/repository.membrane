# -*- coding: utf-8 -*-
import os
import sys
import string
import xbmc
import xbmcvfs
import xbmcgui
import xbmcplugin
from datetime import datetime

import libmediathek3debug
from libmediathek3utils import *
from libmediathek3listing import *
from libmediathek3ttml2srt import *
from libmediathek3premadedirs import *
from libmediathek3dialogs import *
from libmediathek3webvtt2srt import *

"""
prefererdLang = ['de','en','fr']
prefererdSub = ['de','en','fr']
subtitleenabled = False
subtitleenabled = True
"""

def _chooseBitrate(l, force_MP4 = False):
	bitrate = -1
	listitem = None
	url = None
	streamType = None
	for item in l:
		if not force_MP4 and item.get('stream','').lower() == 'hls':#prefer hls
			url = item['url']
			streamType = 'HLS'
			break
		if item.get('stream','').lower() == 'mp4' and item.get('bitrate',0) > bitrate:
			bitrate = item.get('bitrate',0)
			url = item['url']
			streamType = 'MP4'
		if not force_MP4 and item.get('stream','').lower() == 'dash':
			url = item['url']
			streamType = 'DASH'
		if not force_MP4 and item.get('stream','').lower() == 'audio':
			url = item['url']
			streamType = 'AUDIO'
	listitem = xbmcgui.ListItem(path=url)
	if streamType == 'DASH':
		listitem.setProperty('inputstream', 'inputstream.adaptive')
		listitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
		listitem.setProperty('inputstream.adaptive.manifest_type', 'mpd')
		#listitem.setProperty('inputstream.adaptive.stream_headers','User-Agent=Mozilla%2F5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F63.0.3239.84%20Safari%2F537.36')
		listitem.setMimeType('application/dash+xml')
		listitem.setContentLookup(False)
	elif streamType == 'HLS':
		listitem.setMimeType('application/vnd.apple.mpegurl')
		listitem.setProperty('inputstream', 'inputstream.adaptive')
		listitem.setProperty('inputstreamaddon', 'inputstream.adaptive')
		listitem.setProperty('inputstream.adaptive.manifest_type', 'hls')
		listitem.setContentLookup(False)
	#elif streamType == 'MP4':
	#	listitem.setMimeType('application/dash+xml')
	#	listitem.setContentLookup(False)

	return listitem,url


def play(d,external=None,download_dir=None):
	"""
	if 'lang' in d['media'][0]:
		url = _chooseBitrate(d['media'])
		#""
		languageFound = False
		l = []
		lsubtitles = []
		for lang in prefererdLang:
			for item in d['media']:
				if lang == item['lang']:
					if 'subtitlelang' in item:
						lsubtitles.append(item)
					else:
						l.append(item)
					languageFound = True
			if languageFound:
				log('###############')
				if subtitleenabled and len(lsubtitles) > 0:
					url = _chooseBitrate(lsubtitles)
				elif len(l) == 0 and len(lsubtitles) > 0:
					url = _chooseBitrate(lsubtitles)
				elif lang != prefererdLang and len(lsubtitles) > 0:
					url = _chooseBitrate(lsubtitles)
				else:
					url = _chooseBitrate(l)
				break
		#""
		if not languageFound:
			url = _chooseBitrate(d['media'])
	else:
		url = _chooseBitrate(d['media'])
	"""

	#listitem = xbmcgui.ListItem(path=url)
	listitem,url = _chooseBitrate(d['media'], force_MP4 = bool(download_dir))

	i = 0
	if 'subtitle' in d:
		subs = []
		for subtitle in d['subtitle']:
			if subtitle['type'] == 'srt':
				subs.append(subtitle['url'])
			elif subtitle['type'] == 'ttml':
				subFile = ttml2Srt(subtitle['url'])
				subs.append(subFile)
			elif subtitle['type'] == 'webvtt':
				subFile = webvtt2Srt(subtitle['url'])
				subs.append(subFile)
			else:
				log('Subtitle format not supported: ' + subtitle['type'])
		listitem.setSubtitles(subs)

	if 'metadata' in d:
		ilabels = {}
		if 'plot' in d['metadata']:
			ilabels['Plot'] = d['metadata']['plot']
		if 'name' in d['metadata']:
			ilabels['Title'] = d['metadata']['name']
		listitem.setInfo( type="Video", infoLabels=ilabels)

		art = {}
		if 'thumb' in d['metadata']:
			art['thumb'] = d['metadata']['thumb']
		listitem.setArt(art)

	if 'header' in d['media']:
		#listitem.setProperty('media_headers',d['media']['header'])
		#listitem.setProperty('inputstream.adaptive.media_headers',d['media']['header'])
		listitem.setProperty('inputstream.adaptive.stream_headers',d['media']['header'])

	if download_dir:
		filename = datetime.today().strftime('%Y-%m-%d-%H%M%S.mp4')
		title = d.get('metadata',filename).get('name',filename)
		addon_icon = os.path.join(addon.getAddonInfo('path'), 'icon.png')
		if url:
			if title != filename:
				filename = title + ' - ' + filename
				valid_chars = frozenset('-_.() %s%s' % (string.ascii_letters, string.digits))
				filename = ''.join(c for c in filename if c in valid_chars)
			filename = 'DL - ' + filename
			tuple = (addon.getAddonInfo('name'), addon_icon, title, os.path.abspath(os.path.join(download_dir, filename)), url)
			arg = None
			for item in tuple:
				if sys.version_info[0] < 3:
					item = item.decode('utf-8')
				if arg is None: arg = item
				else: 			arg = arg + '\0' + item
			if sys.version_info[0] < 3: # for Python 2
				base64str = arg.encode('utf-8').encode('base64').strip()
				path = os.path.join(xbmc.translatePath('special://home'), 'addons', libmediathek3_addonid, 'lib', 'download.py')
			else: # for Python 3
				import base64
				base64str = base64.b64encode(arg.encode('utf-8')).decode('ascii').strip()
				path = os.path.join(xbmcvfs.translatePath('special://home'), 'addons', libmediathek3_addonid, 'lib', 'download.py')
			xbmc.executebuiltin('RunScript(%s, %s)' % (path, base64str))
		else:
			xbmcgui.Dialog().notification(getTranslation(31044), title, addon_icon)
	elif external:
		xbmc.Player().play(url, listitem)
	else:
		pluginhandle = int(sys.argv[1])
		xbmcplugin.setResolvedUrl(pluginhandle, True, listitem)
		if ('metadata' in d) and (d['metadata'].get('live', None) == 'true'):
			from threading import Thread
			bg_thread = Thread (target = ShowSeekPos, args = (xbmc.Player(), url))
			bg_thread.start()


def ShowSeekPos(player, url):
	monitor = xbmc.Monitor()
	icon = ""									# -> Kodi's i-Symbol
	now = time.mktime(datetime.now().timetuple())	# Unix-Format 1489094334.0
	now_dt = datetime.fromtimestamp(int(now))
	StartTime = now_dt.strftime("%H:%M:%S")

	# Maximal 10 Sekunden bis sich der Player initialisiert hat (Raspi, empirisch)
	i = 0
	TotalTime = 0
	while not monitor.waitForAbort(1) and i < 10:
		xbmc.sleep(100)
		if player.isPlaying():
			TotalTime = int(player.getTotalTime())	# sec, float -> int, max. Puffergröße
			if TotalTime:
				break
		i += 1

	if not TotalTime:
		return

	LastSeek = int(player.getTime())			# Basis-Wert für akt. Uhrzeit
	LastBufTime = now_dt						# für sync errors

	while not monitor.waitForAbort(1):
		xbmc.sleep(100)
		if player.isPlaying():
			try:
				play_time = player.getTime()	# akt. Pos im Puffer (0=Pufferstart)
			except:
				play_time = LastSeek

			p = int(play_time)

			# regelm. Schwankung bei Livestreams 6-10 (empirisch):
			if abs(LastSeek-p) > 10:			# rückwärts/vorwärts im Puffer
				pos_sec = TotalTime - p			# je kleiner p desto größer der Zeitabzug
				now = time.mktime(datetime.now().timetuple()) # Unix-Format 1489094334.0
				time_sec = int(now) - pos_sec	# Pos-Sekunden von akt. Zeit abziehen
				new_dt = datetime.fromtimestamp(time_sec)
				t_string = new_dt.strftime("%H:%M:%S")

				if LastBufTime != new_dt:		# skip_sync_error
					LastBufTime = new_dt
					xbmcgui.Dialog().notification(t_string, "Livestream-Position", icon, 5000, sound = False)

			LastSeek = max(0,min(p,TotalTime))

		else:
			break

	return
