import socket
# Define server host and port
IP = "192.168.1.10"
PORT = 53424
# Define username and password
USERNAMES_PASSWORDS = {
    'phyozawaung': 'phyozawaung1',
}
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen(1)
print('Server is listening on {}:{}'.format(IP, PORT))
while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print('Connection from', client_address)
        print('Connection',connection)
        # Receive username and password
        username = connection.recv(1024).decode()
        password = connection.recv(1024).decode()
        print("Received username: ", username)
        print("Received password: ", password)
        # Authenticate user
        if username in USERNAMES_PASSWORDS and password == USERNAMES_PASSWORDS[username]:
            connection.sendall(b'Success: You are logged in!')
        else:
            connection.sendall(b'Error: Invalid username or password!')
    finally:
        # Clean up the connection
        connection.close()
        print("Connection Close")
