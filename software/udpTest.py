# udpTest
import socket 
server = ('10.160.0.105', 6969)
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.sendto(str.encode('hello there'), server)
s.close()
print('\ndone\n')
