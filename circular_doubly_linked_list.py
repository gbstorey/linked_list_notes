class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #O(1)
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None #O(1)
        self.tail = None #O(1)
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    #O(1) time and space complexity
    def createCDLL(self, nodeValue):
        node = Node(nodeValue)
        self.head = node
        self.tail  = node
        node.prev = node
        node.next = node
        return "The DLL is created successfully."
    #O(n) time complexity, O(1) space complexity
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "The node has been successfully inserted"
    #O(n) time complexity, O(1) space complexity
    def traverseCDLL(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            if tempNode== self.tail:
                break
            tempNode = tempNode.next
     #O(n) time complexity, O(1) space complexity
    def reverseTraverseCDLL(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            if tempNode == self.head:
                break
            tempNode = tempNode.prev
    #O(n) time complexity, O(1) space complexity
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is no node in the DLL."
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                if tempNode.value == nodeValue:
                    return f"{nodeValue} was found at node {index}"
                elif tempNode == self.tail:
                    return "The value does not exist in the CDLL."
                else:
                    tempNode = tempNode.next
                    index += 1
    #O(n) time complexity, O(1) space complexity
    def deleteNode(self, location):
        if self.head == None:
            print("There are no nodes in the CDLL.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None  
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None  
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else: 
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                tempNode.next = tempNode.next.next
                tempNode.next.prev  = tempNode
    #O(n) time complexity, O(1) space complexity
    def deleteCDLL(self):
        if self.head is None:
            print("There are no nodes in this DLL.")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted.")

CDLL = CircularDoublyLinkedList()
print(CDLL.createCDLL(5))
print(CDLL.insertNode(4, 0))
print(CDLL.insertNode(6, -1))
print(CDLL.insertNode(5.5, 2))
CDLL.traverseCDLL()
print(CDLL.searchCDLL(5))
print(CDLL.searchCDLL(70))
# CDLL.reverseTraverseCDLL()
# print([node.value for node in CDLL])