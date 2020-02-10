# -*- coding:utf-8 -*-

class Handler(object):

    def __init__(self):
        self.node = 4
        self.next = ()

    def __input__(self, data):
        self.data = data
    
    def __output__(self):
        data = [num for num in self.data if num <= 5]
        print("Node 4.\t", data)