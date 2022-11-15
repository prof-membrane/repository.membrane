# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcvfs
import xbmcaddon
import libmediathek3utils as utils


if sys.version_info[0] < 3: # for Python 2
	subFile = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'/webvtt.srt').decode('utf-8')
else:
	subFile = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'/webvtt.srt')

bracketLookup = {
	'<c.textWhite>':	'<font color="#ffffff">',
	'<c.textYellow>':	'<font color="#ffff00">',
	'<c.textCyan>':		'<font color="#00ffff">',
	'<c.textRed>':		'<font color="#ff0000">',
	'<c.textGreen>':	'<font color="#00ff00">',
	'<c.textBlue>':		'<font color="#0000ff">',
	'<c.textMagenta>':	'<font color="#ff00ff">',
	'<c.textMagenta>':	'<font color="#ff00ff">',
	'</c>':				'</font>',
}
def webvtt2Srt(url):
	if xbmcvfs.exists(subFile):
		xbmcvfs.delete(subFile)
	
	webvtt = utils.getUrl(url)
	s = webvtt.split('\n\n')
	i = 1
	srt = ''
	while i < len(s):
		j = 0
		for line in s[i].split('\n'):
			if j == 0:
				srt += line + '\n'
			elif j == 1:
				t = line.split(' ')
				srt += t[0][:-1].replace('.',',') + ' --> ' + t[2][:-1].replace('.',',') + '\n'
			else:
				for bracket in bracketLookup:
					line = line.replace(bracket,bracketLookup[bracket])
				srt += line + '\n'
			j += 1
		srt += '\n'
		i += 1
	
	f = xbmcvfs.File(subFile, 'w')
	f.write(srt)
	f.close()
	return subFile