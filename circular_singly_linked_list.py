class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #O(1)

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None #O(1)
        self.tail = None #O(1)

    def __iter__(self): 
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    #Create circular singly linked list. Create a single node with nodeValue that references itself. Head and tail reference this node.
    # O(1) time and space complexity.
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."
    def insertCSLL(self, value, location):
        newNode = Node(value)
        #if list is empty
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            #beginning of linked list:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                #create link between last node and new node
                self.tail.next = newNode
            elif location == -1:
                #create link between last node and first node
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                #find node before target location.
                while index < location -1:                 #O(n) time complexity. O(1) space complexity.
                    tempNode = tempNode.next
                    index += 1
                #establish reference to the node after target location.
                nextNode = tempNode.next
                #establish reference to newNode from previous node.
                tempNode.next = newNode
                #connect the newNode to the node after the target location.
                newNode.next = nextNode
            return "The node has been inserted."
    def traverseCSLL(self):
        if not self.head:
            print("There is not any element for traversal.")
        node = self.head
        while node:              # O(n) time complexity, O(1) space complexity
            print(node.value)
            if node == self.tail:
                break
            node = node.next
    def searchCSLL(self, value):
        if self.head is None:
            print("There is not any node in this CSLL.")
        else:
            tempNode = self.head
            index = 0
            while tempNode:                   #time complexity O(n), space complexity O(1)
                if tempNode.value == value:
                    print( f"{value} was found at node {index}." )
                    break
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    print("The value was not found in this CSLL.")
                    break
                index += 1
    def deleteNode(self, location):
        if self.head == None:
            print("There is no node to delete.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next=self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:                     #O(n) time complexity, O(1) space complexity
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteCSLL(self):
        if self.head:               #O(1) time complexity, O(1) space complexity
            self.head = None
            self.tail.next = None
            self.tail = None
        else:
            print("There is no CSLL to delete.")

csll = CircularSinglyLinkedList()
csll.createCSLL(5)
csll.insertCSLL(4, 0)
csll.insertCSLL(6, -1)
csll.insertCSLL(5.5, 2)
csll.searchCSLL(5.5)
csll.deleteNode(2)
csll.traverseCSLL()