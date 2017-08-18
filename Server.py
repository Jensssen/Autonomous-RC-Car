import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('192.168.178.30', 8000))
s.bind(('127.0.0.1', 8000))
print("Lisstening for connections...")
s.listen(1)

connection, address = s.accept()
print("Connected to client", address)


while True:
	data = connection.recv(2048)
	if not data: break
	print("Received from Client: ", data)
	connection.send(data)
	
connection.close()
	
