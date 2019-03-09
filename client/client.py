import socket

class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self,address):
        self.socket.connect(address)

    def send(self,data):
        self.socket.send(data)
