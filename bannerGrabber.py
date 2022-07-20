import socket

s = socket.socket()

ip   = input("[IP Target] : ")
port = int(input("[PORT Target]: "))

s.connect((ip, port))

print(s.recv(1024))
s.close()
