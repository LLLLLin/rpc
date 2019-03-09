import tcpserver
import jsondecode
import rpcstub
class RPCSever(tcpserver.Server,
               jsondecode.JsonRPC,
               rpcstub.RPCStub
                ):
    def __init__(self):
        super(RPCSever,self).__init__()


    def loop(self):
        self.bind_listen(('localhost', 5000))
        while True:
            self.accept_receive()

    def on_msg(self, data):
        self.form_data(data)
        self.call_method()