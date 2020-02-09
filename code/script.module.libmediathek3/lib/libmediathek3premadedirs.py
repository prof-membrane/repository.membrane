# -*- coding: utf-8 -*-
import sys
import xbmc
from datetime import date, timedelta

def populateDirAZ(mode,ignore=[],channel=None):
	l = []
	if not '#' in ignore:
		d = {}
		d['mode'] = mode
		d['name'] = "#"
		d['_type'] = 'dir'
		if channel:
			d['channel'] = channel
		l.append(d)
	if sys.version_info[0] < 3: # for Python 2
		r = xrange(ord('a'), ord('z')+1)
	else: # for Python 3
		r = range(ord('a'), ord('z')+1)
	letters = [chr(i) for i in r]
	for letter in letters:
		if not letter in ignore:
			d = {}
			d['mode'] = mode
			letter = letter.upper()
			d['name'] = letter
			d['_type'] = 'dir'
			if channel:
				d['channel'] = channel
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

