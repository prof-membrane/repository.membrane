import urllib
import urllib2
import socket
import xbmc
import xbmcaddon
import xbmcvfs
import re
from datetime import date, timedelta

from libmediathek3utils import getTranslation as getTranslation


def populateDirAZ(mode,ignore=[]):
	l = []
	if not '#' in ignore:
		d = {}
		d['mode'] = mode
		d['name'] = "#"
		d['_type'] = 'dir'
		l.append(d)
	letters = [chr(i) for i in xrange(ord('a'), ord('z')+1)]
	for letter in letters:
		if not letter in ignore:
			d = {}
			d['mode'] = mode
			letter = letter.upper()
			d['name'] = letter
			d['_type'] = 'dir'
			l.append(d)
	return l
	
def labelDirDate(day,relative_weekday=None):
	format_string = '{day_of_month:02d}. {month_shortstr} | {day_of_week}'
	return (
		format_string.format(
			day_of_month = day.day, 
			month_shortstr = xbmc.getLocalizedString(50+day.month), 
			day_of_week = 
				xbmc.getLocalizedString(relative_weekday) if relative_weekday else xbmc.getLocalizedString(11+day.weekday()) 
		)
	)	
	
def populateDirDate(mode,channel=False,dateChooser=False):
	l = []
	
	d = {}
	day = date.today()
	d['mode'] = mode
	d['_type'] = 'dir'
	if channel: d['channel'] = channel
	d['_name'] = labelDirDate(day, 33006)
	d['datum'] = '0'
	d['yyyymmdd'] = day.strftime('%Y-%m-%d')
	l.append(d)
	
	i = 1
	while i <= 6:
		d = {}
		day = day - timedelta(1)
		d['_name'] = labelDirDate(day)
		d['datum']  = str(i)
		d['mode'] = mode
		d['_type'] = 'dir'
		if channel: d['channel'] = channel
		d['yyyymmdd'] = day.strftime('%Y-%m-%d')
		l.append(d)
		i += 1
		
	return l
	
