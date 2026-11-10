# -*- coding: utf-8 -*-
import re
import libmediathek3 as libMediathek

def grepToken():
	response = libMediathek.getUrl('https://www.zdf.de/live-tv')
	tokenMenu_list = re.compile('\\\\"appToken\\\\":{\\\\"apiToken\\\\":\\\\"(.+?)\\\\"', re.DOTALL).findall(response)
	tokenMenu = tokenMenu_list[0] if tokenMenu_list else '' 
	tokenPlayer_list = re.compile('\\\\"videoToken\\\\":{\\\\"apiToken\\\\":\\\\"(.+?)\\\\"', re.DOTALL).findall(response)
	tokenPlayer = tokenPlayer_list[0] if tokenPlayer_list else ''
	libMediathek.f_mkdir(libMediathek.pathUserdata(''))
	libMediathek.f_write(libMediathek.pathUserdata('tokenMenu'), tokenMenu)
	libMediathek.f_write(libMediathek.pathUserdata('tokenPlayer'), tokenPlayer)
	return (tokenMenu, tokenPlayer)