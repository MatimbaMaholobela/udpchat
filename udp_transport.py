from socket import *

class Server:
    global serverPort
    serverPort = 12000

    global serverSocket
    serverSocket = socket(AF_INET, SOCK_DGRAM) #creates a server socket

    serverSocket.bind(("", serverPort)) #binds the socket with the port number

    def register(password):

        username, address = serverSocket.recvfrom(2048)
        username = username.decode().split("##")

        host = address[0]
        portNum = address[1]
        user =  username[0]+"#"+host+"#"+str(portNum)+"#"+username[1]

        if (Server.checkUser(username,host)==False):

            try:
                f= open("users/users.txt","a")
                f.write(user)
                f.write("\n")
                f.close()

            except (FileNotFoundError):
                f = open("users/users.txt", "w")
                f.write(user)
                f.write("\n")
                f.close()
            return "New user created"
        else:
            return "User already exists"

    def checkUser(username,host):

        f = open("users/users.txt")
        
        for i in f:
            user = i.split("#")
            if ((username==user[0]) and (host==user[1])):
                return True
        return False
    def login(username,password):

        f = open("users/users.txt")
        for i in f:
            user = i.split("#")
            if(username==user[0]) and password==user[-1]:
                return True
        return False
    
