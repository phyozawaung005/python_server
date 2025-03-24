import socket

# Server configuration
HOST = socket.gethostname()
PORT = 12345

# User credentials (in real-world scenarios, these would be stored securely)
USER_CREDENTIALS = {
    'Admin': 'asd123',

}

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    # Bind the socket to the address and port
    server_socket.bind((HOST, PORT))

    print('Server is listening...')

    while True:
        # Receive data from the client
        data, address = server_socket.recvfrom(1024)
        username, password = data.decode().split(':')

        # Check if the username exists and the password matches
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            response = "Login successful!"
        else:
            response = "Invalid username or password."

        # Send the response back to the client
        server_socket.sendto(response.encode(), address)
