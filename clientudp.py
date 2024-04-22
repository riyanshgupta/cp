import socket
c=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto("Hii".encode("utf-8"), ("localhost", 12345))
data, addr = c.recvfrom(44447)
print(str(data))
c.close()