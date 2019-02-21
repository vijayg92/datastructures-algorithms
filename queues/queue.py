class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        if self.isEmpty is not None:
            return 'Size of the Queue is : {}'.format(len(self.items))
        return 'Queue is Empty'

    def enqueue(self, item):
        if self.isEmpty is not None:
            self.items.insert(0, item)
            return '{} is enqueued in the Queue'.format(item)
        return 'Queue is Empty'

    def dequeue(self):
        if self.isEmpty is not None:
            return '{} is dequeued from the Queue'.format(self.items.pop())
        return 'Queue is Empty'


    def peek(self):
        if len(self.items) == 0:
            return 'Queue is Empty'
        return '{} is on the peek of the Queue'.format(self.items[0])


if __name__=='__main__':
    q = Queue()
    print(q.items)
    print(q.peek())
    print(q.enqueue(18))
    print(q.items)
    print(q.enqueue(8))
    print(q.items)
    print(q.enqueue(28))
    print(q.items)
    print(q.enqueue(92))
    print(q.items)
    print(q.size())
    print(q.dequeue())
    print(q.items)
    print(q.enqueue(101))
    print(q.items)
    print(q.enqueue(301))
    print(q.items)
    print(q.size())
