import socket

client_socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2480

client_socket_object.connect((host, port))

message = client_socket_object.recv(1024)

client_socket_object.close()

print(message.decode('ascii'))
