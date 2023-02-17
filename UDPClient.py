from socket import *
from encyption import *

serverName = "192.168.2.3"
serverPort = 12000

#Af_iNet --> address from the internet
#socket type----> SOCK_DGRAM
clientSocket = socket(AF_INET, SOCK_DGRAM)

key = input("Enter (1) to register or  (2) to login:")
username = input("enter a unique username:")
password = input("enter password:")
send = key+"##"+username+"##"+password

clientSocket.sendto(send.encode(),(serverName, serverPort))

while True:

    response, serverAddress = clientSocket.recvfrom(2048)
    #print(response.decode())

    if(response.decode()=="login unsuccessful" or (response.decode()=="register unsuccessful")):
        key = input("Enter (1) to register or (2) to login:")
        username = input("enter a unique username:")
        password = input("enter password:")
        send = key+"##"+username+"##"+password
        clientSocket.sendto(send.encode(),(serverName, serverPort))
    # else:
    #     print(response.decode())


clientSocket.close()