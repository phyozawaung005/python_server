import socket


    # Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name
host = '192.168.1.8'
port = 12345  # You can use any port you prefer, but make sure it's not in use

    # Bind to the port
server_socket.bind((host, port))

    # Listen for incoming connections
server_socket.listen(5)

print("Server is listening...")

   