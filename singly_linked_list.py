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



SLL = SinglyLinkedList()
for i in range (0, 6):
    SLL.insertSLL(i, -1)
    print([node.value for node in SLL])