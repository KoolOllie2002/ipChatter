import os
from socket import *
print("==Your Ip Address==")
import ipGrabber
print("=Give this to client=")
host = ""
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print ("Waiting to receive messages...")
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    dataChange = str(data, 'utf-8')
    print ("Received message: " + dataChange)
UDPSock.close()
os._exit(0)
