from threading import Thread

class ListenerInputs(Thread):
    def __init__(self, server):
        super(ListenerInputs, self).__init__()
        self._server=server

    def run(self):
        while  self._server.listening:
            msg = input("(SERVER)-> ")
            if msg == "/close":
                self._server.stop_server()
            elif msg == "/users":
                print(f'online:')
            else:
                self._server.broadcast(f'(SERVER): {msg}', 0)
            
            if self._server.event.is_set():
                break
