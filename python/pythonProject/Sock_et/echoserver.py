import socket

# Server configuration
HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 12345        # Arbitrary non-privileged port

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening...')

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    print('Connected to:', client_address)


    try:
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print('Received:', data.decode())
            connection.sendall(data)
    finally:
        # Clean up the connection
        connection.close()
