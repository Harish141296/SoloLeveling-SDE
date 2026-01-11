"""
Design a Singly Linked List class that has a head and tail. Every node is to have two attributes: values: The value of the current Node, and next: a pointer to the next node. The linked list is to be 0-indexed. The class should support the following: 

* SinglyLinkedList() - initializes the SinglyLinkedList object.
* get(index) - Get the value of the indexth node. If the index is invalid, return -1.
* addAtHead(value) - Add a node of given value before the first element of the linked list.
* addAtTail(value) - Add a node of given value at the last element of the linked list.
* addAtIndex(index, value) - Add a node of given value before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, don't insert the node. 
* deleteAtIndex(index) - Delete the indexth node in the linked list, if the index is valid, else nothing happens.
"""

"""
Demo class blueprint

class Node{
    constructor(value){
    this.val = value;
    this.next = null;
    }
}

class SinglylinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }
}
// Add instance methods
// get(index), unshift(value), push(value)
* complexity: 
T = O(index); Worst Case: O(n) ; 
S = O(1)
// addAtHead(value) -> 
* complexity:
T = O(1)
S = O(1)
// addAtTail(value) -> 
* complexity:
T = O(1) ; if tail is not tracked then O(n)
S = O(1)
// addAtIndex(index, value) ->
T = Worst case -> O(n), bestcase -> O(1) either the position at head or tail 
S = O(1) 
// deleteAtIndex(index) -> 
T = O(n) -> Worstcase -> index inbetween head/tail -> else O(1) 
S = O(1)

"""


class Node:
    def __init__(self, value):
        self.val = value 
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        counter = 0 
        current = self.head 
        while counter != index:
            current = current.next 
            counter += 1 
        return current 
    
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
        if index < 0 or index > self.size :
            return 'invalid index'
        if index == self.size:
            return self.addAtTail(value)
        if index == 0:
            return self.addAtHead(value)
        node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = node 
        node.next = temp 
        self.size += 1 
    
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
        if index == self.size -1:
            old_tail = self.tail
            new_tail = self.get(index - 1)
            self.tail = new_tail 
            new_tail.next = None 
            self.size -= 1 
            return old_tail.value 
        prev = self.get(index - 1)
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
        while counter < self.size: # 0 < 3 --> 1 <3 ,2<3,3<3
            prevNode = current 
            current = current.next 
        prevNode.next = None 
        print(f"Deleted Node: {current.val}")

