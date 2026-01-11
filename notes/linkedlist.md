1. What is a Linked List?
   Linked List constructed with attributes value and next, to avoid the limitations of Array, value carries that list's value and next points to the next object or None.

2. What is a Node?
   Node actually a single class with attributes value and next.

3. What is the head?
   Head defines the starting point of LinkedList.

4. One advantage over arrays?
   Inserting node in the middle takes O(x) compares the Array, and its dynamic.

5. One disadvantage compared to arrays?
   Slower accessing Time.

6. What problem does a linked list solve?
   It solves the insertion at the middle of the array, which takes only O(x) compares to array insertion where rest of element were moved one by one which takes O(n).

7. Why can’t arrays solve it well?
   Array takes only O(1) when we insert at the beginning or end, but while inserting in the middle, it first select all the remining item and move all of it to one cell ahead and then insert the required item in the mentioned index.

8. What happens if I lose the head?
   By accidently making the self.head = None without storing the head in someother object, will result in losing all of its data and no recovery.

9. Why is random access slow?
   for Random access, it has to check each and every node, for best case if its found at the first index it will return that item else if the wanted item in last -1 then it has to iterated over each and every node starting from head, so it cause slowness.

10. One real-world analogy (not textbook)
    In youtube or any browser, we can go front and back with clicking the arrow, in the backend i believe they have implemented this linked list to carry the memory address of that history to take you quickly front and back.
