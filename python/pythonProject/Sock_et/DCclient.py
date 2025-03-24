import socket


# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
SERVER_ADDRESS = socket.gethostname()
SERVER_PORT = 10000



# Bind socket to address and port
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening")

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print("Connection established with", client_address)

    # Receive username from client
    username1 = client_socket.recv(1024).decode()
    print("Username received:", username1)

    # Receive password from client
    password1 = client_socket.recv(1024).decode()
    print("Password received:", password1)

    # Authenticate user
    if username1 =='admin' and password1 =='asd123':
        client_socket.send(b"Log in Success")
        print("User authenticated.")
    else:
        client_socket.send(b"Login Fail")
        print("Invalid credentials. Connection closed.")

    # Close connection
    client_socket.close()
