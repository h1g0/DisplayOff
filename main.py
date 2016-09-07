# -*- coding: utf-8 -*-
from ctypes import windll
from time import sleep
import argparse


HWND_BROADCAST = 0xFFFF
WM_SYSCOMMAND = 0x0112
SC_MONITORPOWER = 0xF170
DISPLAY_ON = -1
DISPLAY_OFF = 2

def DispOn(waitTime):
    sleep(waitTime)
    windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_ON
        )

def DispOff(waitTime):
    sleep(waitTime)
    windll.user32.PostMessageA(
        HWND_BROADCAST,
        WM_SYSCOMMAND, 
        SC_MONITORPOWER,
        DISPLAY_OFF
        )

def main():
    parser = argparse.ArgumentParser()
    dispGroup = parser.add_mutually_exclusive_group()
    dispGroup.add_argument( '-x', '--off', action='store_true',  default=True,
                                                help='Turn off the display. (default)' )
    dispGroup.add_argument( '-o', '--on', action='store_true',  default=False,
                                                help='Turn on the display.' )
    parser.add_argument( '-w','--wait', type=int, default=0 ,
                                        help='wait <WAIT> seconds before turning (on | off). (default=0)')
    options = parser.parse_args()

    if options.on == True:
        DispOn( options.wait )
    else:
        DispOff( options.wait )

if __name__ == '__main__':
    main()

