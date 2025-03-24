import socket

# Define server host and port
IP = socket.gethostname()
PORT = 53424

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
client_socket.connect((IP, PORT))

try:
    # Send username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    client_socket.sendall(username.encode())
    client_socket.sendall(password.encode())

    # Receive response
    response = client_socket.recv(1024)
    print(response.decode())

finally:
    # Clean up the connection
    client_socket.close()
