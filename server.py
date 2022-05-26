import socket

#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address family = IPV4, socket type.
print("socket created")

server = "localhost"
port = 5555

serverIP = socket.gethostbyname(server)

serverSocket.bind(server, port) #address, port

serverSocket.listen(2) #max num of connections
print("listening...")


while True:
    clientSocket, clientAddress = serverSocket.accept()
    print (f"connection established with {clientAddress}")

    clientSocket.send(bytes ("you made it", "utf-8")) # converts to byte format

    clientSocket.close()
