import socket
client=socket.socket()
client.connect(('192.168.65.131',1234))
mystring="hgjhgjh"
b = bytes(mystring, 'utf-8')
client.send(b)
client.recv(1024)
def communicate(data):
	mystring=data
	b = bytes(mystring, 'utf-8')
	client.send(b)
	print(client.recv(1024).decode("utf-8"))
	return 

communicate("is this really working!!!")
communicate("Hello server")
communicate("VIRUS")
communicate("TROJAN")	
communicate("disconnect")

