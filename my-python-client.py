#coding:utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9999
s.connect((host,port))
print(s.recv(1024).decode('utf-8'))
for data in ['笑话','小白','小明']:
	s.send(data.encode('utf-8'))
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
