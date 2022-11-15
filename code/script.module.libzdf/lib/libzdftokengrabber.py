# -*- coding: utf-8 -*-
import re
import libmediathek3 as libMediathek

def grepToken():
	response = libMediathek.getUrl('https://www.zdf.de/live-tv')
	tokenMenu = re.compile("apiToken: '(.+?)'", re.DOTALL).findall(response)[0]
	tokenPlayer = re.compile('"apiToken": "(.+?)"', re.DOTALL).findall(response)[0]
	
	libMediathek.f_mkdir(libMediathek.pathUserdata(''))
	libMediathek.f_write(libMediathek.pathUserdata('tokenMenu'), tokenMenu)
	libMediathek.f_write(libMediathek.pathUserdata('tokenPlayer'), tokenPlayer)
	return (tokenMenu, tokenPlayer)