#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading
import argparse

lock = threading.Lock()
openNum = 0
threads = []

def portScanner(host,port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1
        print('[+] %d open' % (port))#在CMD中看开了什么端口
        lock.release()
        return port
        s.close()
    except:
        pass

def DuanKouScan(bot, contact, member, content):
    hostList = content[9:].split(',')
    setdefaulttimeout(1)
    for host in hostList:
        print('Scanning the host:%s......' % (host))
        for p in range(1,10000):#目前只有10000以内的端口扫描，懒得写基于数组或者基于用户输入的扫描了
            t = threading.Thread(target=portScanner,args=(host,p))
            
            threads.append(t)
            t.start()     

        for t in threads:
            t.join()
        
        bot.SendTo(contact,'[*] The host:%s scan is complete!\n[*] A total of %d open port ' % (host,openNum))
