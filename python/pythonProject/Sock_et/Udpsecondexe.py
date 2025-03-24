import socket
cli=socket.socket (socket.AF_INET,socket.SOCK_DGRAM)

ip='192.168.60.99'
port= 5551

msg=b'This is Client,PhyoPhyo'
cli.sendto(msg,(ip,port))

data,serveraddr=cli.recvfrom(1024)
print('Message from server:',data,serveraddr)