# -*- coding:utf-8 -*-

class Trans(object):

    def __init__(self):
        self.node = 3
        self.next = (4,)
    
    def __input__(self, data):
        self.data = data + [88, 99, 100, 120]

    def __output__(self, ):
        print("Node 3.\t", self.data)
        return self.data