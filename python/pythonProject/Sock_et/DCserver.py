import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip = '192.168.60.115'
port = 54321

cli.connect((ip,port))

cli.send(b'Hello Server')
data = cli.recv(10)
print(data)

  
