# -*- coding: utf-8 -*-
import xmlrpc.server as xmlrpc_server
import configparser
import dispctrl

def main():
    config = ConfigParser.SafeConfigParser()
    config.read("./config.ini")

    IPaddress = (config.get('Server','IP'), int(config.get('Server','Port')))

    server = xmlrpc_server.SimpleXMLRPCServer(IPaddress)

    server.register_function(dispctrl.DispOn,'DispOn') 
    server.register_function(dispctrl.DispOff, 'DispOff')

    server.register_introspection_functions()

    server.serve_forever()

if __name__ == '__main__':
    main()