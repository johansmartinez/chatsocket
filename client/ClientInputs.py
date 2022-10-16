from threading import Thread

class ClientInputs(Thread):
    def __init__(self, client):
        super(ClientInputs, self).__init__()
        self.client=client

    def run(self):
        while  self.client.listener :
            msg = input("-> ")
            if msg.lower() == "bye":
                self.client.stop_client()
            else:
                self.client.socket.send(msg.encode("utf-8"))
            if self.client.event.is_set():
                break