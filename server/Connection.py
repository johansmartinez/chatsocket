from socket import socket
from threading import Thread


class Connection(Thread):
    def __init__(self, socket, listener):
        super(Connection, self).__init__()
        self.username=""
        self.socket=socket
        self.listener=listener
        self.open= True

    def run(self):
        self.socket.send("@username:".encode("utf-8"))
        username = self.socket.recv(1024).decode('utf-8')
        self.username=username
        print(f"({username}) has login")
        while self.open:
            try:
                msg = self.socket.recv(1024)
                if msg.lower().decode('utf-8') == "bye":
                    self.listener.removeUser(self)
                    print(f'({self.username}): has logout')
                else:
                    msg= f'({self.username}): {msg.decode("utf-8")}'
                    self.listener.broadcast(msg, self.socket)
                    print(msg)
            except:
                self.open=False
                self.listener.removeUser(self)