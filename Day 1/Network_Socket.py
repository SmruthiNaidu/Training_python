#Network Programming for Server side
import socket
host=''
port=11122
backlog=2
size=1024
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
client,address=s.accept()
while 1:
	data=client.recv(size)
	if data.decode()=='exit':
		client.close()
	else:
		print('>>>' +data.decode())
		client.send(input('>>>').encode())
