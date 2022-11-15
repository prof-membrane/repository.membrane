# coding: utf-8
# This file is generated from Kodi source code and post-edited
# to correct code style and docstrings formatting.
# License: GPL v.3 <https://www.gnu.org/licenses/gpl-3.0.en.html>
"""
GUI functions on Kodi

Offers classes and functions that manipulate the
Graphical User Interface through windows, dialogs, and various control widgets.
"""
import sys
from xbmc import InfoTagVideo, InfoTagMusic

__kodistubs__ = True


INT_MAX = sys.maxsize
ACTION_ANALOG_FORWARD = 113
ACTION_ANALOG_MOVE = 49
ACTION_ANALOG_MOVE_X_LEFT = 601
ACTION_ANALOG_MOVE_X_RIGHT = 602
ACTION_ANALOG_MOVE_Y_DOWN = 604
ACTION_ANALOG_MOVE_Y_UP = 603
ACTION_ANALOG_REWIND = 114
ACTION_ANALOG_SEEK_BACK = 125
ACTION_ANALOG_SEEK_FORWARD = 124
ACTION_ASPECT_RATIO = 19
ACTION_AUDIO_DELAY = 161
ACTION_AUDIO_DELAY_MIN = 54
ACTION_AUDIO_DELAY_PLUS = 55
ACTION_AUDIO_NEXT_LANGUAGE = 56
ACTION_BACKSPACE = 110
ACTION_BIG_STEP_BACK = 23
ACTION_BIG_STEP_FORWARD = 22
ACTION_BROWSE_SUBTITLE = 247
ACTION_BUILT_IN_FUNCTION = 122
ACTION_CALIBRATE_RESET = 48
ACTION_CALIBRATE_SWAP_ARROWS = 47
ACTION_CHANGE_RESOLUTION = 57
ACTION_CHANNEL_DOWN = 185
ACTION_CHANNEL_NUMBER_SEP = 192
ACTION_CHANNEL_SWITCH = 183
ACTION_CHANNEL_UP = 184
ACTION_CHAPTER_OR_BIG_STEP_BACK = 98
ACTION_CHAPTER_OR_BIG_STEP_FORWARD = 97
ACTION_CONTEXT_MENU = 117
ACTION_COPY_ITEM = 81
ACTION_CREATE_BOOKMARK = 96
ACTION_CREATE_EPISODE_BOOKMARK = 95
ACTION_CURSOR_LEFT = 120
ACTION_CURSOR_RIGHT = 121
ACTION_CYCLE_SUBTITLE = 99
ACTION_DECREASE_PAR = 220
ACTION_DECREASE_RATING = 137
ACTION_DELETE_ITEM = 80
ACTION_ENTER = 135
ACTION_ERROR = 998
ACTION_FILTER = 233
ACTION_FILTER_CLEAR = 150
ACTION_FILTER_SMS2 = 151
ACTION_FILTER_SMS3 = 152
ACTION_FILTER_SMS4 = 153
ACTION_FILTER_SMS5 = 154
ACTION_FILTER_SMS6 = 155
ACTION_FILTER_SMS7 = 156
ACTION_FILTER_SMS8 = 157
ACTION_FILTER_SMS9 = 158
ACTION_FIRST_PAGE = 159
ACTION_FORWARD = 16
ACTION_GESTURE_ABORT = 505
ACTION_GESTURE_BEGIN = 501
ACTION_GESTURE_END = 599
ACTION_GESTURE_NOTIFY = 500
ACTION_GESTURE_PAN = 504
ACTION_GESTURE_ROTATE = 503
ACTION_GESTURE_SWIPE_DOWN = 541
ACTION_GESTURE_SWIPE_DOWN_TEN = 550
ACTION_GESTURE_SWIPE_LEFT = 511
ACTION_GESTURE_SWIPE_LEFT_TEN = 520
ACTION_GESTURE_SWIPE_RIGHT = 521
ACTION_GESTURE_SWIPE_RIGHT_TEN = 530
ACTION_GESTURE_SWIPE_UP = 531
ACTION_GESTURE_SWIPE_UP_TEN = 540
ACTION_GESTURE_ZOOM = 502
ACTION_GUIPROFILE_BEGIN = 204
ACTION_HIGHLIGHT_ITEM = 8
ACTION_INCREASE_PAR = 219
ACTION_INCREASE_RATING = 136
ACTION_INPUT_TEXT = 244
ACTION_JUMP_SMS2 = 142
ACTION_JUMP_SMS3 = 143
ACTION_JUMP_SMS4 = 144
ACTION_JUMP_SMS5 = 145
ACTION_JUMP_SMS6 = 146
ACTION_JUMP_SMS7 = 147
ACTION_JUMP_SMS8 = 148
ACTION_JUMP_SMS9 = 149
ACTION_LAST_PAGE = 160
ACTION_MENU = 163
ACTION_MOUSE_DOUBLE_CLICK = 103
ACTION_MOUSE_DRAG = 106
ACTION_MOUSE_END = 109
ACTION_MOUSE_LEFT_CLICK = 100
ACTION_MOUSE_LONG_CLICK = 108
ACTION_MOUSE_MIDDLE_CLICK = 102
ACTION_MOUSE_MOVE = 107
ACTION_MOUSE_RIGHT_CLICK = 101
ACTION_MOUSE_START = 100
ACTION_MOUSE_WHEEL_DOWN = 105
ACTION_MOUSE_WHEEL_UP = 104
ACTION_MOVE_DOWN = 4
ACTION_MOVE_ITEM = 82
ACTION_MOVE_ITEM_DOWN = 116
ACTION_MOVE_ITEM_UP = 115
ACTION_MOVE_LEFT = 1
ACTION_MOVE_RIGHT = 2
ACTION_MOVE_UP = 3
ACTION_MUTE = 91
ACTION_NAV_BACK = 92
ACTION_NEXT_CHANNELGROUP = 186
ACTION_NEXT_CONTROL = 181
ACTION_NEXT_ITEM = 14
ACTION_NEXT_LETTER = 140
ACTION_NEXT_PICTURE = 28
ACTION_NEXT_SCENE = 138
ACTION_NEXT_SUBTITLE = 26
ACTION_NONE = 0
ACTION_NOOP = 999
ACTION_PAGE_DOWN = 6
ACTION_PAGE_UP = 5
ACTION_PARENT_DIR = 9
ACTION_PASTE = 180
ACTION_PAUSE = 12
ACTION_PLAYER_DEBUG = 27
ACTION_PLAYER_FORWARD = 77
ACTION_PLAYER_PLAY = 79
ACTION_PLAYER_PLAYPAUSE = 229
ACTION_PLAYER_PROCESS_INFO = 69
ACTION_PLAYER_PROGRAM_SELECT = 70
ACTION_PLAYER_RESET = 248
ACTION_PLAYER_REWIND = 78
ACTION_PREVIOUS_CHANNELGROUP = 187
ACTION_PREVIOUS_MENU = 10
ACTION_PREV_CONTROL = 182
ACTION_PREV_ITEM = 15
ACTION_PREV_LETTER = 141
ACTION_PREV_PICTURE = 29
ACTION_PREV_SCENE = 139
ACTION_PVR_PLAY = 188
ACTION_PVR_PLAY_RADIO = 190
ACTION_PVR_PLAY_TV = 189
ACTION_PVR_SHOW_TIMER_RULE = 191
ACTION_QUEUE_ITEM = 34
ACTION_RECORD = 170
ACTION_RELOAD_KEYMAPS = 203
ACTION_REMOVE_ITEM = 35
ACTION_RENAME_ITEM = 87
ACTION_REWIND = 17
ACTION_ROTATE_PICTURE_CCW = 51
ACTION_ROTATE_PICTURE_CW = 50
ACTION_SCAN_ITEM = 201
ACTION_SCROLL_DOWN = 112
ACTION_SCROLL_UP = 111
ACTION_SELECT_ITEM = 7
ACTION_SETTINGS_LEVEL_CHANGE = 242
ACTION_SETTINGS_RESET = 241
ACTION_SET_RATING = 164
ACTION_SHIFT = 118
ACTION_SHOW_FULLSCREEN = 36
ACTION_SHOW_GUI = 18
ACTION_SHOW_INFO = 11
ACTION_SHOW_OSD = 24
ACTION_SHOW_OSD_TIME = 123
ACTION_SHOW_PLAYLIST = 33
ACTION_SHOW_SUBTITLES = 25
ACTION_SHOW_VIDEOMENU = 134
ACTION_SMALL_STEP_BACK = 76
ACTION_STEP_BACK = 21
ACTION_STEP_FORWARD = 20
ACTION_STEREOMODE_NEXT = 235
ACTION_STEREOMODE_PREVIOUS = 236
ACTION_STEREOMODE_SELECT = 238
ACTION_STEREOMODE_SET = 240
ACTION_STEREOMODE_TOGGLE = 237
ACTION_STEREOMODE_TOMONO = 239
ACTION_STOP = 13
ACTION_SUBTITLE_ALIGN = 232
ACTION_SUBTITLE_DELAY = 162
ACTION_SUBTITLE_DELAY_MIN = 52
ACTION_SUBTITLE_DELAY_PLUS = 53
ACTION_SUBTITLE_VSHIFT_DOWN = 231
ACTION_SUBTITLE_VSHIFT_UP = 230
ACTION_SWITCH_PLAYER = 234
ACTION_SYMBOLS = 119
ACTION_TAKE_SCREENSHOT = 85
ACTION_TELETEXT_BLUE = 218
ACTION_TELETEXT_GREEN = 216
ACTION_TELETEXT_RED = 215
ACTION_TELETEXT_YELLOW = 217
ACTION_TOGGLE_COMMSKIP = 246
ACTION_TOGGLE_DIGITAL_ANALOG = 202
ACTION_TOGGLE_FONT = 249
ACTION_TOGGLE_FULLSCREEN = 199
ACTION_TOGGLE_SOURCE_DEST = 32
ACTION_TOGGLE_WATCHED = 200
ACTION_TOUCH_LONGPRESS = 411
ACTION_TOUCH_LONGPRESS_TEN = 420
ACTION_TOUCH_TAP = 401
ACTION_TOUCH_TAP_TEN = 410
ACTION_TRIGGER_OSD = 243
ACTION_VIS_PRESET_LOCK = 130
ACTION_VIS_PRESET_NEXT = 128
ACTION_VIS_PRESET_PREV = 129
ACTION_VIS_PRESET_RANDOM = 131
ACTION_VIS_PRESET_SHOW = 126
ACTION_VIS_RATE_PRESET_MINUS = 133
ACTION_VIS_RATE_PRESET_PLUS = 132
ACTION_VOICE_RECOGNIZE = 300
ACTION_VOLAMP = 90
ACTION_VOLAMP_DOWN = 94
ACTION_VOLAMP_UP = 93
ACTION_VOLUME_DOWN = 89
ACTION_VOLUME_SET = 245
ACTION_VOLUME_UP = 88
ACTION_VSHIFT_DOWN = 228
ACTION_VSHIFT_UP = 227
ACTION_ZOOM_IN = 31
ACTION_ZOOM_LEVEL_1 = 38
ACTION_ZOOM_LEVEL_2 = 39
ACTION_ZOOM_LEVEL_3 = 40
ACTION_ZOOM_LEVEL_4 = 41
ACTION_ZOOM_LEVEL_5 = 42
ACTION_ZOOM_LEVEL_6 = 43
ACTION_ZOOM_LEVEL_7 = 44
ACTION_ZOOM_LEVEL_8 = 45
ACTION_ZOOM_LEVEL_9 = 46
ACTION_ZOOM_LEVEL_NORMAL = 37
ACTION_ZOOM_OUT = 30
ALPHANUM_HIDE_INPUT = 2
CONTROL_TEXT_OFFSET_X = 10
CONTROL_TEXT_OFFSET_Y = 2
HORIZONTAL = 0
ICON_OVERLAY_HD = 6
ICON_OVERLAY_LOCKED = 3
ICON_OVERLAY_NONE = 0
ICON_OVERLAY_RAR = 1
ICON_OVERLAY_UNWATCHED = 4
ICON_OVERLAY_WATCHED = 5
ICON_OVERLAY_ZIP = 2
ICON_TYPE_FILES = 106
ICON_TYPE_MUSIC = 103
ICON_TYPE_NONE = 101
ICON_TYPE_PICTURES = 104
ICON_TYPE_PROGRAMS = 102
ICON_TYPE_SETTINGS = 109
ICON_TYPE_VIDEOS = 105
ICON_TYPE_WEATHER = 107
INPUT_ALPHANUM = 0
INPUT_DATE = 2
INPUT_IPADDRESS = 4
INPUT_NUMERIC = 1
INPUT_PASSWORD = 5
INPUT_TIME = 3
KEY_APPCOMMAND = 53248
KEY_ASCII = 61696
KEY_BUTTON_A = 256
KEY_BUTTON_B = 257
KEY_BUTTON_BACK = 275
KEY_BUTTON_BLACK = 260
KEY_BUTTON_DPAD_DOWN = 271
KEY_BUTTON_DPAD_LEFT = 272
KEY_BUTTON_DPAD_RIGHT = 273
KEY_BUTTON_DPAD_UP = 270
KEY_BUTTON_LEFT_ANALOG_TRIGGER = 278
KEY_BUTTON_LEFT_THUMB_BUTTON = 276
KEY_BUTTON_LEFT_THUMB_STICK = 264
KEY_BUTTON_LEFT_THUMB_STICK_DOWN = 281
KEY_BUTTON_LEFT_THUMB_STICK_LEFT = 282
KEY_BUTTON_LEFT_THUMB_STICK_RIGHT = 283
KEY_BUTTON_LEFT_THUMB_STICK_UP = 280
KEY_BUTTON_LEFT_TRIGGER = 262
KEY_BUTTON_RIGHT_ANALOG_TRIGGER = 279
KEY_BUTTON_RIGHT_THUMB_BUTTON = 277
KEY_BUTTON_RIGHT_THUMB_STICK = 265
KEY_BUTTON_RIGHT_THUMB_STICK_DOWN = 267
KEY_BUTTON_RIGHT_THUMB_STICK_LEFT = 268
KEY_BUTTON_RIGHT_THUMB_STICK_RIGHT = 269
KEY_BUTTON_RIGHT_THUMB_STICK_UP = 266
KEY_BUTTON_RIGHT_TRIGGER = 263
KEY_BUTTON_START = 274
KEY_BUTTON_WHITE = 261
KEY_BUTTON_X = 258
KEY_BUTTON_Y = 259
KEY_INVALID = 65535
KEY_MOUSE_CLICK = 57344
KEY_MOUSE_DOUBLE_CLICK = 57360
KEY_MOUSE_DRAG = 57604
KEY_MOUSE_DRAG_END = 57606
KEY_MOUSE_DRAG_START = 57605
KEY_MOUSE_END = 61439
KEY_MOUSE_LONG_CLICK = 57376
KEY_MOUSE_MIDDLECLICK = 57346
KEY_MOUSE_MOVE = 57603
KEY_MOUSE_NOOP = 61439
KEY_MOUSE_RDRAG = 57607
KEY_MOUSE_RDRAG_END = 57609
KEY_MOUSE_RDRAG_START = 57608
KEY_MOUSE_RIGHTCLICK = 57345
KEY_MOUSE_START = 57344
KEY_MOUSE_WHEEL_DOWN = 57602
KEY_MOUSE_WHEEL_UP = 57601
KEY_UNICODE = 61952
KEY_VKEY = 61440
KEY_VMOUSE = 61439
NOTIFICATION_ERROR = 'error'
NOTIFICATION_INFO = 'info'
NOTIFICATION_WARNING = 'warning'
PASSWORD_VERIFY = 1
REMOTE_0 = 58
REMOTE_1 = 59
REMOTE_2 = 60
REMOTE_3 = 61
REMOTE_4 = 62
REMOTE_5 = 63
REMOTE_6 = 64
REMOTE_7 = 65
REMOTE_8 = 66
REMOTE_9 = 67
VERTICAL = 1


class Control(object):
    """
    Code based skin access

    Offers classes and functions that manipulate the add-on gui controls. 

    **Code based skin access.**

    Kodi is noted as having a very flexible and robust framework for its GUI,
    making theme-skinning and personal customization very accessible.
    Users can create their own skin (or modify an existing skin) and share it
    with others.

    Kodi includes a new GUI library written from scratch. This library allows
    you to skin/change everything you see in Kodi, from the images, the sizes
    and positions of all controls, colours, fonts, and text, through to altering
    navigation and even adding new functionality. The skin system is quite
    complex, and this portion of the manual is dedicated to providing in depth
    information on how it all works, along with tips to make the experience
    a little more pleasant.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getId(self):
        # type: () -> int
        """
        Returns the control's current id as an integer. 

        :return: int - Current id

        Example::

            ...
            id = self.button.getId()
            ...
        """
        return 0
    
    def getX(self):
        # type: () -> int
        """
        Returns the control's current X position. 

        :return: int - Current X position

        Example::

            ...
            posX = self.button.getX()
            ...
        """
        return 0
    
    def getY(self):
        # type: () -> int
        """
        Returns the control's current Y position. 

        :return: int - Current Y position

        Example::

            ...
            posY = self.button.getY()
            ...
        """
        return 0
    
    def getHeight(self):
        # type: () -> int
        """
        Returns the control's current height as an integer. 

        :return: int - Current height

        Example::

            ...
            height = self.button.getHeight()
            ...
        """
        return 0
    
    def getWidth(self):
        # type: () -> int
        """
        Returns the control's current width as an integer. 

        :return: int - Current width

        Example::

            ...
            width = self.button.getWidth()
            ...
        """
        return 0
    
    def setEnabled(self, enabled):
        # type: (bool) -> None
        """
        Set's the control's enabled/disabled state. 

        :param enabled: bool - True=enabled / False=disabled.

        Example::

            ...
            self.button.setEnabled(False)
            ...
        """
        pass
    
    def setVisible(self, visible):
        # type: (bool) -> None
        """
        Set's the control's visible/hidden state. 

        :param visible: bool - True=visible / False=hidden.

        Example::

            ...
            self.button.setVisible(False)
            ...
        """
        pass
    
    def setVisibleCondition(self, visible, allowHiddenFocus=False):
        # type: (str, bool) -> None
        """
        Set's the control's visible condition. 

        Allows Kodi to control the visible status of the control.

        List of Conditions

        :param visible: string - Visible condition 
        :param allowHiddenFocus: [opt] bool - True=gains focus even if hidden

        Example::

            ...
            # setVisibleCondition(visible[,allowHiddenFocus])
            self.button.setVisibleCondition('[Control.IsVisible(41) + !Control.IsVisible(12)]', True)
            ...
        """
        pass
    
    def setEnableCondition(self, enable):
        # type: (str) -> None
        """
        Set's the control's enabled condition. 

        Allows Kodi to control the enabled status of the control.

        List of Conditions

        :param enable: string - Enable condition.

        Example::

            ...
            # setEnableCondition(enable)
            self.button.setEnableCondition('System.InternetState')
            ...
        """
        pass
    
    def setAnimations(self, eventAttr):
        # type: (List[Tuple[str_type, str_type]]) -> None
        """
        Set's the control's animations. 

        **[(event,attr,)*]**: list - A list of tuples consisting of event
        and attributes pairs.

        Animating your skin

        :param event: string - The event to animate. 
        :param attr: string - The whole attribute string separated by spaces.

        Example::

            ...
            # setAnimations([(event, attr,)*])
            self.button.setAnimations([('focus', 'effect=zoom end=90,247,220,56 time=0',)])
            ...
        """
        pass
    
    def setPosition(self, x, y):
        # type: (int_type, int_type) -> None
        """
        Set's the controls position. 

        :param x: integer - x coordinate of control. 
        :param y: integer - y coordinate of control.

        You may use negative integers. (e.g sliding a control into view)

        Example::

            ...
            self.button.setPosition(100, 250)
            ...
        """
        pass
    
    def setWidth(self, width):
        # type: (int_type) -> None
        """
        Set's the controls width. 

        :param width: integer - width of control.

        Example::

            ...
            self.image.setWidth(100)
            ...
        """
        pass
    
    def setHeight(self, height):
        # type: (int_type) -> None
        """
        Set's the controls height. 

        :param height: integer - height of control.

        Example::

            ...
            self.image.setHeight(100)
            ...
        """
        pass
    
    def setNavigation(self, up, down, left, right):
        # type: (Control, Control, Control, Control) -> None
        """
        Set's the controls navigation. 

        :param up: control object - control to navigate to on up. 
        :param down: control object - control to navigate to on down. 
        :param left: control object - control to navigate to on left. 
        :param right: control object - control to navigate to on right. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        Same as controlUp(), controlDown(), controlLeft(), controlRight().
        Set to self to disable navigation for that direction.

        Example::

            ...
            self.button.setNavigation(self.button1, self.button2, self.button3, self.button4)
            ...
        """
        pass
    
    def controlUp(self, up):
        # type: (Control) -> None
        """
        Set's the controls up navigation. 

        :param control: control object - control to navigate to on up. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlUp(self.button1)
            ...
        """
        pass
    
    def controlDown(self, control):
        # type: (Control) -> None
        """
        Set's the controls down navigation. 

        :param control: control object - control to navigate to on down. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlDown(self.button1)
            ...
        """
        pass
    
    def controlLeft(self, control):
        # type: (Control) -> None
        """
        Set's the controls left navigation. 

        :param control: control object - control to navigate to on left. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlLeft(self.button1)
            ...
        """
        pass
    
    def controlRight(self, control):
        # type: (Control) -> None
        """
        Set's the controls right navigation. 

        :param control: control object - control to navigate to on right. 
        :raises TypeError: if one of the supplied arguments is not a control type. 
        :raises ReferenceError: if one of the controls is not added to a window.

        You can also use setNavigation(). Set to self to disable navigation.

        Example::

            ...
            self.button.controlRight(self.button1)
            ...
        """
        pass
    

class ControlSpin(Control):
    """
    Used for cycling up/down controls

    Offers classes and functions that manipulate the add-on gui controls. 

    **Code based skin access.**

    The spin control is used for when a list of options can be chosen
    (such as a page up/down control). You can choose the position, size,
    and look of the spin control.

    This class include also all calls from Control

    .. warning::
        **Not working yet**. You can't create this object, it is returned
        by objects like ControlTextBox and ControlList.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def setTextures(self, up, down, upFocus, downFocus, upDisabled, downDisabled):
        # type: (str, str, str, str, str, str) -> None
        """
        Set's textures for this control. 

        Texture are image files that are used for example in the skin

        .. warning:: **Not working yet**.

        :param up: label - for the up arrow when it doesn't have focus. 
        :param down: label - for the down button when it is not focused. 
        :param upFocus: label - for the up button when it has focus. 
        :param downFocus: label - for the down button when it has focus. 
        :param upDisabled: label - for the up arrow when the button is disabled. 
        :param downDisabled: label - for the up arrow when the button is disabled.

        Example::

            ...
            # setTextures(up, down, upFocus, downFocus, upDisabled, downDisabled)
            
            ...
        """
        pass
    

class ControlLabel(Control):
    """
    Used to show some lines of text

    The label control is used for displaying text in Kodi. You can choose
    the font, size, colour, location and contents of the text to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled label's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label.
        (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param hasPath: [opt] bool - True=stores a path / False=no path 
    :param angle: [opt] integer - angle of control.
        (**+** rotates CCW, **-** rotates CW)

    Example::

        ...
        # ControlLabel(x, y, width, height, label[, font, textColor,
        #              disabledColor, alignment, hasPath, angle])
        self.label = xbmcgui.ControlLabel(100, 250, 125, 75, 'Status', angle=45)
        ...
    """
    
    def __init__(self, x, y, width, height, label, font=None, textColor=None,
                 disabledColor=None, alignment=0, hasPath=False, angle=0):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, int_type, bool, int_type) -> None
        pass
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the text value for this label. 

        :return: This label

        Example::

            ...
            label = self.label.getLabel()
            ...
        """
        return ""
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's text for this label. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled label's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.label.setLabel('Status')
            ...
        """
        pass
    

class ControlEdit(Control):
    """
    Used as an input control for the osd keyboard and other input fields

    The edit control allows a user to input text in Kodi. You can choose
    the font, size, colour, location and header of the text to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled label's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled label's label.
        (e.g. '0xFFFF3300')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param focusTexture: [opt] string - filename for focus texture. 
    :param noFocusTexture: [opt] string - filename for no focus texture. 
    :param isPassword: [opt] bool - True=mask text value with  ``****``.

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.edit = xbmcgui.ControlEdit(100, 250, 125, 75, 'Status')
        ...
    """
    
    def __init__(self, x, y, width, height, label, font=None, textColor=None,
                 disabledColor=None, _alignment=0, focusTexture=None,
                 noFocusTexture=None, isPassword=False):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, int_type, str, str, bool) -> None
        pass
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's text heading for this edit control. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled label's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled label's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFF00FFFF')
        :param label2: [opt] string or unicode - text string.

        Example::

            ...
            self.edit.setLabel('Status')
            ...
        """
        pass
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the text heading for this edit control. 

        :return: Heading text

        Example::

            ...
            label = self.edit.getLabel()
            ...
        """
        return ""
    
    def setText(self, text):
        # type: (str_type) -> None
        """
        Set's text value for this edit control. 

        :param value: string or unicode - text string.

        Example::

            ...
            self.edit.setText('online')
            ...
        """
        pass
    
    def getText(self):
        # type: () -> str
        """
        Returns the text value for this edit control. 

        :return: Text value of control

        New function added.

        Example::

            ...
            value = self.edit.getText()
            ...
        """
        return ""
    

class ControlList(Control):
    """
    Used for a scrolling lists of items. Replaces the list control

    The list container is one of several containers used to display items from
    file lists in various ways. The list container is very flexible - it's only
    restriction is that it is a list - i.e. a single column or row of items.
    The layout of the items is very flexible and is up to the skinner.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for items label. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of items label. (e.g. '0xFFFFFFFF') 
    :param buttonTexture: [opt] string - filename for focus texture. 
    :param buttonFocusTexture: [opt] string - filename for no focus texture. 
    :param selectedColor: [opt] integer - x offset of label. 
    :param imageWidth: [opt] integer - width of items icon or thumbnail. 
    :param imageHeight: [opt] integer - height of items icon or thumbnail. 
    :param itemTextXOffset: [opt] integer - x offset of items label. 
    :param itemTextYOffset: [opt] integer - y offset of items label. 
    :param itemHeight: [opt] integer - height of items. 
    :param space: [opt] integer - space between items.
    :param alignmentY: [opt] integer - Y-axis alignment of items labelFlags
        for alignment used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param shadowColor: [opt] hexstring - color of items label's shadow.
        (e.g. '0xFF000000')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.cList = xbmcgui.ControlList(100, 250, 200, 250, 'font14', space=5)
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None,
                 buttonTexture=None, buttonFocusTexture=None,
                 selectedColor=None, _imageWidth=10, _imageHeight=10,
                 _itemTextXOffset=10, _itemTextYOffset=2, _itemHeight=27,
                 _space=2, _alignmentY=4):
        # type: (int_type, int_type, int_type, int_type, str, str, str, str, str, int_type, int_type, int_type, int_type, int_type, int_type, int_type) -> None
        pass
    
    def addItem(self, item, sendMessage=True):
        # type: (Union[str_type, ListItem], bool) -> None
        """
        Add a new item to this list control. 

        :param item: string, unicode or ListItem - item to add.

        Example::

            ...
            cList.addItem('Reboot Kodi')
            ...
        """
        pass
    
    def addItems(self, items):
        # type: (List[Union[str_type, ListItem]]) -> None
        """
        Adds a list of listitems or strings to this list control. 

        :param items: List - list of strings, unicode objects or ListItems to add.

        You can use the above as keywords for arguments.

        Large lists benefit considerably, than using the standard addItem()

        Example::

            ...
            cList.addItems(items=listitems)
            ...
        """
        pass
    
    def selectItem(self, item):
        # type: (int_type) -> None
        """
        Select an item by index number. 

        :param item: integer - index number of the item to select.

        Example::

            ...
            cList.selectItem(12)
            ...
        """
        pass
    
    def removeItem(self, index):
        # type: (int) -> None
        """
        Remove an item by index number. 

        :param index: integer - index number of the item to remove.

        New function added.

        Example::

            ...
            cList.removeItem(12)
            ...
        """
        pass
    
    def reset(self):
        # type: () -> None
        """
        Clear all ListItems in this control list. 

        Example::

            ...
            cList.reset()
            ...
        """
        pass
    
    def getSpinControl(self):
        # type: () -> Control
        """
        Returns the associated ControlSpin object.

        .. warning::
            Not working completely yet After adding this control list to
            a window it is not possible to change the settings
            of this spin control.

        Example::

            ...
            ctl = cList.getSpinControl()
            ...
        """
        return Control()
    
    def getSelectedPosition(self):
        # type: () -> long
        """
        Returns the position of the selected item as an integer.

        Returns -1 for empty lists.

        Example::

            ...
            pos = cList.getSelectedPosition()
            ...
        """
        return 0
    
    def getSelectedItem(self):
        # type: () -> ListItem
        """
        Returns the selected item as a ListItem object. 

        :return: The selected item

        Same as getSelectedPosition(), but instead of an integer a ListItem
        object is returned. Returns None for empty lists.
        See windowexample.py on how to use this.

        Example::

            ...
            item = cList.getSelectedItem()
            ...
        """
        return ListItem()
    
    def setImageDimensions(self, imageWidth, imageHeight):
        # type: (int_type, int_type) -> None
        """
        Sets the width/height of items icon or thumbnail. 

        :param imageWidth: [opt] integer - width of items icon or thumbnail. 
        :param imageHeight: [opt] integer - height of items icon or thumbnail.

        Example::

            ...
            cList.setImageDimensions(18, 18)
            ...
        """
        pass
    
    def setSpace(self, space):
        # type: (int) -> None
        """
        Set's the space between items. 

        :param space: [opt] integer - space between items.

        Example::

            ...
            cList.setSpace(5)
            ...
        """
        pass
    
    def setPageControlVisible(self, visible):
        # type: (bool) -> None
        """
        Sets the spin control's visible/hidden state. 

        :param visible: boolean - True=visible / False=hidden.

        Example::

            ...
            cList.setPageControlVisible(True)
            ...
        """
        pass
    
    def size(self):
        # type: () -> long
        """
        Returns the total number of items in this list control as an integer.

        :return: Total number of items

        Example::

            ...
            cnt = cList.size()
            ...
        """
        return 0
    
    def getItemHeight(self):
        # type: () -> long
        """
        Returns the control's current item height as an integer. 

        :return: Current item heigh

        Example::

            ..
            item_height = self.cList.getItemHeight()
            ...
        """
        return 0
    
    def getSpace(self):
        # type: () -> long
        """
        Returns the control's space between items as an integer. 

        :return: Space between items

        Example::

            ...
            gap = self.cList.getSpace()
            ...
        """
        return 0
    
    def getListItem(self, index):
        # type: (int) -> ListItem
        """
        Returns a given ListItem in this List. 

        :param index: integer - index number of item to return. 
        :return: List item
        :raises ValueError: if index is out of range.

        Example::

            ...
            listitem = cList.getListItem(6)
            ...
        """
        return ListItem()
    
    def setStaticContent(self, items):
        # type: (List[ListItem]) -> None
        """
        Fills a static list with a list of listitems. 

        :param items: List - list of listitems to add.

        You can use the above as keywords for arguments.

        Example::

            ...
            cList.setStaticContent(items=listitems)
            ...
        """
        pass
    

class ControlFadeLabel(Control):
    """
    Used to show multiple pieces of text in the same position, by fading
    from one to the other

    The fade label control is used for displaying multiple pieces of text in
    the same space in Kodi. You can choose the font, size, colour, location
    and contents of the text to be displayed. The first piece of information
    to display fades in over 50 frames, then scrolls off to the left. Once it is
    finished scrolling off screen, the second piece of information fades in and
    the process repeats. A fade label control is not supported in
    a list container.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of fadelabel's labels.
        (e.g. '0xFFFFFFFF')
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        self.fadelabel = xbmcgui.ControlFadeLabel(100, 250, 200, 50, textColor='0xFFFFFFFF')
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None, _alignment=0):
        # type: (int_type, int_type, int_type, int_type, str, str, int_type) -> None
        pass
    
    def addLabel(self, label):
        # type: (str_type) -> None
        """
        Add a label to this control for scrolling. 

        :param label: string or unicode - text string to add.

        To remove added text use  ``reset()`` for them.

        Example::

            ...
            self.fadelabel.addLabel('This is a line of text that can scroll.')
            ...
        """
        pass
    
    def setScrolling(self, scroll):
        # type: (bool) -> None
        """
        Set scrolling. If set to false, the labels won't scroll. Defaults to true. 

        :param scroll: boolean - True = enabled / False = disabled

        Example::

            ...
            self.fadelabel.setScrolling(False)
            ...
        """
        pass
    

class ControlTextBox(Control):
    """
    Used to show a multi-page piece of text

    The text box is used for showing a large multipage piece of text in Kodi.
    You can choose the position, size, and look of the text.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param font: [opt] string - font used for text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of textbox's text.
        (e.g. '0xFFFFFFFF')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlTextBox(x, y, width, height[, font, textColor])
        self.textbox = xbmcgui.ControlTextBox(100, 250, 300, 300, textColor='0xFFFFFFFF')
        ...
    """
    
    def __init__(self, x, y, width, height, font=None, textColor=None):
        # type: (int_type, int_type, int_type, int_type, str, str) -> None
        pass
    
    def setText(self, text):
        # type: (str_type) -> None
        """
        Set's the text for this textbox. 

        :param text: string or unicode - text string.

        Example::

            ...
            # setText(text)
            self.textbox.setText('This is a line of text that can wrap.')
            ...
        """
        pass
    
    def getText(self):
        # type: () -> str
        """
        Returns the text value for this textbox. 

        :return: To get text from box

        Example::

            ...
            # getText()
            text = self.text.getText()
            ...
        """
        return ""
    
    def reset(self):
        # type: () -> None
        """
        Clear's this textbox.

        Example::

            ...
            # reset()
            self.textbox.reset()
            ...
        """
        pass
    
    def scroll(self, id):
        # type: (int_type) -> None
        """
        Scrolls to the given position. 

        :param id: integer - position to scroll to.

        Example::

            ...
            # scroll(position)
            self.textbox.scroll(10)
            ...
        """
        pass
    
    def autoScroll(self, delay, time, repeat):
        # type: (int, int, int) -> None
        """
        Set autoscrolling times. 

        :param delay: integer - Scroll delay (in ms) 
        :param time: integer - Scroll time (in ms) 
        :param repeat: integer - Repeat time

        New function added.

        Example::

            ...
            self.textbox.autoScroll(1, 2, 1)
            ...
        """
        pass
    

class ControlImage(Control):
    """
    Used to show an image

    The image control is used for displaying images in Kodi. You can choose
    the position, size, transparency and contents of the image to be displayed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param filename: string - image filename. 
    :param aspectRatio: [opt] integer - (values 0 = stretch (default),
        1 = scale up (crops), 2 = scale down (black bar)
    :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlImage(x, y, width, height, filename[, aspectRatio, colorDiffuse])
        self.image = xbmcgui.ControlImage(100, 250, 125, 75, aspectRatio=2)
        ...
    """
    
    def __init__(self, x, y, width, height, filename, aspectRatio=0, colorDiffuse=None):
        # type: (int_type, int_type, int_type, int_type, str, int_type, str) -> None
        pass
    
    def setImage(self, imageFilename, useCache=True):
        # type: (str, bool) -> None
        """
        Changes the image. 

        :param filename: string - image filename. 
        :param useCache: [opt] bool - True=use cache (default) /
            False=don't use cache.

        Added new option **useCache**.

        Example::

            ...
            # setImage(filename[, useCache])
            self.image.setImage('special://home/scripts/test.png')
            self.image.setImage('special://home/scripts/test.png', False)
            ...
        """
        pass
    
    def setColorDiffuse(self, hexString):
        # type: (str) -> None
        """
        Changes the images color. 

        :param colorDiffuse: hexString - (example, '0xC0FF0000' (red tint))

        Example::

            ...
            # setColorDiffuse(colorDiffuse)
            self.image.setColorDiffuse('0xC0FF0000')
            ...
        """
        pass
    

class ControlProgress(Control):
    """
    Used to show the progress of a particular operation

    The progress control is used to show the progress of an item that may take
    a long time, or to show how far through a movie you are. You can choose
    the position, size, and look of the progress control.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param filename: string - image filename. 
    :param texturebg: [opt] string - specifies the image file whichshould
        be displayed in the background of the progress control.
    :param textureleft: [opt] string - specifies the image file whichshould
        be displayed for the left side of the progress bar. This is rendered on the left side of the bar.
    :param texturemid: [opt] string - specifies the image file which should
        be displayed for the middl portion of the progress bar. This is the  ``fill`` texture used to fill up the bar. It's positioned on the right of the  ``<lefttexture>`` texture, and fills the gap between the  ``<lefttexture>`` and  ``<righttexture>`` textures, depending on how far progressed the item is.
    :param textureright: [opt] string - specifies the image file which
        should be displayed for the right side of the progress bar.
        This is rendered on the right side of the bar.
    :param textureoverlay: [opt] string - specifies the image file which
        should be displayed over the top of all other images in the progress bar.
        It is centered vertically and horizontally within the space taken up
        by the background image.

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require the keyword.
    After you create the control, you need to add it to the window with addControl().

    Example::

        ...
        # ControlProgress(x, y, width, height, filename[, texturebg, textureleft,
        # texturemid, textureright, textureoverlay])
        self.image = xbmcgui.ControlProgress(100, 250, 250, 30,
                                             'special://home/scripts/test.png')
        ...
    """
    
    def __init__(self, x, y, width, height, texturebg=None, textureleft=None,
                 texturemid=None, textureright=None, textureoverlay=None):
        # type: (int_type, int_type, int_type, int_type, str, str, str, str, str) -> None
        pass
    
    def setPercent(self, pct):
        # type: (float) -> None
        """
        Sets the percentage of the progressbar to show. 

        :param percent: float - percentage of the bar to show.

        valid range for percent is 0-100

        Example::

            ...
            # setPercent(percent)
            self.progress.setPercent(60)
            ...
        """
        pass
    
    def getPercent(self):
        # type: () -> float
        """
        Returns a float of the percent of the progress. 

        :return: Percent position

        Example::

            ...
            # getPercent()
            print self.progress.getPercent()
            ...
        """
        return 0.0
    

class ControlButton(Control):
    """
    A standard push button control

    The button control is used for creating push buttons in Kodi. You can
    choose the position, size, and look of the button, as well as choosing
    what action(s) should be performed when pushed.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param focusTexture: [opt] string - filename for focus texture. 
    :param noFocusTexture: [opt] string - filename for no focus texture. 
    :param textOffsetX: [opt] integer - x offset of label. 
    :param textOffsetY: [opt] integer - y offset of label. 
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of enabled button's label.
        (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of disabled button's label.
        (e.g. '0xFFFF3300')
    :param angle: [opt] integer - angle of control. (+ rotates CCW, - rotates CW) 
    :param shadowColor: [opt] hexstring - color of button's label's shadow.
        (e.g. '0xFF000000')
    :param focusedColor: [opt] hexstring - color of focused button's label.
        (e.g. '0xFF00FFFF')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    Example::

        ...
        # ControlButton(x, y, width, height, label[, focusTexture, noFocusTexture, textOffsetX, textOffsetY,
        #               alignment, font, textColor, disabledColor, angle, shadowColor, focusedColor])
        self.button = xbmcgui.ControlButton(100, 250, 200, 50, 'Status', font='font14')
        ...
    """
    
    def __init__(self, x, y, width, height, label, focusTexture=None,
                 noFocusTexture=None, textOffsetX=10, textOffsetY=2,
                 alignment=(0 | 4), font=None, textColor=None,
                 disabledColor=None, angle=0, shadowColor=None,
                 focusedColor=None):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, int_type, int_type, int_type, str, str, str, int_type, str, str) -> None
        pass
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's this buttons text attributes. 

        :param label: [opt] string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled button's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled button's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused button's label.
            (e.g. '0xFFFFFF00')
        :param label2: [opt] string or unicode - text string.

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            # setLabel([label, font, textColor, disabledColor, shadowColor, focusedColor])
            self.button.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setDisabledColor(self, color):
        # type: (str) -> None
        """
        Set's this buttons disabled color.

        :param disabledColor: hexstring - color of disabled button's label.
            (e.g. '0xFFFF3300')

        Example::

            ...
            # setDisabledColor(disabledColor)
            self.button.setDisabledColor('0xFFFF3300')
            ...
        """
        pass
    
    def getLabel(self):
        # type: () -> unicode
        """
        Returns the buttons label as a unicode string. 

        :return: Unicode string

        Example::

            ...
            # getLabel()
            label = self.button.getLabel()
            ...
        """
        return u""
    
    def getLabel2(self):
        # type: () -> unicode
        """
        Returns the buttons label2 as a unicode string. 

        :return: Unicode string of label 2

        Example::

            ...
            # getLabel2()
            label = self.button.getLabel2()
            ...
        """
        return u""
    

class ControlGroup(Control):
    """
    Used to group controls together

    The group control is one of the most important controls.
    It allows you to group controls together, applying attributes
    to all of them at once. It also remembers the last navigated button
    in the group, so you can set the ``<onup>`` of a control to a group
    of controls to have it always go back to the one you were at before.
    It also allows you to position controls more accurately relative
    to each other, as any controls within a group take their coordinates
    from the group's top left corner (or from elsewhere if you use the
    ``"r"`` attribute). You can have as many groups as you like within the skin,
    and groups within groups are handled with no issues.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control.

    Example::

        ...
        self.group = xbmcgui.ControlGroup(100, 250, 125, 75)
        ...
    """
    
    def __init__(self, x, y, width, height):
        # type: (int_type, int_type, int_type, int_type) -> None
        pass
    

class ControlRadioButton(Control):
    """
    For control a radio button (as used for on/off settings)

    The radio button control is used for creating push button on/off settings
    in Kodi. You can choose the position, size, and look of the button.
    When the user clicks on the radio button, the state will change, toggling
    the extra textures (textureradioon and textureradiooff).
    Used for settings controls.

    This class include also all calls from Control

    :param x: integer - x coordinate of control. 
    :param y: integer - y coordinate of control. 
    :param width: integer - width of control. 
    :param height: integer - height of control. 
    :param label: string or unicode - text string. 
    :param focusOnTexture: [opt] string - filename for radio ON focused texture. 
    :param noFocusOnTexture: [opt] string - filename for radio ON not focused texture. 
    :param focusOfTexture: [opt] string - filename for radio OFF focused texture. 
    :param noFocusOffTexture: [opt] string - filename for radio OFF not focused texture. 
    :param focusTexture: [opt] string - filename for radio ON texture
        (deprecated, use focusOnTexture and noFocusOnTexture).
    :param noFocusTexture: [opt] string - filename for radio OFF texture
        (deprecated, use focusOffTexture and noFocusOffTexture).
    :param textOffsetX: [opt] integer - horizontal text offset 
    :param textOffsetY: [opt] integer - vertical text offset 
    :param alignment: [opt] integer - alignment of labelFlags for alignment
        used as bits to have several together:

    =================  ===========  ===============
    Defination name    Bitflag      Description    
    =================  ===========  ===============
    XBFONT_LEFT        0x00000000   Align X left   
    XBFONT_RIGHT       0x00000001   Align X right  
    XBFONT_CENTER_X    0x00000002   Align X center 
    XBFONT_CENTER_Y    0x00000004   Align Y center 
    XBFONT_TRUNCATED   0x00000008   Truncated text 
    XBFONT_JUSTIFIED   0x00000010   Justify text   
    =================  ===========  ===============

    :param font: [opt] string - font used for label text. (e.g. 'font13') 
    :param textColor: [opt] hexstring - color of label when control is enabled.
        radiobutton's label. (e.g. '0xFFFFFFFF')
    :param disabledColor: [opt] hexstring - color of label when control is disabled.
        (e.g. '0xFFFF3300')

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    New function added.  Deprecated **focusTexture** and **noFocusTexture**.
    Use **focusOnTexture** and **noFocusOnTexture**.

    Example::

        ...
        self.radiobutton = xbmcgui.ControlRadioButton(100, 250, 200, 50, 'Enable', font='font14')
        ...
    """
    
    def __init__(self, x, y, width, height, label, focusOnTexture=None,
                 noFocusOnTexture=None, focusOffTexture=None,
                 noFocusOffTexture=None, focusTexture=None, noFocusTexture=None,
                 textOffsetX=10, textOffsetY=2, _alignment=(0 |4 ), font=None,
                 textColor=None, disabledColor=None, angle=0, shadowColor=None,
                 focusedColor=None, disabledOnTexture=None,
                 disabledOffTexture=None):
        # type: (int_type, int_type, int_type, int_type, str_type, str, str, str, str, str, str, int_type, int_type, int_type, str, str, str, int_type, str, str, str, str) -> None
        pass
    
    def setSelected(self, selected):
        # type: (bool) -> None
        """
        Sets the radio buttons's selected status

        :param selected: bool - True=selected (on) / False=not selected (off)

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            self.radiobutton.setSelected(True)
            ...
        """
        pass
    
    def isSelected(self):
        # type: () -> bool
        """
        Returns the radio buttons's selected status. 

        :return: True if selected on

        Example::

            ...
            is = self.radiobutton.isSelected()
            ...
        """
        return True
    
    def setLabel(self, label="", font=None, textColor=None, disabledColor=None,
                 shadowColor=None, focusedColor=None, label2=""):
        # type: (str_type, str, str, str, str, str, str_type) -> None
        """
        Set's the radio buttons text attributes. 

        :param label: string or unicode - text string. 
        :param font: [opt] string - font used for label text. (e.g. 'font13') 
        :param textColor: [opt] hexstring - color of enabled radio button's label.
            (e.g. '0xFFFFFFFF')
        :param disabledColor: [opt] hexstring - color of disabled radio button's label.
            (e.g. '0xFFFF3300')
        :param shadowColor: [opt] hexstring - color of radio button's label's shadow.
            (e.g. '0xFF000000')
        :param focusedColor: [opt] hexstring - color of focused radio button's label.
            (e.g. '0xFFFFFF00')

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            # setLabel(label[, font, textColor, disabledColor, shadowColor, focusedColor])
            self.radiobutton.setLabel('Status', 'font14', '0xFFFFFFFF', '0xFFFF3300', '0xFF000000')
            ...
        """
        pass
    
    def setRadioDimension(self, x, y, width, height):
        # type: (int_type, int_type, int_type, int_type) -> None
        """
        Sets the radio buttons's radio texture's position and size. 

        :param x: integer - x coordinate of radio texture. 
        :param y: integer - y coordinate of radio texture. 
        :param width: integer - width of radio texture. 
        :param height: integer - height of radio texture.

        You can use the above as keywords for arguments and skip certain
        optional arguments. Once you use a keyword, all following arguments
        require the keyword.

        Example::

            ...
            self.radiobutton.setRadioDimension(x=100, y=5, width=20, height=20)
            ...
        """
        pass
    

class ControlSlider(Control):
    """
    Used for a volume slider

    The slider control is used for things where a sliding bar best represents
    the operation at hand (such as a volume control or seek control).
    You can choose the position, size, and look of the slider control.

    This class include also all calls from Control

    :param x: integer - x coordinate of control 
    :param y: integer - y coordinate of control 
    :param width: integer - width of control 
    :param height: integer - height of control 
    :param textureback: [opt] string - image filename 
    :param texture: [opt] string - image filename 
    :param texturefocus: [opt] string - image filename 
    :param orientation: [opt] integer - orientation of slider
        (xbmcgui.HORIZONTAL / xbmcgui.VERTICAL (default))

    You can use the above as keywords for arguments and skip certain optional
    arguments. Once you use a keyword, all following arguments require
    the keyword. After you create the control, you need to add it to the window
    with addControl().

    **orientation** option added.

    Example::

        ...
        self.slider = xbmcgui.ControlSlider(100, 250, 350, 40)
        ...
    """
    
    def __init__(self, x, y, width, height, textureback=None, texture=None,
                 texturefocus=None, orientation=VERTICAL):
        # type: (int_type, int_type, int_type, int_type, str, str, str, int) -> None
        pass
    
    def getPercent(self):
        # type: () -> float
        """
        Returns a float of the percent of the slider. 

        :return: float - Percent of slider

        Example::

            ...
            print self.slider.getPercent()
            ...
        """
        return 0.0
    
    def setPercent(self, pct):
        # type: (float) -> None
        """
        Sets the percent of the slider. 

        :param pct: float - Percent value of slider

        Example::

            ...
            self.slider.setPercent(50)
            ...
        """
        pass
    

class Dialog(object):
    """
    Kodi's dialog class

    The graphical control element dialog box (also called dialogue box or
    just dialog) is a small window that communicates information to the user
    and prompts them for a response.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def yesno(self, heading, line1, line2="", line3="", nolabel="", yeslabel="",
              autoclose=0):
        # type: (str_type, str_type, str_type, str_type, str_type, str_type, int) -> bool
        """
        Yes / no dialog

        The Yes / No dialog can be used to inform the user about questions
        and get the answer.

        :param heading: string or unicode - dialog heading. 
        :param line1: string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text. 
        :param nolabel: [opt] label to put on the no button. 
        :param yeslabel: [opt] label to put on the yes button. 
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :return: Returns True if 'Yes' was pressed, else False.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Added new option **autoclose**.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.yesno('Kodi', 'Do you want to exit this script?')
            ..
        """
        return True
    
    def info(self, item):
        # type: (ListItem) -> bool
        """
        Info dialog

        Show the corresponding info dialog for a given listitem

        :param listitem: xbmcgui.ListItem - ListItem to show info for. 
        :return: Returns whether the dialog opened successfully.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.info(listitem)
            ..
        """
        return True
    
    def select(self, heading, list, autoclose=0, preselect=-1, useDetails=False):
        # type: (str_type, List[Union[str_type, ListItem]], int, int, bool) -> int
        """
        Select dialog

        Show of a dialog to select of an entry as a key

        :param heading: string or unicode - dialog heading. 
        :param list: list of strings / xbmcgui.ListItems - list of items shown
            in dialog.
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :param preselect: [opt] integer - index of preselected item.
            (default=no preselected item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the position of the highlighted item as an integer.

        **preselect** option added.  Added new option **useDetails**.
        Allow listitems for parameter **list**

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.select('Choose a playlist', ['Playlist #1', 'Playlist #2, 'Playlist #3'])
            ..
        """
        return 0
    
    def contextmenu(self, list):
        # type: (List[str_type]) -> int
        """
        Show a context menu.

        :param list: string list - list of items. 
        :return: the position of the highlighted item as an integer
            (-1 if cancelled).

        New function added

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.contextmenu(['Option #1', 'Option #2', 'Option #3'])
            ..
        """
        return 0
    
    def multiselect(self, heading, options, autoclose=0, preselect=None,
                    useDetails=False):
        # type: (str_type, List[Union[str_type, ListItem]], int, List[int], bool) -> List[int]
        """
        Show a multi-select dialog.

        :param heading: string or unicode - dialog heading. 
        :param options: list of strings / xbmcgui.ListItems - options to choose from. 
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :param preselect: [opt] list of int - indexes of items to preselect
            in list (default: do not preselect any item)
        :param useDetails: [opt] bool - use detailed list instead of a compact list.
            (default=false)
        :return: Returns the selected items as a list of indices, or None if cancelled.

        New function added.  Added new option **preselect**.
        Added new option **useDetails**.  Allow listitems for parameter **options**

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ret = dialog.multiselect("Choose something", ["Foo", "Bar", "Baz"], preselect=[1,2])
            ..
        """
        return [0]
    
    def ok(self, heading, line1, line2="", line3=""):
        # type: (str_type, str_type, str_type, str_type) -> bool
        """
        OK dialog

        The functions permit the call of a dialog of information, a confirmation
        of the user by press from OK required.

        :param heading: string or unicode - dialog heading. 
        :param line1: string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text. 
        :return: Returns True if 'Ok' was pressed, else False.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            ok = dialog.ok('Kodi', 'There was an error.')
            ..
        """
        return True
    
    def textviewer(self, heading, text):
        # type: (str_type, str_type) -> None
        """
        **TextViewe dialog**

        The text viewer dialog can be used to display descriptions,
        help texts or other larger texts.

        :param heading: string or unicode - dialog heading. 
        :param text: string or unicode - text.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.textviewer('Plot', 'Some movie plot.')
            ..
        """
        pass
    
    def browse(self, type, heading, shares, mask="", useThumbs=False,
               treatAsFolder=False, defaultt="", enableMultiple=False):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type, bool) -> Union[str, List[str]]
        """
        Browser dialog

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers all support file types.

        :param type: integer - the type of browse dialog.

        ======  =============================
        Param   Name                         
        ======  =============================
        0       ShowAndGetDirectory          
        1       ShowAndGetFile               
        2       ShowAndGetImage              
        3       ShowAndGetWriteableDirectory 
        ======  =============================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if files exist. 
        :param treatAsFolder: [opt] boolean - if True playlists and archives act as folders. 
        :param defaultt: [opt] string - default path or file. 
        :param enableMultiple: [opt] boolean - if True multiple file selection is enabled.
        :return: If enableMultiple is False (default): returns filename and/or
            path as a string to the location of the highlighted item,
            if user pressed 'Ok' or a masked item was selected.
            Returns the default value if dialog was canceled. If enableMultiple
            is True: returns tuple of marked filenames as a strin if user
            pressed 'Ok' or a masked item was selected.
            Returns empty tuple if dialog was canceled.
            If type is 0 or 3 the enableMultiple parameter is ignore

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browse(3, 'Kodi', 'files', '', False, False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseSingle(self, type, heading, shares, mask="", useThumbs=False,
                     treatAsFolder=False, defaultt=""):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type) -> str
        """
        Browse single dialog

        The function offer the possibility to select a file by the user of the add-on.

        It allows all the options that are possible in Kodi itself and offers
        all support file types.

        :param type: integer - the type of browse dialog.

        ======  =============================
        Param   Name                         
        ======  =============================
        0       ShowAndGetDirectory          
        1       ShowAndGetFile               
        2       ShowAndGetImage              
        3       ShowAndGetWriteableDirectory 
        ======  =============================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view if
            files exist (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives
            act as folders (default=false).
        :param defaultt: [opt] string - default path or file.
        :return: Returns filename and/or path as a string to the location
            of the highlighted item, if user pressed 'Ok' or a masked item
            was selected. Returns the default value if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseSingle(3, 'Kodi', 'files', '', False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return ""
    
    def browseMultiple(self, type, heading, shares, mask="", useThumbs=False,
                       treatAsFolder=False, defaultt=""):
        # type: (int, str_type, str_type, str_type, bool, bool, str_type) -> List[str]
        """
        Browser dialog

        The function offer the possibility to select multiple files by the user
        of the add-on.

        It allows all the options that are possible in Kodi itself and offers
        all support file types.

        :param type: integer - the type of browse dialog.

        ======  ================
        Param   Name            
        ======  ================
        1       ShowAndGetFile  
        2       ShowAndGetImage 
        ======  ================

        :param heading: string or unicode - dialog heading. 
        :param shares: string or unicode - from sources.xml . (i.e. 'myprograms') 
        :param mask: [opt] string or unicode - '|' separated file mask. (i.e. '.jpg|.png') 
        :param useThumbs: [opt] boolean - if True autoswitch to Thumb view
            if files exist (default=false).
        :param treatAsFolder: [opt] boolean - if True playlists and archives
            act as folders (default=false).
        :param defaultt: [opt] string - default path or file. 
        :return: Returns tuple of marked filenames as a string," if user
            pressed 'Ok' or a masked item was selected.
            Returns empty tuple if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            fn = dialog.browseMultiple(2, 'Kodi', 'files', '', False, False,
                            'special://masterprofile/script_data/Kodi Lyrics')
            ..
        """
        return [""]
    
    def numeric(self, type, heading, defaultt=""):
        # type: (int, str_type, str_type) -> str
        """
        **Numeric dialog**

        The function have to be permitted by the user for the representation
        of a numeric keyboard around an input.

        :param type: integer - the type of numeric dialog.

        ======  ====================  =============================
        Param   Name                  Format                       
        ======  ====================  =============================
        0       ShowAndGetNumber      (default format: #)          
        1       ShowAndGetDate        (default format: DD/MM/YYYY) 
        2       ShowAndGetTime        (default format: HH:MM)      
        3       ShowAndGetIPAddress   (default format: #.#.#.#)    
        ======  ====================  =============================

        :param heading: string or unicode - dialog heading. 
        :param defaultt: [opt] string - default value. 
        :return: Returns the entered data as a string.
            Returns the default value if dialog was canceled.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.numeric(1, 'Enter date of birth')
            ..
        """
        return ""
    
    def notification(self, heading, message, icon="", time=0, sound=True):
        # type: (str_type, str_type, str_type, int, bool) -> None
        """
        Show a Notification alert.

        :param heading: string - dialog heading. 
        :param message: string - dialog message. 
        :param icon: [opt] string - icon to use. (default xbmcgui.NOTIFICATION_INFO) 
        :param time: [opt] integer - time in milliseconds (default 5000) 
        :param sound: [opt] bool - play notification sound (default True)

        Builtin Icons:xbmcgui.NOTIFICATION_INFO

        xbmcgui.NOTIFICATION_WARNING

        xbmcgui.NOTIFICATION_ERROR

          New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            dialog.notification('Movie Trailers', 'Finding Nemo download finished.',
                                xbmcgui.NOTIFICATION_INFO, 5000)
            ..
        """
        pass
    
    def input(self, heading, defaultt="", type=0, option=0, autoclose=0):
        # type: (str_type, str_type, int, int, int) -> str
        """
        Show an Input dialog.

        :param heading: string - dialog heading. 
        :param defaultt: [opt] string - default value. (default=empty string) 
        :param type: [opt] integer - the type of keyboard dialog.
            (default=xbmcgui.INPUT_ALPHANUM)

        =======================  ========
        Parameter                Format  
        =======================  ========
        xbmcgui.INPUT_ALPHANUM   (standard keyboard)
        xbmcgui.INPUT_NUMERIC    (format: #)
        xbmcgui.INPUT_DATE       (format: DD/MM/YYYY)
        xbmcgui.INPUT_TIME       (format: HH:MM)
        xbmcgui.INPUT_IPADDRESS  (format: #.#.#.#)
        xbmcgui.INPUT_PASSWORD   (return md5 hash of input, input is masked)
        =======================  ========

        :param option: [opt] integer - option for the dialog. (see Options below)
            Password dialog: ``xbmcgui.PASSWORD_VERIFY`` (verifies an existing
            (default) md5 hashed password)Alphanum dialog:
            ``xbmcgui.ALPHANUM_HIDE_INPUT`` (masks input)
        :param autoclose: [opt] integer - milliseconds to autoclose dialog.
            (default=do not autoclose)
        :return: Returns the entered data as a string.
            Returns an empty string if dialog was canceled.

        New function added.

        Example::

            ..
            dialog = xbmcgui.Dialog()
            d = dialog.input('Enter secret code', type=xbmcgui.INPUT_ALPHANUM,
                             option=xbmcgui.ALPHANUM_HIDE_INPUT)
            ..
        """
        return ""
    

class DialogProgress(object):
    """
    Kodi's progress dialog class
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self, heading, line1="", line2="", line3=""):
        # type: (str_type, str_type, str_type, str_type) -> None
        """
        Create and show a progress dialog.

        :param heading: string or unicode - dialog heading. 
        :param line1: [opt] string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Use update() to update lines and progressbar.

        Example::

            ..
            pDialog = xbmcgui.DialogProgress()
            pDialog.create('Kodi', 'Initializing script...')
            ..
        """
        pass
    
    def update(self, percent, line1="", line2="", line3=""):
        # type: (int, str_type, str_type, str_type) -> None
        """
        Updates the progress dialog.

        :param percent: integer - percent complete. (0:100) 
        :param line1: [opt] string or unicode - line #1 multi-line text. 
        :param line2: [opt] string or unicode - line #2 text. 
        :param line3: [opt] string or unicode - line #3 text.

        It is preferred to only use line1 as it is actually a multi-line text.
        In this case line2 and line3 must be omitted.

        Example::

            ..
            pDialog.update(25, 'Importing modules...')
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the progress dialog.

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def iscanceled(self):
        # type: () -> bool
        """
        Checks progress is canceled.

        :return: True if the user pressed cancel.

        Example::

            ..
            if (pDialog.iscanceled()): return
            ..
        """
        return True
    

class DialogBusy(object):
    """
    Kodi's busy dialog class

      New class added.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self):
        # type: () -> None
        """
        Create and show a busy dialog.

        Use update() to update the progressbar.

        New method added

        Example::

            ..
            dialog = xbmcgui.DialogBusy()
            dialog.create()
            ..
        """
        pass
    
    def update(self, percent):
        # f(int) -> None
        """
        Updates the busy dialog.

        :param percent: integer - percent complete. (-1:100)

        If percent == -1 (default), the progressbar will be hidden.

        New method added
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the progress dialog.

        New method added
        """
        pass
    
    def iscanceled(self):
        # f() -> bool
        """
        Checks if busy dialog is canceled.

        :return: True if the user pressed cancel.

        New method added
        """
        return True
    

class DialogProgressBG(object):
    """
    Kodi's background progress dialog class
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def create(self, heading, message=""):
        # type: (str_type, str_type) -> None
        """
        Create and show a background progress dialog.

        :param heading: string or unicode - dialog heading. 
        :param message: [opt] string or unicode - message text.

        'heading' is used for the dialog's id. Use a unique heading.
        Use update() to update heading, message and progressbar.

        Example::

            ..
            pDialog = xbmcgui.DialogProgressBG()
            pDialog.create('Movie Trailers', 'Downloading Monsters Inc... .')
            ..
        """
        pass
    
    def update(self, percent=0, heading="", message=""):
        # type: (int, str_type, str_type) -> None
        """
        Updates the background progress dialog.

        :param percent: [opt] integer - percent complete. (0:100) 
        :param heading: [opt] string or unicode - dialog heading. 
        :param message: [opt] string or unicode - message text.

        To clear heading or message, you must pass a blank character.

        Example::

            ..
            pDialog.update(25, message='Downloading Finding Nemo ...')
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Close the background progress dialog

        Example::

            ..
            pDialog.close()
            ..
        """
        pass
    
    def isFinished(self):
        # type: () -> bool
        """
        Checks progress is finished

        :return: True if the background dialog is active.

        Example::

            ..
            if (pDialog.isFinished()): return
            ..
        """
        return True
    

class ListItem(object):
    """
    Selectable window list item

    The list item control is used for creating item lists in Kodi

    :param label: [opt] string 
    :param label2: [opt] string 
    :param iconImage: **Deprecated. Use setArt**
    :param thumbnailImage: **Deprecated. Use setArt**
    :param path: [opt] string

    .. note::
        **iconImage** and **thumbnailImage** are deprecated. Use **setArt()**.

    Example::

        ...
        listitem = xbmcgui.ListItem('Casino Royale')
        ...
    """
    
    def __init__(self, label="", label2="", iconImage="", thumbnailImage="", path=""):
        # type: (str_type, str_type, str_type, str_type, str_type) -> None
        pass
    
    def getLabel(self):
        # type: () -> str
        """
        Returns the listitem label. 

        :return: Label of item

        Example::

            ...
            # getLabel()
            label = listitem.getLabel()
            ...
        """
        return ""
    
    def getLabel2(self):
        # type: () -> str
        """
        Returns the second listitem label. 

        :return: Second label of item

        Example::

            ...
            # getLabel2()
            label = listitem.getLabel2()
            ...
        """
        return ""
    
    def setLabel(self, label):
        # type: (str_type) -> None
        """
        Sets the listitem's label. 

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel(label)
            listitem.setLabel('Casino Royale')
            ...
        """
        pass
    
    def setLabel2(self, label):
        # type: (str_type) -> None
        """
        Sets the listitem's label2. 

        :param label: string or unicode - text string.

        Example::

            ...
            # setLabel2(label)
            listitem.setLabel2('Casino Royale')
            ...
        """
        pass
    
    def setIconImage(self, iconImage):
        # type: (str_type) -> None
        """
        Deprecated. Use **setArt()**. 


        """
        pass
    
    def setThumbnailImage(self, thumbFilename):
        # type: (str_type) -> None
        """
        .. warning:: Deprecated. Use **setArt()**.
        """
        pass
    
    def setArt(self, dictionary):
        # type: (Dict[str, str_type]) -> None
        """
        Sets the listitem's art 

        :param values: dictionary - pairs of  ``label: value``.
            Some default art values (any string possible):

        ==========  ========================
        Label       Type                    
        ==========  ========================
        thumb       string - image filename 
        poster      string - image filename 
        banner      string - image filename 
        fanart      string - image filename 
        clearart    string - image filename 
        clearlogo   string - image filename 
        landscape   string - image filename 
        icon        string - image filename 
        ==========  ========================

        New function added.  Added new label **icon**.

        Example::

            ...
            # setArt(values)
            listitem.setArt(``'poster': 'poster.png', 'banner' : 'banner.png'``)
            ...
        """
        pass
    
    def setUniqueIDs(self, dictionary):
        # type: (Dict[str, str_type]) -> None
        """
        Sets the listitem's uniqueID 

        :param values: dictionary - pairs of  ``label: value``.
            Some example values (any string possible):

        ======  =======================
        Label   Type                   
        ======  =======================
        imdb    string - uniqueid name 
        tvdb    string - uniqueid name 
        tmdb    string - uniqueid name 
        anidb   string - uniqueid name 
        ======  =======================

        Example::

            ...
            # setUniqueIDs(values)
            listitem.setUniqueIDs(``'imdb': 'tt8938399', 'tmdb' : '9837493'``)
            ...
        """
        pass
    
    def setRating(self, type, rating, votes=0, defaultt=False):
        # type: (str_type, float, int, bool) -> None
        """
        Sets a listitem's rating. It needs at least type and rating param 

        :param type: string - the type of the rating. Any string. 
        :param rating: float - the value of the rating. 
        :param votes: int - the number of votes. Default 0. 
        :param defaultt: bool - is the default rating?. Default False.
            Some example type (any string possible):

        ======  =====================
        Label   Type                 
        ======  =====================
        imdb    string - rating type 
        tvdb    string - rating type 
        tmdb    string - rating type 
        anidb   string - rating type 
        ======  =====================

        Example::

            ...
            # setRating(type, rating, votes, defaultt))
            listitem.setRating("imdb", 4.6, 8940, True)
            ...
        """
        pass
    
    def getArt(self, key):
        # type: (str) -> str
        """
        Returns a listitem art path as a string, similar to an infolabel.

        :param key: string - art name.Some default art values (any string possible):

        ==========  ====================
        Label       Type                
        ==========  ====================
        thumb       string - image path 
        poster      string - image path 
        banner      string - image path 
        fanart      string - image path 
        clearart    string - image path 
        clearlogo   string - image path 
        landscape   string - image path 
        icon        string - image path 
        ==========  ====================

        New function added.


        Example::

            ...
            poster = listitem.getArt('poster')
            ...
        """
        return ""
    
    def getUniqueID(self, key):
        # type: (str) -> str
        """
        Returns a listitem uniqueID as a string, similar to an infolabel.

        :param key: string - uniqueID name.Some default uniqueID values
            (any string possible):

        ======  =======================
        Label   Type                   
        ======  =======================
        imdb    string - uniqueid name 
        tvdb    string - uniqueid name 
        tmdb    string - uniqueid name 
        anidb   string - uniqueid name 
        ======  =======================

        Example::

            ...
            uniqueID = listitem.getUniqueID('imdb')
            ...
        """
        return ""
    
    def getRating(self, key):
        # type: (str) -> float
        """
        Returns a listitem rating as a float.

        :param key: string - rating type.Some default key values
            (any string possible):

        ======  ===================
        Label   Type               
        ======  ===================
        imdb    string - type name 
        tvdb    string - type name 
        tmdb    string - type name 
        anidb   string - type name 
        ======  ===================

        Example::

            ...
            rating = listitem.getRating('imdb')
            ...
        """
        return 0.0
    
    def getVotes(self, key):
        # type: (str) -> int
        """
        Returns a listitem votes as a integer.

        :param key: string - rating type.Some default key values
            (any string possible):

        ======  ===================
        Label   Type               
        ======  ===================
        imdb    string - type name 
        tvdb    string - type name 
        tmdb    string - type name 
        anidb   string - type name 
        ======  ===================

        Example::

            ...
            votes = listitem.getVotes('imdb')
            ...
        """
        return 0
    
    def select(self, selected):
        # type: (bool) -> None
        """
        Sets the listitem's selected status. 

        :param selected: bool - True=selected/False=not selected

        Example::

            ...
            # select(selected)
            listitem.select(True)
            ...
        """
        pass
    
    def isSelected(self):
        # type: () -> bool
        """
        Returns the listitem's selected status. 

        :return: bool - true if selected, otherwise false

        Example::

            ...
            # isSelected()
            selected = listitem.isSelected()
            ...
        """
        return True
    
    def setInfo(self, type, infoLabels):
        # type: (str, Dict[str, str_type]) -> None
        """
        Sets the listitem's infoLabels. 

        :param type: string - type of 
        :param infoLabels: dictionary - pairs of  ``label: value``

        **Available types**

        =============  ======================
        Command name   Description           
        =============  ======================
        video          Video information     
        music          Music information     
        pictures       Pictures informantion 
        =============  ======================

        To set pictures exif info, prepend  ``exif:`` to the label.
        Exif values must be passed as strings, separate value pairs with
        a comma. **(eg.  ``{'exif:resolution': '720,480'}``**
        See kodi_pictures_infotag for valid strings. You can use the above
        as keywords for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.

        **General Values** (that apply to all types):

        ===========  ===========================================================
        Info label   Description                                                                  
        ===========  ===========================================================
        count        integer (12) - can be used to store an id for later,
                     or for sorting purposes
        size         long (1024) - size in bytes                                                  
        date         string (d.m.Y / 01.01.2009) - file date                                      
        ===========  ===========================================================

        **Video Values**:

        ==============  ========================================================
        Info label      Description                                                                                                           
        ==============  ========================================================
        genre           string (Comedy)                                                                                                       
        country         string (Germany)                                                                                                      
        year            integer (2009)                                                                                                        
        episode         integer (4)                                                                                                           
        season          integer (1)                                                                                                           
        top250          integer (192)                                                                                                         
        setid           integer (14)                                                                                                          
        tracknumber     integer (3)                                                                                                           
        rating          float (6.4) - range is 0..10                                                                                          
        userrating      integer (9) - range is 1..10 (0 to reset)                                                                             
        watched         depreciated - use playcount instead                                                                                   
        playcount       integer (2) - number of times this item has been played                                                               
        overlay         integer (2) - range is                                                                                                  0..7  . See Overlay icon types for values 
        cast            list (["Michal C. Hall","Jennifer Carpenter"]) -
                        if provided a list of tuples cast will be interpreted
                        as castandrole
        castandrole     list of tuples ([("Michael C. Hall","Dexter"),
                        ("Jennifer Carpenter","Debra")])
        director        string (Dagur Kari)                                                                                                   
        mpaa            string (PG-13)                                                                                                        
        plot            string (Long Description)                                                                                             
        plotoutline     string (Short Description)                                                                                            
        title           string (Big Fan)                                                                                                      
        originaltitle   string (Big Fan)                                                                                                      
        sorttitle       string (Big Fan)                                                                                                      
        duration        integer (245) - duration in seconds                                                                                   
        studio          string (Warner Bros.)                                                                                                 
        tagline         string (An awesome movie) - short description of movie                                                                
        writer          string (Robert D. Siegel)                                                                                             
        tvshowtitle     string (Heroes)                                                                                                       
        premiered       string (2005-03-04)                                                                                                   
        status          string (Continuing) - status of a TVshow                                                                              
        set             string (Batman Collection) - name of the collection                                                                   
        imdbnumber      string (tt0110293) - IMDb code                                                                                        
        code            string (101) - Production code                                                                                        
        aired           string (2008-12-07)                                                                                                   
        credits         string (Andy Kaufman) - writing credits                                                                               
        lastplayed      string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        album           string (The Joshua Tree)                                                                                              
        artist          list (['U2'])                                                                                                         
        votes           string (12345 votes)                                                                                                  
        path            string (/home/user/movie.avi)                                                                                         
        trailer         string (/home/user/trailer.avi)                                                                                       
        dateadded       string (Y-m-d h:m:s = 2009-04-05 23:16:04)                                                                            
        mediatype       string - "video", "movie", "tvshow", "season", "episode"
                        or "musicvideo"
        dbid            integer (23) - Only add this for items which are part
                        of the local db. You also need to set the correct 'mediatype'!
        ==============  ========================================================

        **Music Values**:

        =========================  =============================================
        Info label                 Description                                             
        =========================  =============================================
        tracknumber                integer (8)                                             
        discnumber                 integer (2)                                             
        duration                   integer (245) - duration in seconds                     
        year                       integer (1998)                                          
        genre                      string (Rock)                                           
        album                      string (Pulse)                                          
        artist                     string (Muse)                                           
        title                      string (American Pie)                                   
        rating                     float - range is between 0 and 10                       
        userrating                 integer - range is 1..10                                
        lyrics                     string (On a dark desert highway...)                    
        playcount                  integer (2) - number of times this item has
                                   been played
        lastplayed                 string (Y-m-d h:m:s = 2009-04-05 23:16:04)              
        mediatype                  string - "music", "song", "album", "artist"             
        listeners                  integer (25614)                                         
        musicbrainztrackid         string (cd1de9af-0b71-4503-9f96-9f5efe27923c)           
        musicbrainzartistid        string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)           
        musicbrainzalbumid         string (24944755-2f68-3778-974e-f572a9e30108)           
        musicbrainzalbumartistid   string (d87e52c5-bb8d-4da8-b941-9f4928627dc8)           
        comment                    string (This is a great song)                           
        =========================  =============================================

        **Picture Values**:

        ============  =====================================================
        Info label    Description                                          
        ============  =====================================================
        title         string (In the last summer-1)                        
        picturepath   string (/home/username/pictures/img001.jpg  )
        exif*         string (See kodi_pictures_infotag for valid strings) 
        ============  =====================================================

        Added new label **discnumber**.  **duration** has to be set in seconds.
        Added new label **mediatype**.
        Added labels **setid**, **set**, **imdbnumber**, **code**, **dbid**,
        **path** and **userrating**.
        Expanded the possible infoLabels for the option **mediatype**.

        Example::

            ...
            listitem.setInfo('video', ``'genre': 'Comedy'``)
            ...
        """
        pass
    
    def setCast(self, actors):
        # type: (List[Dict[str, str_type]]) -> None
        """
        Set cast including thumbnails

        :param actors: list of dictionaries (see below for relevant keys)

        Keys:

        ==========  =========================
        Label       Description              
        ==========  =========================
        name        string (Michael C. Hall) 
        role        string (Dexter)          
        thumbnail   string (http://www.someurl.com/someimage.png  )
        order       integer (1)              
        ==========  =========================

        New function added.

        Example::

            ...
            actors = [{"name": "Actor 1", "role": "role 1"},
                      {"name": "Actor 2", "role": "role 2"}]
            listitem.setCast(actors)
            ...
        """
        pass
    
    def addStreamInfo(self, cType, dictionary):
        # type: (str, Dict[str, str_type]) -> None
        """
        Add a stream with details.

        :param type: string - type of stream(video/audio/subtitle). 
        :param values: dictionary - pairs of ``label: value``.

        Video Values:

        =========  ==================
        Label      Description       
        =========  ==================
        codec      string (h264)     
        aspect     float (1.78)      
        width      integer (1280)    
        height     integer (720)     
        duration   integer (seconds) 
        =========  ==================

        Audio Values:

        =========  =============
        Label      Description  
        =========  =============
        codec      string (dts) 
        language   string (en)  
        channels   integer (2)  
        =========  =============

        Subtitle Values:

        =========  =============
        Label      Description  
        =========  =============
        language   string (en)  
        =========  =============

        Example::

            ...
            listitem.addStreamInfo('video', ``'codec': 'h264', 'width' : 1280``)
            ...
        """
        pass
    
    def addContextMenuItems(self, items, replaceItems=False):
        # type: (List[Tuple[str_type, str_type]], bool) -> None
        """
        Adds item(s) to the context menu for media lists. 

        :param items: list - [(label, action,)*] A list of tuples consisting
            of label and action pairs.

        * label [string or unicode] - item's label
        * action [string or unicode] - any built-in function to perform.

        List of functions - http://kodi.wiki/view/List_of_Built_In_Functions

        You can use the above as keywords for arguments and skip certain optional
        arguments. Once you use a keyword, all following arguments require
        the keyword.

        Completely removed option **replaceItems**.

        Example::

            ...
            listitem.addContextMenuItems(
                [('Theater Showtimes',
                'RunScript(special://home/scripts/showtimes/default.py,Iron Man)',)]
                )
            ...
        """
        pass
    
    def setProperty(self, key, value):
        # type: (str, str_type) -> None
        """
        Sets a listitem property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. You can use the above as keywords
        for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.
        Some of these are treated internally by Kodi, such as the 'StartOffset'
        property, which is the offset in seconds at which to start playback of
        an item. Others may be used in the skin to add extra information,
        such as 'WatchedCount' for tvshow items

        Example::

            ...
            listitem.setProperty('AspectRatio', '1.85 : 1')
            listitem.setProperty('StartOffset', '256.4')
            ...
        """
        pass
    
    def getProperty(self, key):
        # type: (str) -> str
        """
        Returns a listitem property as a string, similar to an infolabel. 

        :param key: string - property name.

        Key is NOT case sensitive. You can use the above as keywords
        for arguments and skip certain optional arguments. Once you use
        a keyword, all following arguments require the keyword.

        Example::

            ...
            AspectRatio = listitem.getProperty('AspectRatio')
            ...
        """
        return ""
    
    def setPath(self, path):
        # type: (str_type) -> None
        """
        Sets the listitem's path. 

        :param path: string or unicode - path, activated when item is clicked.

        You can use the above as keywords for arguments.

        Example::

            ...
            listitem.setPath(path='/path/to/some/file.ext')
            ...
        """
        pass
    
    def setMimeType(self, mimetype):
        # type: (str_type) -> None
        """
        Sets the listitem's mimetype if known. 

        :param mimetype: string or unicode - mimetype

        If known prehand, this can (but does not have to) avoid HEAD requests
        being sent to HTTP servers to figure out file type.
        """
        pass
    
    def setContentLookup(self, enable):
        # type: (bool) -> None
        """
        Enable or disable content lookup for item. 

        If disabled, HEAD requests to e.g determine mime type will not be sent.

        enable bool to enable content lookup 

        New function added. 
        """
        pass
    
    def setSubtitles(self, subtitleFiles):
        # type: (List[str_type]) -> None
        """
        Sets subtitles for this listitem. 

        :param subtitleFiles: list with path to subtitle files

        Example::

            ...
            listitem.setSubtitles(['special://temp/example.srt', 'http://example.com/example.srt'])
            ...
          New function added. 
        """
        pass
    
    def getdescription(self):
        # type: () -> str
        """
        .. warning:: Deprecated.
        """
        return ""
    
    def getduration(self):
        # type: () -> str
        """
        .. warning:: Deprecated. Use **InfoTagMusic**.
        """
        return ""
    
    def getfilename(self):
        # type: () -> str
        """
        .. warning:: Deprecated.
        """
        return ""
    
    def getPath(self):
        # type: () -> str
        """
        Returns the path of this listitem. 

        [string] filename 

        New function added. 
        """
        return ""
    
    def getVideoInfoTag(self):
        # type: () -> InfoTagVideo
        """
        Returns the VideoInfoTag for this item. 

        video info tag 

        New function added. 
        """
        return InfoTagVideo()
    
    def getMusicInfoTag(self):
        # type: () -> InfoTagMusic
        """
        Returns the MusicInfoTag for this item. 

        music info tag 

        New function added. 
        """
        return InfoTagMusic()
    

class Action(object):
    """
    Action class

    ``xbmcgui.Action():``

    This class serves in addition to identify carried out kodi_key_action_ids
    of Kodi and to be able to carry out thereby own necessary steps.

    The data of this class are always transmitted by callback
    Window::onAction at a window.
    """
    
    def __init__(self):
        # type: () -> None
        pass
    
    def getId(self):
        # type: () -> long
        """
        To get kodi_key_action_ids 

        This function returns the identification code used by the explained order,
        it is necessary to determine the type of command from kodi_key_action_ids.

        :return: The action's current id as a long or 0 if no action is mapped in the xml's.

        Example::

            ..
            def onAction(self, action):
                if action.getId() == ACTION_PREVIOUS_MENU:
                    print('action recieved: previous')
            ..
        """
        return 0
    
    def getButtonCode(self):
        # type: () -> long
        """
        Returns the button code for this action. 

        :return: [integer] button code 
        """
        return 0
    
    def getAmount1(self):
        # type: () -> float
        """
        Returns the first amount of force applied to the thumbstick. 

        :return: [float] first amount 
        """
        return 0.0
    
    def getAmount2(self):
        # type: () -> float
        """
        Returns the second amount of force applied to the thumbstick. 

        :return: [float] second amount 
        """
        return 0.0
    

class Window(object):
    """
    GUI window class for Add-Ons

    This class allows over their functions to create and edit windows that
    can be accessed from an Add-On.

    Likewise, all functions from here as well in the other window classes
    WindowDialog, WindowXML and WindowXMLDialog with inserted and available.

    Constructor for window 

    ``xbmcgui.Window([existingWindowId]):``

    Creates a new from Add-On usable window class. This is to create window
    for related controls by system calls.

    :param existingWindowId: [opt] Specify an id to use an existing window. 
    :raises ValueError: if supplied window Id does not exist. 
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        win = xbmcgui.Window()
        width = win.getWidth()
        ..
    """
    
    def __init__(self, existingWindowId=-1):
        # type: (int) -> None
        pass
    
    def show(self):
        # type: () -> None
        """
        Show this window. 

        Shows this window by activating it, calling close() after it wil
        activate the current window again.

        If your script ends this window will be closed to. To show it forever,
        make a loop at the end of your script or use doModal() instead.
        """
        pass
    
    def setFocus(self, pControl):
        # type: (Control) -> None
        """
        Give the supplied control focus. 

        :param Control: Control class to focus 
        :raises TypeError: If supplied argument is not a Control type 
        :raises SystemError: On Internal error
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def setFocusId(self, iControlId):
        # type: (int) -> None
        """
        Gives the control with the supplied focus. 

        :param ControlId: [integer] On skin defined id of control 
        :raises SystemError: On Internal error 
        :raises RuntimeError: If control is not added to a window
        """
        pass
    
    def getFocus(self):
        # type: () -> Control
        """
        Returns the control which is focused. 

        :return: Focused control class
        :raises SystemError: On Internal error 
        :raises RuntimeError: If no control has focus
        """
        return Control()
    
    def getFocusId(self):
        # type: () -> long
        """
        Returns the id of the control which is focused. 

        :return: Focused control id
        :raises SystemError: On Internal error 
        :raises RuntimeError: If no control has focus
        """
        return 0
    
    def removeControl(self, pControl):
        # type: (Control) -> None
        """
        Removes the control from this window. 

        :param Control: Control class to remove 
        :raises TypeError: If supplied argument is not a Control type 
        :raises RuntimeError: If control is not added to this window

        This will not delete the control. It is only removed from the window. 
        """
        pass
    
    def removeControls(self, pControls):
        # type: (List[Control]) -> None
        """
        Removes a list of controls from this window. 

        :param List: List with controls to remove 
        :raises TypeError: If supplied argument is not a Control type 
        :raises RuntimeError: If control is not added to this window

        This will not delete the controls. They are only removed from the window. 
        """
        pass
    
    def getHeight(self):
        # type: () -> long
        """
        Returns the height of this screen. 

        :return: Screen height 
        """
        return 0
    
    def getWidth(self):
        # type: () -> long
        """
        Returns the width of this screen. 

        :return: Screen width 
        """
        return 0
    
    def getResolution(self):
        # type: () -> long
        """
        Returns The resolution of the screen 

        :return: Used Resolution The returned value is one of the following:

        ======  =====================
        value   Resolution           
        ======  =====================
        0       1080i (1920x1080)    
        1       720p (1280x720)      
        2       480p 4:3 (720x480)   
        3       480p 16:9 (720x480)  
        4       NTSC 4:3 (720x480)   
        5       NTSC 16:9 (720x480)  
        6       PAL 4:3 (720x576)    
        7       PAL 16:9 (720x576)   
        8       PAL60 4:3 (720x480)  
        9       PAL60 16:9 (720x480) 
        ======  =====================
        """
        return 0
    
    def setCoordinateResolution(self, res):
        # type: (int_type) -> None
        """
        Sets the resolution 

        That the coordinates of all controls are defined in. Allows Kodi
        to scale control positions and width/heights to whatever resolution
        Kodi is currently using.

        :param res: Coordinate resolution to set Resolution is one of the following:

        ======  =====================
        value   Resolution           
        ======  =====================
        0       1080i (1920x1080)    
        1       720p (1280x720)      
        2       480p 4:3 (720x480)   
        3       480p 16:9 (720x480)  
        4       NTSC 4:3 (720x480)   
        5       NTSC 16:9 (720x480)  
        6       PAL 4:3 (720x576)    
        7       PAL 16:9 (720x576)   
        8       PAL60 4:3 (720x480)  
        9       PAL60 16:9 (720x480) 
        ======  =====================

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.setCoordinateResolution(0)
            ..
        """
        pass
    
    def setProperty(self, key, value):
        # type: (str, str_type) -> None
        """
        Sets a window property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. Setting value to an empty string is equivalent
        to clearProperty(key). You can use the above as keywords for arguments
        and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.setProperty('Category', 'Newest')
            ..
        """
        pass
    
    def getProperty(self, key):
        # type: (str) -> str
        """
        Returns a window property as a string, similar to an infolabel. 

        :param key: string - property name.

        Key is NOT case sensitive. You can use the above as keywords for
        arguments and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            category = win.getProperty('Category')
            ..
        """
        return ""
    
    def clearProperty(self, key):
        # type: (str) -> None
        """
        Clears the specific window property. 

        :param key: string - property name.

        Key is NOT case sensitive. Equivalent to setProperty(key,''). You can use
        the above as keywords for arguments and skip certain optional arguments.
        Once you use a keyword, all following arguments require the keyword.

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperty('Category')
            ..
        """
        pass
    
    def clearProperties(self):
        # type: () -> None
        """
        Clears all window properties. 

        Example::

            ..
            win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
            win.clearProperties()
            ..
        """
        pass
    
    def close(self):
        # type: () -> None
        """
        Closes this window. 

        Closes this window by activating the old window.

        The window is not deleted with this method. 
        """
        pass
    
    def doModal(self):
        # type: () -> None
        """
        Display this window until close() is called.
        """
        pass
    
    def addControl(self, pControl):
        # type: (Control) -> None
        """
        Add a Control to this window. 

        :param Control: Control to add 
        :raises TypeError: If supplied argument is not a Control type 
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)

        The next controls can be added to a window atm

        ==================  =============
        Control-class       Description  
        ==================  =============
        ControlLabel        Label control to show text
        ControlFadeLabel    The fadelabel has multiple labels which it cycles through
        ControlTextBox      To show bigger text field
        ControlButton       Brings a button to do some actions
        ControlEdit         The edit control allows a user to input text in Kodi
        ControlFadeLabel    The fade label control is used for displaying
                            multiple pieces of text in the same space in Kodi
        ControlList         Add a list for something like files
        ControlGroup        Is for a group which brings the others together
        ControlImage        Controls a image on skin
        ControlRadioButton  For a radio button which handle boolean values
        ControlProgress     Progress bar for a performed work or something else
        ControlSlider       The slider control is used for things where
                            a sliding bar best represents the operation at hand
        ControlSpin         The spin control is used for when a list of options
                            can be chosen
        ControlTextBox      The text box is used for showing a large multipage
                            piece of text in Kodi
        ==================  =============
        """
        pass
    
    def addControls(self, pControls):
        # type: (List[Control]) -> None
        """
        Add a list of Controls to this window. 

        :param List: List with controls to add 
        :raises TypeError: If supplied argument is not of List type,
            or a control is not of Control type
        :raises ReferenceError: If control is already used in another window
        :raises RuntimeError: Should not happen :-)
        """
        pass
    
    def getControl(self, iControlId):
        # type: (int) -> Control
        """
        Gets the control from this window. 

        :param controlId: Control id to get 
        :raises Exception: If Control doesn't exist

        controlId doesn't have to be a python control, it can be a control
        id from a Kodi window too (you can find id's in the xml files.

        Not python controls are not completely usable yet You can only use
        the Control functions
        """
        return Control()
    

class WindowDialog(Window):
    """
    GUI window dialog class for Add-Ons

    ``xbmcgui.WindowDialog(int windowId):``

    Creates a new window from Add-On usable dialog class. This is to create
    window for related controls by system calls.

    :param windowId: [opt] Specify an id to use an existing window. 
    :raises ValueError: if supplied window Id does not exist. 
    :raises Exception: if more then 200 windows are created.

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        dialog = xbmcgui.WindowDialog()
        width = dialog.getWidth()
        ..
    """
    
    def __init__(self):
        # type: () -> None
        pass
    

class WindowXML(Window):
    """
    GUI xml window class

    Creates a new xml file based window class.

    This class include also all calls from ``Window``.

    :param xmlFilename: string - the name of the xml file to look for. 
    :param scriptPath: string - path to script. used to fallback to if the xml
        doesn't exist in the current skin.
        (eg xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
    :param defaultSkin: [opt] string - name of the folder in the skins path
        to look in for the xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution. (default='720p') 
    :raises Exception: if more then 200 windows are created.

    Skin folder structure is e.g. **resources/skins/Default/720p**

    Deleting this window will activate the old window that was active and resets
    (not delete) all controls that are associated with this window.

    Example::

        ..
        win = xbmcgui.WindowXML('script-Lyrics-main.xml',
                xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'),
                'default', '1080p')
        win.doModal()
        del win
        ..

    On functions defined input variable **
    ``controlId`` (GUI control identifier)** is the on window.xml defined value
    behind type added with  ``**id="..."**`` and used to identify for changes
    there and on callbacks.

    .. code-block:: xml

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename, scriptPath, defaultSkin="Default",
                 defaultRes="720p"):
        # type: (str_type, str_type, str_type, str_type) -> None
        pass
    
    def addItem(self, item, position=INT_MAX):
        # type: (Union[str_type, ListItem], int) -> None
        """
        Add a new item to this WindowList. 

        :param item: string, unicode or ListItem - item to add. 
        :param position: [opt] integer - position of item to add.
            (NO Int = Adds to bottom,0 adds to top, 1 adds to one below from top,
            -1 adds to one above from bottom etc etc ). If integer positions are
            greater than list size, negative positions will add to top of list,
            positive positions will add to bottom of list

        Example::

            ..
            self.addItem('Reboot Kodi', 0)
            ..
        """
        pass
    
    def addItems(self, items):
        # type: (List[Union[str_type, ListItem]]) -> None
        """
        Add a list of items to to the window list. 

        :param items: List - list of strings, unicode objects or ListItems to add.

        Example::

            ..
            self.addItems(['Reboot Kodi', 'Restart Kodi'])
            ..
        """
        pass
    
    def removeItem(self, position):
        # type: (int) -> None
        """
        Removes a specified item based on position, from the WindowList. 

        :param position: integer - position of item to remove.

        Example::

            ..
            self.removeItem(5)
            ..
        """
        pass
    
    def getCurrentListPosition(self):
        # type: () -> int
        """
        Gets the current position in the WindowList.

        Example::

            ..
            pos = self.getCurrentListPosition()
            ..
        """
        return 0
    
    def setCurrentListPosition(self, position):
        # type: (int) -> None
        """
        Set the current position in the WindowList. 

        :param position: integer - position of item to set.

        Example::

            ..
            self.setCurrentListPosition(5)
            ..
        """
        pass
    
    def getListItem(self, position):
        # type: (int) -> ListItem
        """
        Returns a given ListItem in this WindowList. 

        :param position: integer - position of item to return.

        Example::

            ..
            listitem = self.getListItem(6)
            ..
        """
        return ListItem()
    
    def getListSize(self):
        # type: () -> int
        """
        Returns the number of items in this WindowList.

        Example::

            ..
            listSize = self.getListSize()
            ..
        """
        return 0
    
    def clearList(self):
        # type: () -> None
        """
        Clear the WindowList. 

        Example::

            ..
            self.clearList()
            ..
        """
        pass
    
    def setContainerProperty(self, strProperty, strValue):
        # type: (str_type, str_type) -> None
        """
        Sets a container property, similar to an infolabel. 

        :param key: string - property name. 
        :param value: string or unicode - value of property.

        Key is NOT case sensitive. You can use the above as keywords for arguments
        and skip certain optional arguments. Once you use a keyword,
        all following arguments require the keyword.

        Changed function from **setProperty** to **setContainerProperty**.

        Example::

            ..
            self.setContainerProperty('Category', 'Newest')
            ..
        """
        pass
    
    def getCurrentContainerId(self):
        # type: () -> int
        """
        Get the id of the currently visible container. 

        Added new function.

        Example::

            ..
            container_id = self.getCurrentContainerId()
            ..
        """
        return 0
    

class WindowXMLDialog(WindowXML):
    """
    GUI xml window dialog

    Creates a new xml file based window dialog class.

    :param xmlFilename: string - the name of the xml file to look for. 
    :param scriptPath: string - path to script. used to fallback to if the xml
        doesn't exist in the current skin.
        (eg xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'))
    :param defaultSkin: [opt] string - name of the folder in the skins path
        to look in for the xml. (default='Default')
    :param defaultRes: [opt] string - default skins resolution.
        (default='720p')
    :raises Exception: if more then 200 windows are created.

    Skin folder structure is e.g. **resources/skins/Default/720p**

    Example::

        ..
        dialog = xbmcgui.WindowXMLDialog('script-Lyrics-main.xml',
            xbmcaddon.Addon().getAddonInfo('path').decode('utf-8'),
            'default', '1080p')
        dialog.doModal()
        del dialog
        ..

    On functions defined input variable ** ``controlId``
    (GUI control identifier)** is the on window.xml defined value behind type
    added with  ``**id="..."**`` and used to identify for changes there and
    on callbacks.

    .. code-block:: xml

        <control type="label" id="31">
          <description>Title Label</description>
          ...
        </control>
        <control type="progress" id="32">
          <description>progress control</description>
          ...
        </control>
    """
    
    def __init__(self, xmlFilename, scriptPath, defaultSkin="Default", defaultRes="720p"):
        # type: (str_type, str_type, str_type, str_type) -> None
        pass
    

def getCurrentWindowId():
    # type: () -> long
    """
    Returns the id for the current 'active' window as an integer. 

    :return: The currently active window Id

    Example::

        ..
        wid = xbmcgui.getCurrentWindowId()
        ..
    """
    return 0


def getCurrentWindowDialogId():
    # type: () -> long
    """
    Returns the id for the current 'active' dialog as an integer. 

    :return: The currently active dialog Id

    Example::

        ..
        wid = xbmcgui.getCurrentWindowDialogId()
        ..
    """
    return 0
