import socket

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self,address):
        self.socket.bind(address)
        self.socket.listen(5)

    def accept_receive(self):
        (client_socket, address) = self.socket.accept()
        msg = client_socket.recv(1024)
        self.on_msg(msg)
        client_socket.close()
