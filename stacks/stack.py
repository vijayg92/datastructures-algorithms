class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        if self.isEmpty is not None:
            return 'Size of the stack is : {}'.format(len(self.items))
        return 'Stack is Empty'

    def peek(self):
        if len(self.items) == 0:
            return 'Stack is Empty'
        return '{} is on the peek of stack'.format(self.items[-1])

    def pop(self):
        if self.isEmpty is not None:
            return '{} is poped from the stack'.format(self.items.pop())
        return 'Stack is Empty'

    def push(self, item):
        if self.isEmpty is not None:
            self.items.append(item)
            return '{} is pushed to the stack'.format(item)
        return 'Stack is Empty'

if __name__=='__main__':
    s = Stack()
    print(s.items)
    print(s.peek())
    print(s.push(18))
    print(s.items)
    print(s.push(8))
    print(s.items)
    print(s.push(28))
    print(s.items)
    print(s.push(92))
    print(s.items)
    print(s.size())
    print(s.pop())
    print(s.items)
    print(s.push(101))
    print(s.items)
    print(s.push(301))
    print(s.items)
    print(s.size())
