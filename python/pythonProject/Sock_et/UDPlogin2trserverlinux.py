import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '192.168.1.2'
port = 5623

s.bind((ip, port))
print('Binding...')

while True:
    data, addr = s.recvfrom(1024)
    username, password = data.decode().split(',')

    if username == 'admin' and password == 'asd123':
        response = 'Login Success'
    else:
        response = 'Login Fail'
    s.sendto(response.encode(), addr)
