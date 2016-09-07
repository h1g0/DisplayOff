# -*- coding: utf-8 -*-
import argparse
import dispctrl

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
        return dispctrl.DispOn( options.wait )
    else:
        return dispctrl.DispOff( options.wait )

if __name__ == '__main__':
    main()

