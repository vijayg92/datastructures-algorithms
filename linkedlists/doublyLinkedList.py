class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_data(self, item):
        self.data = item

    def set_next(self, next):
        self.next = next

    def set_prev(self,prev):
        self.prev = prev


class LinkedList:

    def __int__(self):
        self.start = None

    def display_list(self):
        current = self.head
        while current:
            print(current.get_next())
            current = current.get_next()
        pass

    def create_list(self):
        pass

    def search_list(self):
        pass

    def