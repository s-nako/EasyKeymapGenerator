from . import util

MAP_TYPES = util.Bidict({
    "Keyboard": "KEYBOARD", "Tweak": "TWEAK", "Mouse": "MOUSE", "NDOF": "NDOF", "Text Input": "TEXTINPUT",
    "Timer": "TIMER"
})

# values for Keyboard, Mouse, NDOF
CLICK_VALUES = util.Bidict({
    "Press": "PRESS", "Any": "ANY", "Release": "RELEASE", "Click": "CLICK", "Double Click": "DOUBLE_CLICK",
    "Click Drag": "CLICK_DRAG", "Nothing": "NOTHING"
})

TWEAK_VALUES = util.Bidict({
    "Any": "ANY", "North": "NORTH", "North-East": "NORTH_EAST", "East": "EAST", "South-East": "SOUTH_EAST",
    "South": "SOUTH", "South-West": "SOUTH_WEST", "West": "WEST", "North-West": "NORTH_WEST"
})

TWEAK_TYPES = util.Bidict({
    "Left": "EVT_TWEAK_L", "Middle": "EVT_TWEAK_M", "Right": "EVT_TWEAK_R"
})

MOUSE_TYPES = util.Bidict({
    "Left": "LEFTMOUSE", "Middle": "MIDDLEMOUSE", "Right": "RIGHTMOUSE", "Button4": "BUTTON4MOUSE",
    "Button5": "BUTTON5MOUSE", "Button6": "BUTTON6MOUSE", "Button7": "BUTTON7MOUSE", "Pen": "PEN",
    "Eraser": "ERASER",
    "Move": "MOUSEMOVE", "Mouse/Trackpad Pan": "TRACKPADPAN", "Mouse/Trackpad Zoom": "TRACKPADZOOM",
    "Mouse/Trackpad Rotate": "MOUSEROTATE", "Mouse/Trackpad Smart Zoom": "MOUSESMARTZOOM",
    "Wheel Up": "WHEELUPMOUSE",
    "Wheel Down": "WHEELDOWNMOUSE", "Wheel In": "WHEELINMOUSE", "Wheel Out": "WHEELOUTMOUSE"
})

TIMER_TYPES = util.Bidict({
    "Timer": "TIMER", "Timer 0": "TIMER0", "Timer 1": "TIMER1", "Timer 2": "TIMER2", "Timer Jobs": "TIMER_JOBS",
    "Timer Autosave": "TIMER_AUTOSAVE", "Timer Report": "TIMER_REPORT", "Timer Region": "TIMERREGION"
})

NDOF_TYPES = util.Bidict({
    "Motion": "NDOF_MOTION", "Menu": "NDOF_BUTTON_MENU", "Fit": "NDOF_BUTTON_FIT", "Top": "NDOF_BUTTON_TOP",
    "Bottom": "NDOF_BUTTON_BOTTOM", "Left": "NDOF_BUTTON_LEFT", "Right": "NDOF_BUTTON_RIGHT",
    "Front": "NDOF_BUTTON_FRONT", "Back": "NDOF_BUTTON_BACK", "Isometric 1": "NDOF_BUTTON_ISO1",
    "Isometric 2": "NDOF_BUTTON_ISO2", "Roll CW": "NDOF_BUTTON_ROLL_CW", "Roll CCW": "NDOF_BUTTON_ROLL_CCW",
    "Spin CW": "NDOF_BUTTON_SPIN_CW NDOF", "Spin CCW": "NDOF_BUTTON_SPIN_CCW", "Tilt CW": "NDOF_BUTTON_TILT_CW",
    "Tilt CCW": "NDOF_BUTTON_TILT_CCW", "Rotate": "NDOF_BUTTON_ROTATE", "Pan/Zoom": "NDOF_BUTTON_PANZOOM",
    "Dominant": "NDOF_BUTTON_DOMINANT", "Plus": "NDOF_BUTTON_PLUS", "Minus": "NDOF_BUTTON_MINUS",
    "Esc": "NDOF_BUTTON_ESC", "Alt": "NDOF_BUTTON_ALT", "Shift": "NDOF_BUTTON_SHIFT",
    "Ctrl": "NDOF_BUTTON_CTRL",
    "Button 1": "NDOF_BUTTON_1", "Button 2": "NDOF_BUTTON_2", "Button 3": "NDOF_BUTTON_3",
    "Button 4": "NDOF_BUTTON_4",
    "Button 5": "NDOF_BUTTON_5", "Button 6": "NDOF_BUTTON_6", "Button 7": "NDOF_BUTTON_7",
    "Button 8": "NDOF_BUTTON_8",
    "Button 9": "NDOF_BUTTON_9", "Button 10": "NDOF_BUTTON_10", "Button A": "NDOF_BUTTON_A",
    "Button B": "NDOF_BUTTON_B", "Button C": "NDOF_BUTTON_C"
})
"""
TYPES = {
    "NONE": "Undocumented", "LEFTMOUSE": "Left Mouse", "MIDDLEMOUSE": "Middle Mouse",
    "RIGHTMOUSE":"Right Mouse", "BUTTON4MOUSE": "Button4 Mouse", "BUTTON5MOUSE": "Button5 Mouse",
    "BUTTON6MOUSE": "Button6 Mouse", "BUTTON7MOUSE": "Button7 Mouse", "PEN": "Pen",
    "ERASER": "Eraser", "MOUSEMOVE": "Mouse Move", "INBETWEEN_MOUSEMOVE": "In-between Move",
    "TRACKPADPAN": "Mouse/Trackpad Pan", "TRACKPADZOOM": "Mouse/Trackpad Zoom",
    "MOUSEROTATE": "Mouse/Trackpad Rotate", "MOUSESMARTZOOM": "Mouse/Trackpad Smart Zoom",
    "WHEELUPMOUSE": "Wheel Up", "WHEELDOWNMOUSE": "Wheel Down", "WHEELINMOUSE": "Wheel In",
    "WHEELOUTMOUSE": "Wheel Out", "EVT_TWEAK_L": "Tweak Left", "EVT_TWEAK_M": "Tweak Middle",
    "EVT_TWEAK_R": "Tweak Right", "A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F",
    "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N", "O": "O",
    "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X",
    "Y": "Y", "Z": "Z", "ZERO": "0", "ONE": "1", "TWO": "2", "THREE": "3", "FOUR": "4", "FIVE": "5",
    "SIX": "6", "SEVEN": "7", "EIGHT": "8", "NINE": "9", "LEFT_CTRL": "Left Ctrl","LEFT_ALT": "Left Alt",
    "LEFT_SHIFT": "Left Shift", "RIGHT_ALT": "Right Alt", "RIGHT_CTRL": "Right Ctrl",
    "RIGHT_SHIFT": "Right Shift", "OSKEY": "OS Key", "APP": "Application", "GRLESS": "Grless",
    "ESC": "Esc", "TAB": "Tab", "RET Return": "Enter", "SPACE": "Spacebar", "LINE_FEED": "Line Feed",
    "BACK_SPACE": "Backspace", "DEL": "Delete", "SEMI_COLON": ";", "PERIOD": ".", "COMMA": ",",
    "QUOTE": '"', "ACCENT_GRAVE": "`", "MINUS": "-", "PLUS": "+", "SLASH": "/", "BACK_SLASH": r"\",",
    "EQUAL": "=", "LEFT_BRACKET": "[", "RIGHT_BRACKET": "]", "LEFT_ARROW": "Left Arrow",
    "DOWN_ARROW": "Down Arrow", "RIGHT_ARROW": "Right Arrow", "UP_ARROW": "Up Arrow",
    "NUMPAD_2": "Numpad 2", "NUMPAD_4": "Numpad 4", "NUMPAD_6": "Numpad 6", "NUMPAD_8": "Numpad 8",
    "NUMPAD_1": "Numpad 1", "NUMPAD_3": "Numpad 3", "NUMPAD_5": "Numpad 5", "NUMPAD_7": "Numpad 7",
    "NUMPAD_9": "Numpad 9", "NUMPAD_PERIOD": "Numpad .", "NUMPAD_SLASH": "Numpad /",
    "NUMPAD_ASTERIX": "Numpad *", "NUMPAD_0": "Numpad 0", "NUMPAD_MINUS": "Numpad -",
    "NUMPAD_ENTER": "Numpad Enter", "NUMPAD_PLUS": "Numpad +", "F1": "F1", "F2": "F2", "F3": "F3",
    "F4": "F4", "F5": "F5", "F6": "F6", "F7": "F7", "F8": "F8", "F9": "F9", "F10": "F10",
    "F11": "F11", "F12": "F12", "F13": "F13", "F14": "F14", "F15": "F15", "F16": "F16", "F17": "F17",
    "F18": "F18", "F19": "F19", "F20": "F20", "F21": "F21", "F22": "F22", "F23": "F23", "F24": "F24",
    "PAUSE": "Pause", "INSERT": "Insert", "HOME": "Home", "PAGE_UP": "Page Up",
    "PAGE_DOWN": "Page Down", "END": "End", "MEDIA_PLAY": "Media Play/Pause", "MEDIA_STOP": "Media Stop",
    "MEDIA_FIRST": "Media First", "MEDIA_LAST": "Media Last", "TEXTINPUT": "Text Input",
    "WINDOW_DEACTIVATE": "Window Deactivate", "TIMER": "Timer", "TIMER0": "Timer 0", "TIMER1": "Timer 1",
    "TIMER2": "Timer 2", "TIMER_JOBS": "Timer Jobs", "TIMER_AUTOSAVE": "Timer Autosave",
    "TIMER_REPORT": "Timer Report", "TIMERREGION": "Timer Region", "NDOF_MOTION": "NDOF Motion",
    "NDOF_BUTTON_MENU": "NDOF Menu", "NDOF_BUTTON_FIT": "NDOF Fit", "NDOF_BUTTON_TOP": "NDOF Top",
    "NDOF_BUTTON_BOTTOM": "NDOF Bottom", "NDOF_BUTTON_LEFT": "NDOF Left",
    "NDOF_BUTTON_RIGHT": "NDOF Right", "NDOF_BUTTON_FRONT": "NDOF Front",
    "NDOF_BUTTON_BACK": "NDOF Back", "NDOF_BUTTON_ISO1": "NDOF Isometric 1",
    "NDOF_BUTTON_ISO2": "NDOF Isometric 2", "NDOF_BUTTON_ROLL_CW": "NDOF Roll CW",
    "NDOF_BUTTON_ROLL_CCW": "NDOF Roll CCW", "NDOF_BUTTON_SPIN_CW": "NDOF Spin CW",
    "NDOF_BUTTON_SPIN_CCW": "NDOF Spin CCW", "NDOF_BUTTON_TILT_CW": "NDOF Tilt CW",
    "NDOF_BUTTON_TILT_CCW": "NDOF Tilt CCW", "NDOF_BUTTON_ROTATE": "NDOF Rotate",
    "NDOF_BUTTON_PANZOOM": "NDOF Pan/Zoom", "NDOF_BUTTON_DOMINANT": "NDOF Dominant",
    "NDOF_BUTTON_PLUS": "NDOF Plus", "NDOF_BUTTON_MINUS": "NDOF Minus",
    "NDOF_BUTTON_ESC": "NDOF Esc", "NDOF_BUTTON_ALT": "NDOF Alt",
    "NDOF_BUTTON_SHIFT": "NDOF Shift", "NDOF_BUTTON_CTRL": "NDOF Ctrl",
    "NDOF_BUTTON_1": "NDOF Button 1", "NDOF_BUTTON_2": "NDOF Button 2", "NDOF_BUTTON_3": "NDOF Button 3",
    "NDOF_BUTTON_4": "NDOF Button 4", "NDOF_BUTTON_5": "NDOF Button 5", "NDOF_BUTTON_6": "NDOF Button 6",
    "NDOF_BUTTON_7": "NDOF Button 7", "NDOF_BUTTON_8": "NDOF Button 8", "NDOF_BUTTON_9": "NDOF Button 9",
    "NDOF_BUTTON_10": "NDOF Button 10", "NDOF_BUTTON_A NDOF": "Button A", "NDOF_BUTTON_B": "NDOF Button B",
    "NDOF_BUTTON_C": "NDOF Button C", "ACTIONZONE_AREA": "ActionZone Area",
    "ACTIONZONE_REGION": "ActionZone Region", "ACTIONZONE_FULLSCREEN": "ActionZone Fullscreen"
}
"""
KEY_TYPES = util.Bidict({
    "Undocumented": "NONE", "Pen": "PEN", "Eraser": "ERASER", "A": "A", "B": "B", "C": "C", "D": "D", "E": "E",
    "F": "F", "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P",
    "Q": "Q", "R": "R", "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "Z", "0": "ZERO",
    "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR", "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT", "9": "NINE",
    "Left Ctrl": "LEFT_CTRL", "Left Alt": "LEFT_ALT", "Left Shift": "LEFT_SHIFT", "Right Alt": "RIGHT_ALT",
    "Right Ctrl": "RIGHT_CTRL", "Right Shift": "RIGHT_SHIFT", "OS Key": "OSKEY", "Application": "APP",
    "Grless": "GRLESS", "Esc": "ESC", "Tab": "TAB", "Enter": "RET Return", "Spacebar": "SPACE",
    "Line Feed": "LINE_FEED", "Backspace": "BACK_SPACE", "Delete": "DEL", ";": "SEMI_COLON", ".": "PERIOD",
    ",": "COMMA", '"': "QUOTE", "`": "ACCENT_GRAVE", "-": "MINUS", "+": "PLUS", "/": "SLASH", r"\",": "BACK_SLASH",
    "=": "EQUAL", "[": "LEFT_BRACKET", "]": "RIGHT_BRACKET", "Left Arrow": "LEFT_ARROW", "Down Arrow": "DOWN_ARROW",
    "Right Arrow": "RIGHT_ARROW", "Up Arrow": "UP_ARROW", "Numpad 2": "NUMPAD_2", "Numpad 4": "NUMPAD_4",
    "Numpad 6": "NUMPAD_6", "Numpad 8": "NUMPAD_8", "Numpad 1": "NUMPAD_1", "Numpad 3": "NUMPAD_3",
    "Numpad 5": "NUMPAD_5", "Numpad 7": "NUMPAD_7", "Numpad 9": "NUMPAD_9", "Numpad .": "NUMPAD_PERIOD",
    "Numpad /": "NUMPAD_SLASH", "Numpad *": "NUMPAD_ASTERIX", "Numpad 0": "NUMPAD_0", "Numpad -": "NUMPAD_MINUS",
    "Numpad Enter": "NUMPAD_ENTER", "Numpad +": "NUMPAD_PLUS", "F1": "F1", "F2": "F2", "F3": "F3", "F4": "F4",
    "F5": "F5", "F6": "F6", "F7": "F7", "F8": "F8", "F9": "F9", "F10": "F10", "F11": "F11", "F12": "F12",
    "F13": "F13", "F14": "F14", "F15": "F15", "F16": "F16", "F17": "F17", "F18": "F18", "F19": "F19", "F20": "F20",
    "F21": "F21", "F22": "F22", "F23": "F23", "F24": "F24", "Pause": "PAUSE", "Insert": "INSERT", "Home": "HOME",
    "Page Up": "PAGE_UP", "Page Down": "PAGE_DOWN", "End": "END", "Media Play/Pause": "MEDIA_PLAY",
    "Media Stop": "MEDIA_STOP", "Media First": "MEDIA_FIRST", "Media Last": "MEDIA_LAST",
    "Window Deactivate": "WINDOW_DEACTIVATE", "ActionZone Area": "ACTIONZONE_AREA",
    "ActionZone Region": "ACTIONZONE_REGION", "ActionZone Fullscreen": "ACTIONZONE_FULLSCREEN"
})
