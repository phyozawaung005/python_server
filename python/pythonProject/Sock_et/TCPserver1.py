import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 10000
s.bind((ip, port))
s.listen(3)
print('Server listening....')
while True:
    clisock, cliaddr = s.accept()
    print('Client address is:', cliaddr)
    msg=clisock.recv(50)
    print('message by client:', msg.decode())

    data = 'Hello I am server'
    clisock.send(data.encode())
