import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = '192.168.1.2' # Added parentheses to call the function
port = 5569

username = input('Enter Username:')
password = input('Enter Password:')

# Encoding username and password properly
data = f"{username},{password}".encode()

c.sendto(data, (ip, port))

response, caddr = c.recvfrom(1024)
print('Response from server:', response.decode())
