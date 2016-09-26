import urllib
import urllib2
import socket
import xbmc
import xbmcaddon
import xbmcvfs
import re
temp = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'temp').decode('utf-8')
dict = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')+'dict.py').decode('utf-8')

def getUrl(url):
    xbmc.log(url)
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:25.0) Gecko/20100101 Firefox/25.0')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    return link
	
		
	
def f_open(path):
	f = xbmcvfs.File(path)
	result = f.read()
	f.close()
	return result

def f_write(path,data):
	print 'writing to '+path
	f = xbmcvfs.File(path, 'w')
	result = f.write(data)
	f.close()
	return True
	
def f_mkdir(path):
	return xbmcvfs.mkdir(path)