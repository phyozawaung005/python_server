import socket

c=socket.socket()
ip=socket.gethostname()
port=4443

c.connect ((ip,port))
msg=input ('~>>')
c.send(msg.encode())

data=c.recv(100).decode
print ('Message from Server', data)

while msg.lower().strip() !="bye":
    c.send (msg.encode())
    data=c.recv(100).decode()
    print(data)
    msg=input('~>>')
    c.close()
