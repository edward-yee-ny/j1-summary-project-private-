class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode
            
    def insert(self, index, data):
        newNode = Node(data)
        currentIndex = 0
        currentNode = self.head
        while currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1
        newNode.next = currentNode.next
        currentNode.next = newNode
        
    def remove(self, index):
        currentNode = self.head
        currentIndex = 0
        while currentIndex < index - 1:
            currentNode = currentNode.next
            currentIndex += 1
            
        tempNode = currentNode.next
        
        if currentNode.next.next is not None:
            currentNode.next = currentNode.next.next
            
        else:
            currentNode.next = None
            
        return tempNode.data
        