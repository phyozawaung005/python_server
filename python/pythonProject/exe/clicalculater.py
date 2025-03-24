import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 4572))

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    client_socket.send(str(a).encode())
    client_socket.send(str(b).encode())

    response = client_socket.recv(4096).decode()
    print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
