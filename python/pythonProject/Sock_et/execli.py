import socket
cli= socket.socket (socket.AF_INET, socket.SOCK_STREAM)
ip=socket.gethostname()
port=12345
cli.connect((ip,port))
cli.send (b'I am Your Client')
data=cli.recv(60)