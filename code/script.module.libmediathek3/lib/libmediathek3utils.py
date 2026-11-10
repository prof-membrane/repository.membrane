# -*- coding: utf-8 -*-
import sys
import socket
import gzip
import pickle
import xbmc
import xbmcplugin
import xbmcaddon
import xbmcvfs

addon = xbmcaddon.Addon()

socket.setdefaulttimeout(30)

if sys.version_info[0] < 3: # for Python 2
	libmediathek3_addonid = 'script.module.libmediathek3'
	from StringIO import StringIO
	from cookielib import CookieJar
	from urllib2 import Request, urlopen, build_opener, HTTPCookieProcessor
	from urllib import quote_plus
	from xbmc import validatePath 
else: # for Python 3
	libmediathek3_addonid = 'script.module.libmediathek3.matrix'
	from io import BytesIO
	from http.cookiejar import CookieJar
	from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor
	from urllib.parse import quote_plus
	from xbmcvfs import validatePath


def log(msg):
	xbmc.log(msg)

def getTranslation(id,addonid=libmediathek3_addonid):
	return xbmcaddon.Addon(id=addonid).getLocalizedString(id)

def getUrl(url,headers=False,post=False,cookies=False):
	log(url)
	return _request(url,headers,post,cookies)
	try:
		return _request(url,headers,post,cookies)
	except:#fast retry hack
		return _request(url,headers,post,cookies)
def _request(url,headers,post,cookies):
	log(url)
	url = quote_plus(url,safe='%/:?=&')
	if post:
		if sys.version_info[0] >= 3: # for Python 3
			post = post.encode('utf-8')
		req = Request(url,post)
		log('########POST!')
	else:
		req = Request(url)
	if headers:
		for key in headers:
			req.add_header(key, headers[key])
		#req.add_header('Content-Type','application/json')
		req.has_header = lambda header_name: (True if header_name == 'Content-Length' else Request.has_header(req, header_name))
	else:
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0')
		req.add_header('Accept-Encoding','gzip, deflate')

	if cookies:
		cj = CookieJar()
		log(pathUserdata(''))
		log(pathUserdata('cookies.txt'))
		if not f_exists(pathUserdata('')):
			f_mkdir(pathUserdata(''))
		if f_exists(pathUserdata('cookies.txt')):
			cookies_txt = f_open(pathUserdata('cookies.txt'))
			if cookies_txt:
				if sys.version_info[0] >= 3: # for Python 3
					if isinstance(cookies_txt, str):
						cookies_txt = cookies_txt.encode('utf-8')
				c = pickle.loads(cookies_txt)
				for cookie in c:
					cj.set_cookie(cookie)
		opener = build_opener(HTTPCookieProcessor(cj))
		response = opener.open(req)

		c = []
		for cookie in cj:
			log(str(cookie))
			c.append(cookie)
		log(str(cj))

		f_write(pathUserdata('cookies.txt'),pickle.dumps(c))
		#cj.save(cookiefile)
	else:
		response = urlopen(req)

	compressed = response.info().get('Content-Encoding') == 'gzip'
	link = response.read()
	response.close()
	if compressed:
		if sys.version_info[0] < 3:
			buf = StringIO(link)
		else:
			buf = BytesIO(link)
		f = gzip.GzipFile(fileobj=buf)
		link = f.read()
	if sys.version_info[0] >= 3: # for Python 3
 	 	link = link.decode('utf-8')
	return link


def clearString(s):
	if s:
		s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").replace("&#034;", "\"").replace("&#039;", "'").replace("&quot;", "\"").replace("&szlig;", "ß").replace("&ndash;", "-")
		s = s.replace("&Auml;", "Ä").replace("&Uuml;", "Ü").replace("&Ouml;", "Ö").replace("&auml;", "ä").replace("&uuml;", "ü").replace("&ouml;", "ö").replace("&eacute;", "é").replace("&egrave;", "è")
		s = s.replace("&#x00c4;","Ä").replace("&#x00e4;","ä").replace("&#x00d6;","Ö").replace("&#x00f6;","ö").replace("&#x00dc;","Ü").replace("&#x00fc;","ü").replace("&#x00df;","ß")
		#ISO-8859-1?!?!?! oh how i hate the friggin encoding
		s = s.replace("&apos;","'")
		s = s.replace("&#43;","\"")
		s = s.strip()
	return s

def pathUserdata(path):
	special = addon.getAddonInfo('profile')+path
	special = special.replace('//','/').replace('special:/','special://')
	return special

def pathAddon(path):
	special = validatePath(addon.getAddonInfo('path').replace('\\','/')+path.replace('\\','/'))
	special = special.replace('//','/').replace('special:/','special://')
	return special

def f_open(path):
	try:
		f = xbmcvfs.File(path)
		result = f.read()
	except: pass
	finally:
		f.close()
	return result

def f_write(path,data):
	try:
		#f_mkdir(path)
		f = xbmcvfs.File(path, 'w')
		result = f.write(data)
	except: pass
	finally:
		f.close()
	return True

def f_remove(path):
	return xbmcvfs.delete(path)

def f_exists(path):
	exists = xbmcvfs.exists(path)
	if exists == 0:
		return False
	elif exists == False:
		return False
	else:
		return True

def f_mkdir(path):
	return xbmcvfs.mkdir(path)

def searchWorkaroundWrite(searchword):
	f_write(pathUserdata('/search.lock'),searchword)
def searchWorkaroundRead():
	return f_open(pathUserdata('/search.lock'))
def searchWorkaroundExists():
	return f_exists(pathUserdata('/search.lock'))
def searchWorkaroundRemove():
	log('###Krypton workaround: removing lock...')
	f_remove(pathUserdata('/search.lock'))

def setSetting(id, value):
	addon.setSetting(id,value)

def getSetting(id):
	return addon.getSetting(id)

def setSettingBool(id, value):
	addon.setSetting(id, 'true' if bool(value) else 'false')

def getSettingBool(id):
	return (addon.getSetting(id) == 'true')
