#!/usr/bin/python3
#client.py

import socket
import binascii
import re
import mmap

host = "192.168.80.68"
port = 2002

for i in range(20):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host,port)) #connect to client
        connection=True
        print("Connected")
        filename="flag"+str(i)+".jpg"
        file = open(filename, "wb")
        next=client.recv(1024)
        flag=b''
        signature= binascii.a2b_hex("ffd8")
        while next!=b'':
            next=client.recv(1024)
            start=binascii.b2a_hex(next)
            if "ffd8" in start:
                start1= re.search('.*(ffd8.*)',start)
                print("found it!" + str(start1))
                file.close
                client.close()
            flag = flag + next
            print(binascii.b2a_hex(next))
        file.write(flag)
        file.close
        client.close()
    except ConnectionRefusedError:
        print ("Connection closed")
        connection=False
