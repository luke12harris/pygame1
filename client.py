import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#address family, socket type

serverAddress = ("localhost", 9999)

clientSocket.connect(serverAddress)

print(clientSocket.recv(1024).decode()) #where 1024 is a buffer
