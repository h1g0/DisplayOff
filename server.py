# -*- coding: utf-8 -*-
import xmlrpc.server as xmlrpc_server
import configparser
import dispctrl
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse


#serverShutdown=False # flag whether stop this server.

config = configparser.SafeConfigParser()
config.read("./config.ini")

host = config.get('Server','Host')
port = int(config.get('Server','Port'))

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        url=urlparse(self.path)
        body = b'Usage: http://host:port/(on|off)[?wait seconds]'
        wait=0

        if url.query.isdigit() and int(url.query) >0:
            wait=int(url.query)
        
        if url.path == '/on':
            dispctrl.DispOn(wait)
            body = b'Turning on succeeded.'
        elif url.path == '/off':
            dispctrl.DispOff(wait)
            body = b'Turning off succeeded.'

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)


def main():
    httpd = HTTPServer((host, port), MyHandler)
    print('Server starting... press Ctrl+C to exit.')
    httpd.serve_forever()

if __name__ == '__main__':
    main()