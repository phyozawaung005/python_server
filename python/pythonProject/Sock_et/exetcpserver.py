import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 12345
s.bind((ip, port))
s.listen(3)
print('Server is lisening...')
while True:
    clisock, cliaddr = s.accept()
    print('Client address is:', cliaddr)
    msg = clisock.recv(60)
    print('Message From Client:',msg.decode())
    data = 'Hello Client'
    clisock.send(data.encode())
