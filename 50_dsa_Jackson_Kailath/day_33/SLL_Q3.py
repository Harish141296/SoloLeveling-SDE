"""
You are given the head of a Singly Linked list. Write a function that will take the given head as input, reverse the Linked list and return the new head of the reversed Linked List. 

"""

class Node:
    def __init__(self, value):
        self.val = value 
        self.next = None 

    def __str__(self):
        return(f"{self.val} -> {self.next}")
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1 
        if index ==0:
            return self.head 
        if index == self.size -1:
            return self.tail  

    def addAtHead(self, value):
        node = Node(value) 
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            node.next = self.head 
            self.head = node 
        self.size += 1 

    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node 
            self.tail = node 
        else:
            self.tail.next = node 
            self.tail = node 
        self.size += 1  

    def addAtIndex(self, index, value):
        node = Node(value) 
        if index < 0 or index >= self.size:
            return "invalid index"
        if index ==0:
            return self.addAtHead(value)
        if index == self.size -1 :
            return self.addAtTail(value)
        
        prev_node = self.get(index-1)
        temp = prev_node.next 
        prev_node.next = node 
        node.next = temp 
        return(self.head)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 'invalid index'
        if index == 0:
            temp = self.head 
            self.head = temp.next 
            self.size -= 1 
            if self.size == 0:
                self.tail = None 
            return temp.value  
        if index == self.size -1 :
            old_tail = self.tail 
            new_tail = self.get(index -1)
            self.tail = new_tail 
            new_tail.next = None 
            self.size -= 1 
            return old_tail.value 
        prev = self.get(index-1)
        deleted_node = prev.next 
        prev.next = deleted_node.next 
        self.size -= 1 
        return deleted_node.value 

    def deleteTail(self):
        counter = 0 
        prevNode = None 
        current = self.head 
        if self.size == 1:
            self.head = None 
            self.tail = None 
            self.size = 0 
        while counter <self.size : 
            prevNode = current 
            current = current.next 
        prevNode.next = None 
        print(f"Deleted Node: {current.val}")
         