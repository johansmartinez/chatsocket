import os
import socket
from threading import Event, Thread

from ClientInputs import ClientInputs

class ClientListener(Thread):
    def __init__(self):
        super(ClientListener, self).__init__()
        self.host_name = "127.0.0.1"
        self.port=5100
        self.listener=True
        self.event=Event()
        self.inputs= ClientInputs(self)
        self.socket=socket.socket()
        self.socket.connect((self.host_name, self.port))
        self.start()
    
    def run(self):
        print("iniciando cliente")
        while self.listener:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if message == "@username:":
                    self.socket.send(self.getUsername().encode("utf-8"))
                    self.inputs.start()
                else:
                    print(message)
                if self.event.is_set():
                    break
            except:
                self.stop_client()
        self.socket.close()

    def getUsername(self):    
        return input("Ingrese su nombre de usuario: ")

    def stop_client(self):
        self.event.set()
        self.listening=False
        print("Client Closed")
        os._exit(os.X_OK) 






