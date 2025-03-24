import socket

c = socket.socket (socket.AF_INET,socket.SOCK_DGRAM)

ip = '192.168.60.102'
port = 5564

username1 =input('Enter username')
c.sendto(username1.encode(),(ip,port))
password1 =input('Enter password')

c.sendto(password1.encode(),(ip,port))

data, saveradr = c.recvfrom(1024)
print('Massage and server address from server: ',data, saveradr)