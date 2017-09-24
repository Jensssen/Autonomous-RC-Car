import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('192.168.2.30', 8000)) #Adolf-Wagner
#s.bind(('127.0.0.1', 8000))   #LocalHost
s.bind(('192.168.2.67', 8000))   #Area51 Pi

print("Lisstening for connections...")
s.listen(1)

connection, address = s.accept()
print("Connected to client", address)


while True:
	connection.send(data)
	
connection.close()
	
