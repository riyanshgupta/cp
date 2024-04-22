import socket
s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind(("localhost", 12345))
while True:
    data, addr = s.recvfrom(4444)
    print(str(data), f" from address: {addr}")
    msg = bytes("Hello".encode("utf-8"))
    s.sendto(msg, addr)
    