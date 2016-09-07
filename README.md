# DisplayOff
A Python script for turning off (on) the display by using Win32API.  
Server and client programs are also included so that you may run this script from remote computer.

```
usage: main.py [-h] [-x | -o] [-w WAIT] 

optional arguments: 
  -h, --help            show this help message and exit 
  -x, --off             Turn off the display. (default)
  -o, --on              Turn on the display.
  -w WAIT, --wait WAIT  wait <WAIT> seconds before turning off (on). (default=0)
  ```