import socket
import os
def send_file(conn, filename):
    try:
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                conn.sendall(data)
        print("File sent successfully")
    except FileNotFoundError:
        print("File not found")
def main():
    host = socket.gethostname()
    port = 12355

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening...")

    while True:
        conn, addr = server_socket.accept()
        print("Connected to", addr)
        filename = conn.recv(1024).decode()
        print("Request received for file:", filename)
        send_file(conn, filename)
        conn.close()
if __name__ == "__main__":
    main()
