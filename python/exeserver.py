import socket
cli=socket.socket (socket.AF_INET, socket.SOCK_STREAM)
ip=socket.gethostname()
port=2100
cli.connect((ip,port))
cli.send (b'I am your Client')
data=cli.recv(60)
