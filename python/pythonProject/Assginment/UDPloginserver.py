import socket
#UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Define server host and port
IP = '192.168.1.2'
PORT = 53425
# Bind the socket to the address and port
server_socket.bind((IP, PORT))
# Define username and password
USERNAMES_PASSWORDS = {
    'phyozawaung': 'phyozawaung1',
}

print('Server is listening.....'.format(IP, PORT))

while True:
    # Receive data from clients
    data, client_address = server_socket.recvfrom(1024)
    username, password = data.decode().split(',')
    # assuming the client sends username and password separated by a comma
    print("Received username: ", username)
    print("Received password: ", password)
    # Authenticate user
    if username in USERNAMES_PASSWORDS and password == USERNAMES_PASSWORDS[username]:
        server_socket.sendto(b'Success: You are logged in!', client_address)
        print("User login is successful.")
    else:
        server_socket.sendto(b'Error: Invalid username or password!', client_address)
        print("User login fail")
