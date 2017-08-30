#Network Programming for Client side
import socket
host='10.77.17.198'
port=12345
size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
while 1:
	s.send(input('>>>').encode())
	data=s.recv(size)
	print('>>>' +data.decode())