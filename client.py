import os
from socket import *
data=""
def ipAddress():
    while True:
        host = input("Enter servers ip: ") # set to IP address of target computer 
        if host=="":
            print("error")
        else:
            return host
            
    
def sendMsg(host):
    port = 13000
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    connected = str.encode("DEVICE CONNECTED...")
    UDPSock.sendto(connected, addr)
    messageToSend = input("Enter message to send or type 'exit': ")
    ipAddress = socket.gethostbyname(socket.gethostname())
    data = (ipAddress, ": ", messageToSend)
    dataChange = str.encode(ipAddress + ":" + data)
    UDPSock.sendto(dataChange, addr)
    UDPSock.close()
    
    
host=ipAddress()
while True:
    if data=="exit":
        break
    else:
        sendMsg(host)
os._exit(0)
 

