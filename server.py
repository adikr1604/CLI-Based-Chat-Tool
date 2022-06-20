import socket, threading
host = '127.0.0.1'
port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []