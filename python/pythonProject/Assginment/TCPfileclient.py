import socket

def receive_file(sock, filename):
    try:
        with open(filename, 'wb') as file:
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                file.write(data)
        print("File received successfully")
    except Exception as e:
        print("Error receiving file:", str(e))

def main():
    host = socket.gethostname()
    port = 12355

    filename = input("Enter file name to download: ")  # Prompt user for filename

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(filename.encode())

    receive_file(client_socket, filename)

    client_socket.close()

if __name__ == "__main__":
    main()
