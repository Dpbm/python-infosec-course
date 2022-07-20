import socket

# using IPV4 and TCP
server_socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 2480

server_socket_object.bind((host, port))

max_connections_at_once = 2
server_socket_object.listen(max_connections_at_once)

while True:
    client_socket, address = server_socket_object.accept()
    print(f"[connection] {str(address)}")

    message = 'thank you for connecting!'
    client_socket.send(message.encode('ascii'))

    client_socket.close()
