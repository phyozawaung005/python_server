import socket

# Server configuration
SERVER_HOST = '192.168.60.1'
SERVER_PORT = 5561

# User credentials
username = input("Enter username: ")
password = input("Enter password: ")

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    # Send data to the server
    client_socket.sendto(f"{username}:{password}".encode(), (SERVER_HOST, SERVER_PORT))

    # Receive response from the server
    response, _ = client_socket.recvfrom(1024)
    print("Server response:", response.decode())
