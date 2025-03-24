import socket


def calculate_operations(a, b):
    Add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    rem = a % b

    if Add % 2 == 0 and sub % 2 == 0 and mul % 2 == 0 and div % 2 == 0 and rem % 2 == 0:
        result = f'Addition: {Add}\nSubtraction: {sub}\nMultiplication: {mul}\nDivision: {div}\nRemainder: {rem}\nAll results are even.'
    else:
        result = f'Addition: {Add}\nSubtraction: {sub}\nMultiplication: {mul}\nDivision: {div}\nRemainder: {rem}\nAt least one result is odd.'

    print(result)  # Print the result on the server
    return result


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 4572))
    server_socket.listen(1)

    print("Server is listening...")

    while True:
        client_socket, _ = server_socket.accept()
        print("Connection established with client")

        a = int(client_socket.recv(1024).decode())
        b = int(client_socket.recv(1024).decode())

        result = calculate_operations(a, b)

        client_socket.send(result.encode())
        client_socket.close()


if __name__ == "__main__":
    main()
