import win32gui
from win32gui import *
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

screen_size = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

left = screen_size[0]
top = screen_size[1]
right = screen_size[2]
bottom = screen_size[3]


lpppoint = ((left + 75, top - 75), (right + 75, top + 75), (left - 75, bottom - 75))


while True:

    hdc = win32gui.GetDC(0)
    mhdc = CreateCompatibleDC(hdc)
    hbit = CreateCompatibleBitmap(hdc, sh, sw)
    holdbit = SelectObject(mhdc, hbit)

    PlgBlt(
        hdc,
        lpppoint,
        hdc,
        left - 40,
        top - 40,
        (right - left) + 80,
        (bottom - top) + 80,
        None,
        0,
        0,
    )