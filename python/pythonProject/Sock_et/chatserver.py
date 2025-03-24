import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a TCP socket

ip = socket.gethostname()
port = 54321

s.bind((ip, port))
s.listen(3)
print('Listening.....')

clisock, cliaddr = s.accept()
print('Client address is = ', cliaddr)

while True:
    data = clisock.recv(100).decode()
    print('by client = ', data)

    msg = input('~>> ')

    clisock.send(msg.encode())

# Closing the client socket after the loop ends
clisock.close()
