from socket import *
from encyption import *
class Server:

    global serverSocket
    global serverPort

    def main():
        serverPort = 12000    
        serverSocket = socket(AF_INET, SOCK_DGRAM) #creates a server socket
        serverSocket.bind(("", serverPort)) #binds the socket with the port number
        print("The server is ready to receive")

        
        while True:

            incomingMsg,address = serverSocket.recvfrom(2048)
            host = address[0]
            portNum = address[1]

            #message = {action,username,password}
            message = incomingMsg.decode().split("##")
            #print(message)
            if message[0]=="1":
                status =(Server.register(host,portNum,message[1],message[2]))

                serverSocket.sendto(status.encode(),(host,portNum))
                
            elif message[0]=="2":
                status =(Server.login(message[1],message[2]))
                serverSocket.sendto(status.encode(),(host,portNum))

    if __name__ == "__main__":
        main()

    def register(host,portNum,username,password):

        user =  username+"#"+host+"#"+str(portNum)+"#"+password

        if (Server.checkUser(username,host)==False):

            try:
                f= open("users/users.txt","a+")
                f.writelines(user)
                f.close()

            except (FileNotFoundError):
                f = open("users/users.txt", "w+")
                f.writelines(user)
                f.close()
            return "register successful"
        else:
            return "register unsuccessul"

    def checkUser(username,host):

        try:

            f = open("users/users.txt")
            
            for i in f:
                user = i.split("#")
                if ((username==user[0]) and (host==user[1])):
                    return True
            return False
        except FileNotFoundError:
            return False
        
    def login(username,password):
        try:

            f = open("users/users.txt")

            for i in f:
            
                #reads the data stored in the text file
                user = i.split("#")
                print(user)

                if((username==user[0]) and (password==(user[3]).strip())):
                   return "login successful"
            return "login unsuccessful"
        except FileNotFoundError:
            return "login unsuccessful"
Server.main()