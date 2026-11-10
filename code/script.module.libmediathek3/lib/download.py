import xbmc
import xbmcgui
import sys

base64str = sys.argv[1]

if sys.version_info[0] >= 3: # for Python 3
	from urllib.request import urlretrieve
	import base64
	args = base64.b64decode(base64str.encode('ascii')).decode('utf-8')
else:
	from urllib import urlretrieve
	args = base64str.decode('base64').decode('utf-8')

addon_name, addon_icon, title, filename, video_url = args.split('\0')

def reporthook(block_number, block_size, total_size):
	if total_size - block_size <= block_number * block_size < total_size:
		xbmcgui.Dialog().notification('End download', title, addon_icon)

xbmcgui.Dialog().notification('Start download', title, addon_icon)
try:
	urlretrieve(video_url, filename, reporthook)
except Exception as e:
	heading = 'Failed download'
	errormsg = type(e).__name__ + ' ' + str(e)
	xbmc.log(heading + ' "' + title + '": ' + errormsg, xbmc.LOGERROR)
	xbmcgui.Dialog().notification(heading, title + ': '  + errormsg, addon_icon)
