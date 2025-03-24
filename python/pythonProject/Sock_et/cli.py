import socket

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostname()
port = 12345
##client and server need to same port

cli.connect((ip,port))
##((ip,port))= server ip and port
##to connect server


cli.send(b'Hello,I am your cliend')
##b=string to avoid error
data=cli.recv (10)
##10=receive letter
