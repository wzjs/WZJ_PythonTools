import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(("127.0.0.1",9999))
# while True:
# 	_input = input("please send data:")
# 	s.send(_input.encode("utf-8"))
# 	data_get = s.recv(1024)
# 	if not data_get:
# 		break
# 	print(data_get.decode("utf-8"))
# s.close()

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b'Hello,server',('127.0.0.1',9999))
print(s.recv(1024))