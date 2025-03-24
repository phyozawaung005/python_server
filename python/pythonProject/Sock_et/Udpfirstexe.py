import socket
s=socket.socket (socket.AF_INET,socket.SOCK_DGRAM)

ip= '192.168.60.101'
port = 5432
s.bind ((ip,port))
print('Server Binding...')

while True:
    data,cliaddr=s.recvfrom(1024)
    print('Client ip:',cliaddr)
    print('Message from client',data.decode())
    msg='Hello I am server.'
    s.sendto(msg.encode(),cliaddr)