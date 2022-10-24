class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #O(1)
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None #O(1)
        self.tail = None #O(1)
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #O(1) time and space complexity
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail  = node
        return "The DLL is created successfully."
    #O(n) time complexity, O(1) space complexity
    def insertNode(self, value, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(value)

            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next=newNode
                self.tail = newNode

            else:
                traversalNode = self.head
                index = 0
                while index < location-1:
                    traversalNode = traversalNode.next
                    index += 1

                nextNode = traversalNode.next
                nextNode.prev = newNode
                newNode.next = nextNode
                newNode.prev = traversalNode
                traversalNode.next = newNode
    #O(n) time complexity, O(1) space complexity
    def traverseDLL(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
    #O(n) time complexity, O(1) space complexity
    def reverseTraverseDLL(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev
    #O(n) time complexity, O(1) space complexity
    def searchDLL(self, nodeValue):
        tempNode = self.head
        index = 0
        while tempNode:
            if tempNode.value == nodeValue:
                return f"{nodeValue} was found at node {index}"
            else:
                tempNode = tempNode.next
                index += 1
        return "The value does not exist in the DLL"
    #O(n) time complexity, O(1) space complexity
    def deleteNode(self, location):
        if self.head == None:
            print("There is no node to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                tempNode.next = tempNode.next.next
                tempNode.next.prev  = tempNode
            print("The node has been deleted.")
    #O(n) time complexity, O(1) space complexity
    def deleteDLL(self):
        if self.head is None:
            print("There are no nodes in this DLL.")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted.")

DLL = DoublyLinkedList()
DLL.createDLL(5)
DLL.insertNode(4, 0)
DLL.insertNode(6, -1)
DLL.insertNode(5.5, 2)
DLL.traverseDLL()
DLL.reverseTraverseDLL()
print(DLL.searchDLL(5.5))
print(DLL.searchDLL(70))
DLL.deleteNode(0)
DLL.traverseDLL()