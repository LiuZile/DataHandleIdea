# -*- coding:utf-8 -*-

class Trans(object):

    def __init__(self):
        self.node = 1
        self.next = (2, 3)
    
    def __input__(self, data):
        pass

    def __output__(self, ):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8]
        print("Node 1.\t", self.data)
        return self.data