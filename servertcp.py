import socket 
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) # by default it is TCP, family as IPv4 and TCP protocol type
s.bind(('localhost', 9999))
print("Waiting For Connection")
s.listen(3)
c, addr = s.accept()
print("Connction Established: ", addr, c)
while True:
    msg_rec = c.recv(1024).decode(encoding="utf-8")
    print("CLient >> ", msg_rec)
    msg_send = input("You >> ")
    c.send(bytes(msg_send, encoding="utf-8"))
    if msg_send == "exit":
        c.close()