import socket
from ListenerConnections import ListenerConnections
from ListenerInputs import ListenerInputs
from threading import Event
import os


class Server():
    def __init__(self):
        self.host_name = '127.0.0.1'
        self.port = 5100
        self.socket = socket.socket()
        self.socket.bind((self.host_name, self.port))
        self.socket.listen(5)
        self.listening = True

        self.event=Event()

        self.connections=ListenerConnections(self)
        self.inputs=ListenerInputs(self)
        self.connections.start()
        self.inputs.start()

    def broadcast(self,message, _user):
        self.connections.broadcast(message, _user)

    def stop_server(self):
        self.event.set()
        self.listening=False
        print("Server Closed")
        os._exit(os.X_OK) 
