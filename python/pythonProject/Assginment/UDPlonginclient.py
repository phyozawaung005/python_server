import socket

# Define server host and port
IP = '192.168.1.2'
PORT = 53425


# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    # Send username and password
    username = input("Enter username to login in server: ")
    password = input("Enter password to login in server: ")
    message = username + ',' + password  # Combine username and password separated by a comma
    client_socket.sendto(message.encode(), (IP, PORT))

    # Receive response
    response, server_address = client_socket.recvfrom(10246)
    print(response.decode())

finally:
    # Clean up the socket
    client_socket.close()
