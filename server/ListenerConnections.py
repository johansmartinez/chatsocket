from threading import Thread
from Connection import Connection


class ListenerConnections(Thread):
    def __init__(self, server):
        super(ListenerConnections, self).__init__()
        self._server=server
        self.users=[]

    def broadcast(self, message, socket):
        for user in self.users:
            if user.socket != socket:
                try:
                    user.socket.send(message.encode("utf-8"))
                except:
                    print('No se ha podido envia el mensaje')

    def run(self):
        print(f'Server running on port: {self._server.port}')
        while self._server.listening:
            client, address = self._server.socket.accept()
            print(f'{address[0]} has been connected')
            new_conn= Connection( socket=client, listener=self)
            self.users.append(new_conn)
            new_conn.start()
            if self._server.event.is_set():
                break
        self._server.socket.close()
        print("Server Closed")