class Heap:

    size = 10

    def __init__(self):
        self.heap = [0]*size
        self.currentPosition = -1

    def insert(self,item):
        if self.isFull():
            print("Heap is Full!!")
            return
        
        self.currentPosition = self.currentPosition + 1
        self.heap[currentPosition] = item
        self.fixUp(self.currentPosition)

    def fixUp(self, index):
        parentIndex = int((index-1)/2)

