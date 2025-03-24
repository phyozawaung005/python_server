import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=socket.gethostname()
port=2100
s.bind((ip,port))
s.listen(2)
print('Server is listening...')

while True:
    clisock, cliaddr = s.accept()
    print ('Client address is:', cliaddr)
    msg = clisock.recv(60)
    print ('Message From Client:',msg.decode())
    data = 'Hello Client'
    clisock.send(data.encode())
