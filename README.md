# DisplayOff
A Python script for turning (on|off) the display by using Win32API.  
Server program is also included so that you may run this script from the web browser on your remote computers.

## main.py
Turning (on|off) by local compter.
```
usage: 
python main.py [-h] [-x | -o] [-w WAIT] 

optional arguments: 
  -h, --help            show this help message and exit 
  -x, --off             Turn off the display. (default)
  -o, --on              Turn on the display.
  -w WAIT, --wait WAIT  wait <WAIT> seconds before turning off (on). (default=0)
  ```
## server.py
  
```
usage:
python server.py
 ```

Open your browser and access  "http://host:port/(on|off)[?wait seconds]".  
for example:  
*  "http://localhost:8000/off" means to turn off  immediately.
* "http://192.168.0.2:8080/on?5" means to turn on in 5 seconds.

To shutdown the server, please press Ctrl+C.  
To configure host and port, please see config.ini.  
Attention: You may need to configure port and firewall settings on your Internet router. 
