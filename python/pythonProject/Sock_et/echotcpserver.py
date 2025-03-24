import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the local IP address of the server
ip = socket.gethostbyname(socket.gethostname())
port = 1234

# Bind the socket to the IP and port
s.bind((ip, port))
print('Binding....')

while True:
    # Receive data from client
    Rdata, addr = s.recvfrom(1024)
    print('Message from client:', Rdata.decode())

    # Echo the received data back to the client
    s.sendto(Rdata, addr)
