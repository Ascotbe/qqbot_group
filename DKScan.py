#!/usr/bin/python
#coding=utf-8

import socket
 

def DuanKouScan(bot, contact, member, content):
    ip = content[9:24].strip(' ')
    port =100
        for port in range(20,port):
            get_ip_status(ip,port)
def get_ip_status(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip,port))
        bot.SendTo(contact,'{0} port {1} is open'.format(ip, port))
    except Exception as err:
        bot.SendTo(contact,'{0} port {1} is not open'.format(ip,port))
    finally:
        server.close()
 

 