import socket

#create socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #address family, socket type

serverSocket.bind(("localhost", 9999)) #address, port

serverSocket.listen(3) #num of connections

while True:
    clientSocket, clientAddress = serverSocket.accept()
    print (f"connection established with {clientAddress}")

    clientSocket.send(bytes ("you made it", "utf-8")) # converts to byte format

    clientSocket.close()
