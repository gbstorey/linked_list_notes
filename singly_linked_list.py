class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #O(1)

class SinglyLinkedList:
    def __init__(self):
        self.head = None #O(1)
        self.tail = None #O(1)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #insertion algorithm #O(n) time complexity, O(1) space complexity
    def insertSLL(self, value, location):
        newNode = Node(value)
        #empty linked list
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            #beginning of linked list
            if location == 0:
                #self.head is first node's physical location
                #set new node's reference to location of first node
                newNode.next = self.head
                #update head to new node's physical location
                self.head = newNode
            #end of linked list
            elif location == -1:
                #set new node's pointer to None
                newNode.next = None
                #tail's reference becomes new node
                self.tail.next = newNode
                #Reference the new tail to the new node
                self.tail = newNode
            #inside linked list (after target location)
            else:
                #create new node to traverse through SLL
                traversalNode = self.head
                index = 0
                #find current element
                while index < location-1:
                    traversalNode = traversalNode.next
                    index += 1
                #find next item in list
                nextNode = traversalNode.next
                #temp node next reference is newNode
                traversalNode.next = newNode
                #new node's reference is next node
                newNode.next = nextNode
                #insert between current and next node
                if traversalNode == self.tail:
                    self.tail = newNode
    #traversal algorithm #O(n) time complexity, O(1) space complexity
    def traverseSLL(self):
        if self.head:
            node = self.head
            while node:
                print(node.value)
                node = node.next
        else:
            print("The SLL does not exist.")
    #searching in single linked list #O(n) time complexity, O(1) space complexity
    def searchSLL(self, value):
        if self.head:
            node = self.head
            index = 0
            while node:
                if node.value == value:
                    print(f"{value} is found at index {index}.")
                    break
                node = node.next
                index += 1
        else:
            print("The SLL does not exist, or the value is not inside.")
    #deleting a node in single linked list #O(n) time complexity, O(1) space complexity
    def deleteSLL(self, location):
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else: 
                self.head=self.head.next
        elif location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        else: 
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSLL(self): #deleteing 
        if self.head:
            self.head = None
            self.tail = None
        else:
            print("The SLL does not exist.")
SLL = SinglyLinkedList()
for i in range(0,10):
    SLL.insertSLL(i, -1)
SLL.traverseSLL()
SLL.searchSLL(4)
SLL.deleteSLL(-1)
SLL.deleteEntireSLL()
SLL.traverseSLL()


