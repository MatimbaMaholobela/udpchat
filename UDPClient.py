from socket import *

serverName = "192.168.1.112"
serverPort = 12000

#Af_iNet --> address from the internet
#socket type----> SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_DGRAM)

user = input("enter a unique username:")
password = input("enter password:")

send = user+"##"+password


clientSocket.sendto(send.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()