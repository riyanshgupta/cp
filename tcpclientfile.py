import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("localhost", 8888))
with open(file="received.txt", encoding="utf-8", mode="w+") as f:
    data = c.recv(1024).decode(encoding="utf-8")
    f.write(data)    