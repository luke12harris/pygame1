import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#address family, socket type

clientSocket.connect(("localhost", 9999))

print(clientSocket.recv(1024).decode()) #where 1024 is a buffer
