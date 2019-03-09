import rpcclient

RpcC = rpcclient.RpcClient()
address =('127.0.0.1', 5000)
RpcC.connect(address)
RpcC.foo(1, 2, c=3)
