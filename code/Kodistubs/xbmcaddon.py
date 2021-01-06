# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
Kodi's addon class
"""

__kodistubs__ = True



class Addon(object):
    """
    Kodi's addon class

    Offers classes and functions that manipulate the add-on settings,
    information and localization.

    Creates a new AddOn class.

    :param id: [opt] string - id of the addon as specified in addon.xml

    Specifying the addon id is not needed. Important however is that the addon
    folder has the same name as the AddOn id provided in addon.xml.
    You can optionally specify the addon id from another installed addon
    to retrieve settings from it.

    **id** is optional as it will be auto detected for this add-on instance.

    Example::

        ..
        self.Addon = xbmcaddon.Addon()
        self.Addon = xbmcaddon.Addon('script.foo.bar')
        ..
    """
    
    def __init__(self, id=None):
        # type: (str) -> None
        pass
    
    def getLocalizedString(self, id):
        # type: (int) -> unicode
        """
        Returns an addon's localized 'unicode string'. 

        :param id: integer - id# for string you want to localize. 
        :return: Localized 'unicode string'

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            ..
            locstr = self.Addon.getLocalizedString(32000)
            ..
        """
        return u""
    
    def getSetting(self, id):
        # type: (str) -> str
        """
        Returns the value of a setting as a unicode string. 

        :param id: string - id of the setting that the module needs to access. 
        :return: Setting as a unicode string

        **id** is optional as it will be auto detected for this add-on instance.

        Example::

            ..
            apikey = self.Addon.getSetting('apikey')
            ..
        """
        return ""
    
    def setSetting(self, id, value):
        # type: (str, str_type) -> None
        """
        Sets a script setting. 

        :param id: string - id of the setting that the module needs to access. 
        :param value: string or unicode - value of the setting.

        You can use the above as keywords for arguments.

        Example::

            ..
            self.Addon.setSetting(id='username', value='teamkodi')
            ..
        """
        pass
    
    def openSettings(self):
        # type: () -> None
        """
        Opens this scripts settings dialog. 

        Example::

            ..
            self.Addon.openSettings()
            ..
        """
        pass
    
    def getAddonInfo(self, id):
        # type: (str) -> str
        """
        Returns the value of an addon property as a string. 

        :param id: string - id of the property that the module needs to access.

        Choices for the property are:

        =======  ==========  ============  ===========
        author   changelog   description   disclaimer 
        fanart   icon        id            name       
        path     profile     stars         summary    
        type     version                              
        =======  ==========  ============  ===========

        :return: AddOn property as a string

        Example::

            ..
            version = self.Addon.getAddonInfo('version')
            ..
        """
        return ""
