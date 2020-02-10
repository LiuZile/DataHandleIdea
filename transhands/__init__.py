# -*- coding:utf-8 -*-

class TransHands(object):
    def __init__(self):
        self.firstNode = []

    def __taskFlowers__(self, node):
        level_tasks = dict()
        output = self.tasks[node].__output__()
        level_tasks[self.tasks[node].next] = output

        while(level_tasks != {}):
            tasks = level_tasks.items()
            level_tasks = dict()
            for nodes, output in tasks:
                for node in nodes:
                    self.tasks[node].__input__(output)
                    output = self.tasks[node].__output__()
                    if self.tasks[node].next != []:
                        level_tasks[self.tasks[node].next] = output

    def run(self):
        from transhands import transporter
        from transhands import handler
        trans_mods = [attr for attr in dir(transporter) if "__" not in attr]
        hand_mods = [attr for attr in dir(handler) if "__" not in attr]
        self.tasks = dict()
        for mod in trans_mods:
            obj = getattr(transporter, mod).Trans()
            self.tasks[obj.node] = obj
        for mod in hand_mods:
            obj = getattr(handler, mod).Handler()
            self.tasks[obj.node] = obj
        for node in self.firstNode:
            self.__taskFlowers__(node)