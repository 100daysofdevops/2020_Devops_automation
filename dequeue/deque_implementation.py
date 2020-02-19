
class Deque(object):

    def __init__(self):
        self.item s =[]

    def addFront(self ,item):
        self.items.append(item)

    def addRear(self ,item):
        self.items.insert(0 ,item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

