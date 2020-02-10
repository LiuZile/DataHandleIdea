# -*- coding:utf-8 -*-

class Handler(object):
    def __init__(self):
        self.node = 2
        self.next = (3, 4)

    
    def __input__(self, data):
        self.data = data

    def __output__(self, ):
        data = [num for num in self.data if num >= 5]
        print("Node 2.\t", data)
        return data