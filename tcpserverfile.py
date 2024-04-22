import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8888))
s.listen(1)
print("Waiting for connection")
c, addr = s.accept()
print('Connection Established with', addr)
with open("rec.txt", encoding="utf-8", mode="r") as f:
    a = f.read()
    c.send(bytes(a, encoding="utf-8"))