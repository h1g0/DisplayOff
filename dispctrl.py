# -*- coding: utf-8 -*-
from ctypes import windll
from time import sleep

HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
DISPLAY_ON = -1
DISPLAY_OFF = 2

def DispOn(waitTime):
    sleep(waitTime)
    return windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_ON
        )

def DispOff(waitTime):
    sleep(waitTime)
    return windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_OFF
        )
