import client
import rpcstub

class RpcClient(client.Client,
                rpcstub.RPCStub):
    def __init__(self):
        super(RpcClient,self).__init__()