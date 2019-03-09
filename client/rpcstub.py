import json

class RPCStub:
    def __getattr__(self, item):
        def format_data(*args, **kwargs):
            d = {'method_name': item,
                 'method_args': args,
                 'method_kwargs': kwargs,
                 }
            self.send(json.dumps(d).encode('utf-8'))
        setattr(self, item, format_data)
        return format_data
