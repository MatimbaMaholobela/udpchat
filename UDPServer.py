from socket import *


#server portNumber
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("The server is ready to receive")

while True:

      
    message, clientAddress = serverSocket.recvfrom(2048)
    xx = message.decode().splitlines()
    print(xx[0])


    serverSocket.sendto(xx[1].encode(), clientAddress)