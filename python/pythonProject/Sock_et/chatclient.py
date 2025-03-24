import socket

c = socket.socket()
ip = socket.gethostname()
port = 54321

c.connect((ip, port))

while True:
    msg = input('~>> ')
    c.send(msg.encode())

    if msg.lower().strip() == "bye":
        break

    data = c.recv(1024).decode()
    print("Message from Server:", data)

c.close()
