"""
Docstring for 50_dsa_Jackson_Kailath.day_33.SLL_Q2
Question:
You are given the head of a Sorted Singly Linked list. Write a function that will take the given head as input, delete all nodes that have a value that is already the value of another node so that each value appears 1 time only and return the linked list, which is still to be a sorted linked list.

Test Cases: 
1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> Null  # O/P : 1 -> 2 -> 3 -> 4 -> Null 
"""

class Node:
    def __init__(self, value):
        self.val = value 
        self.next = None 
    def __str__(self):
        return(f"{self.val}->{self.next}")

class SinglyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0 

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1 
        if index == 0: return self.head
        if index == self.size -1: return self.tail 

        counter = 0 
        current = self.head 
        while counter == index:
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
        if index < 0 or index >= self.size :
            return 'invalid index'
        if index == 0: 
            return self.addAtHead(value) 
        if index == self.size -1 :
            return self.addAtTail(value) 

        node = Node(value)
        prev = self.get(index)
        temp = prev.next 
        prev.next = node
        node.next = temp 
        self.size += 1 

    def deleteAtIndex(self, index):
        if index <0 or index >= self.size:
            return 'invalid index'
        if index == 0:
            curr = self.head 
            curr.next = self.head 
            return curr.val
        
        if index == self.size -1 :
            temp = self.tail
            prev = self.get(self.size - 2)
            prev.next = None 
            if self.size == 1:
                self.tail = None
            else:   
                self.tail = prev
            return temp.val
        # a -> b -> c -> d -> e -> Null
        curr = self.get(index)
        prev = self.get(index - 1)
        # temp = prev.next
        prev.next = curr.next
        return curr.val
    
    def duplicate_remover_OWN(self):
        if self.size == 1:
            return self.head 
        current = self.head 
        counter = 0
        distinct_node = self.head 
        while counter < self.size: 
            if current.next == None: break
            # print(current.val)
            if current.val == current.next.val:
                # duplicate 
                current.next = current.next.next
            else:
                current = current.next
            counter += 1
        print(self.head)


    def removeDupes_1(self):
        curr = self.head 
        while curr:
            nextDistinctVal = curr.next 
            while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
                nextDistinctVal = nextDistinctVal.next 
            curr.next = nextDistinctVal
            curr = nextDistinctVal
        return self.head

    def __str__(self):
        return(f"{self.head}")
    

    
if __name__ == '__main__':
    # 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> Null  # O/P : 1 -> 2 -> 3 -> 4 -> Null 
    sll = SinglyLinkedList() 
    sll.addAtHead(1)
    sll.addAtTail(1)
    sll.addAtTail(2)
    sll.addAtTail(2)
    sll.addAtTail(3)
    sll.addAtTail(4)
    sll.addAtTail(4)
    sll.addAtTail(4)
    print(sll)
    sll.duplicate_remover_OWN()
    print(sll)
    sll.addAtHead(1)
    sll.addAtTail(1)
    sll.addAtTail(2)
    sll.addAtTail(2)
    sll.addAtTail(3)
    sll.addAtTail(4)
    sll.addAtTail(4)
    sll.addAtTail(4)
    sll.removeDupes_1()
    print(sll)
    # A = Node(1)
    # B = Node(2)
    # C = Node(2)
    # D = Node(3)
    # E = Node(4)
    # F = Node(4)
    # G = Node(4)

    # A.next = B 
    # B.next = C 
    # C.next = D 
    # D.next = E
    # E.next = F
    # F.next = G

    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(E)
    # print(F)
    # print(G)



