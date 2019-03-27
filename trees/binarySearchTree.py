class Node:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # O(logN) --- If the tree is balanced
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftChild:
            return self.getMin(node.leftChild)
        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)
        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print("{}".format(node.data))

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)
        elif data < node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and node.rightChild:
                print("Leaf remove is deleted")
                del node
                return None
            if not node.leftChild:
                print("Removing node with single right child")
                tempNode = node.rigtChild
                del node
                return tempNode
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode

            print("Removing node with two children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


if __name__=='__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(13)
    bst.insert(5)
    bst.insert(1)
    print("Maximum Value is {}".format(bst.getMaxValue()))
    print("Minimum Value is {}".format(bst.getMinValue()))
    print("InOrder Tree Traversal")
    bst.traverse()
    bst.remove(5)
    bst.traverse()
