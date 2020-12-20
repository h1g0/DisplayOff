# -*- coding: utf-8 -*-
from ctypes import windll
from time import sleep
from types import Final

HWND_BROADCAST: Final[int] = 0xFFFF
WM_SYSCOMMAND: Final[int] = 0x0112
SC_MONITORPOWER: Final[int] = 0xF170
DISPLAY_ON: Final[int] = -1
DISPLAY_OFF: Final[int] = 2

def DispOn(wait_time: int)->bool:
    sleep(wait_time)
    result = windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_ON
        )
    if result is 0:
        return False
    else:
        return True

def DispOff(wait_time: int)->bool:
    sleep(wait_time)
    result = windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_OFF
        )
    if result is 0:
        return False
    else:
        return True
