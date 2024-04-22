import socket
c = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
c.connect(("localhost", 9999))
while True:
    msg_send = input("You >> ")
    c.send(bytes(msg_send, encoding='utf-8'))
    msg_rec = c.recv(1024).decode(encoding="utf-8")
    if msg_rec== "exit":
        print("server closed the connection")
        c.close()