import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 4443
s.bind ((ip,port))
s.listen(3)
print('Server is listening...')

clisock, cliaddr = s.accept()
print('Client address is = ', cliaddr)
while True:
    data=clisock.recv(100).decode()
    print('by Client = ',data)
    msg = input ('~>>')
    clisock.send(msg.encode())
    clisock.close()
