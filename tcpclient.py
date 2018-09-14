#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
ip_port = ('127.0.0.1',8009)
sk = socket.socket()
sk.connect(ip_port)
while True:
    data = sk.recv(1024)
    print 'receive:',data
    inp = input('please input:')
    sk.sendall(inp)
    if inp == 'exit':
        break
sk.close()
