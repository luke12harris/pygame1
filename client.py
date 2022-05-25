import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#address family, socket type

#get ip
hostname = socket. gethostname()
local_ip = socket. gethostbyname(hostname)

clientSocket.connect((local_ip, 9999))

print(clientSocket.recv(1024).decode()) #where 1024 is a buffer
