import socket

c=socket.socket()
ip='192.168.60.1'
port=5834

c.connect((ip,port))
c.send(b'Hello World')
data=c.recv(100)
print(data)