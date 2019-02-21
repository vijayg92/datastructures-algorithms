class Dequeue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addRear(self, item):
        return self.items.append(item)

    def addFront(self, item):
        return self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()


if __name__ == '__main__':
    d = Dequeue()
    d.addFront('Hello')
    d.addRear('World')
    print(d.items)
    d.removeRear()
    print(d.items)
    d.removeFront()
    print(d.items)
