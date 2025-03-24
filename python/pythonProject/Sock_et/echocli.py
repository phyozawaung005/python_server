import socket

# Create a UDP socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server configuration
ip = '192.168.60.46'
port = 5803

# Prompt the user to input a message
msg = input("Type a message: ")

# Send the message to the server
c.sendto(msg.encode(), (ip, port))

# Receive response from the server
Rdata, addr = c.recvfrom(1024)
print('Response from server:', Rdata.decode(), addr)

# Close the socket
c.close()
