import socket


TCP_IP = '192.168.0.104'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
enMESSAGE = MESSAGE.encode()
s.send(enMESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

deData = data.decode()
print ("received data:", data)
