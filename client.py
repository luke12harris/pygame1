import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#address family, socket type

serverAddress = ("192.168.0.2", 65535) # hardcoded

clientSocket.connect(serverAddress)

print(clientSocket.recv(1024).decode()) #where 1024 is a buffer
