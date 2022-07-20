import socket

s = socket.socket()

ip   =     input("[Target IP]: ")
port = int(input("[Target PORT]: "))

if(s.connect_ex((ip, port))):
    print(f"the port {port} is open at {ip}")
else:
    print(f"the port is not open")

s.close()
