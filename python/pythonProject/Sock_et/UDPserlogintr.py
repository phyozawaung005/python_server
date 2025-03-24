import socket
s=socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

ip = '192.168.60.86'
port = 54312

s.bind((ip,port))
print('Server Binding')
username,cliaddr=s.recvfrom(1024)
print('Username:', username)
print('Connect with', cliaddr)

password,cliaddr=s.recvfrom(1024)

#Authentication
if username == 'admin' and password == 'asd123':
    s.sendto(b'Login Success', cliaddr)
else:
    s.sendto(b'Login Fail', cliaddr)
