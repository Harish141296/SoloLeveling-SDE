"""
Docstring for day_33.practise

Singly Linked List: 
Each node contains Value and Pointer (to next Node) 

Big O of common Singly LL: 
Operations          singly Linked List 
1. Insert 
-> at beginning -- S, T = O(1) 
-> at end       -- S, T = O(1) [if tail sorted], else T=O(1)
-> in between   -- T = O(x), S=(1)

2.Remove
-> at beginning -- S, T = O(1) 
-> at end       -- T = O(n), S = O(1)
-> in between   -- T = O(x), S=(1)

3.Access xth node -- T = O(x), S = O(1)

4. Set value of xth node -- T = O(x), S = O(1)

5. Copy         -- S, T = O(n) 

6. Traverse / Search -- T = O(n), S = O(1)


"""
# SinglyNode class creation
class SinglyNode():
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next 

    def __str__(self):
        return str(self.val)

#Nodes values initialization 
Head = SinglyNode(1) 
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7) 

Head.next = A 
A.next = B
B.next = C 

print(Head) 


# Traverse the list - O(n) 
curr = Head 
while curr:
    print(curr)
    curr = curr.next 

# Display linked list - O(n) 
def display(head):
    curr = head
    elements = [] 
    while curr:
        elements.append(str(curr.val))
        curr = curr.next 
    print(" -> ".join(elements))


display(Head)

# Search for Node value - O(n) 
def search(head, val):
    curr = head 
    while curr:
        if val == curr.val:
            return True 
        curr = curr.next 
    return False 

value = 5
if search(Head, value):
    print(f"The value {value} is available in the LinkedList.")
else:
    print(f"The value {value} is not available in the LinkedList.")


# Doubly Linked Lists

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val 
        self.next = next 
        self.prev = prev 

    def __str__(self):
        print(str(self.val))

    
head = tail = DoublyNode(1)
print(head)
print(tail)

def display(head):
    curr = head 
    elements = [] 
    while curr:
        elements.append(curr.val)
        curr = curr.next 
    print(' <-> '.join(elements))
display(head) 

def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node 
    return new_node, tail 

head, tail = insert_at_beginning(head, tail, 3)
display(head)
