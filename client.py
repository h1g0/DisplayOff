# -*- coding: utf-8 -*-
import xmlrpc.client as xmlrpc_client
import configparser

def main():
    config.read("./config.ini")
    client = xmlrpc_client.ServerProxy(config.get('Client','Address'))

    #client.DispOn(0)
    #client.DispOff(0)

if __name__ == '__main__':
    main()