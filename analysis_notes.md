# Complexity Analysis

## Dynamic Array

### Time

- length: O(1) because it is stored in a variable.
- get: O(1) Because access is via index
- set: O(1)
- append: O(n) if resising is required, because we copy all elements to a new array. But amortized it is O(1). Proof via sum of geometric progression formula.
- insert: O(n), because if we insert in the beginning, we need to shift all elements.
- delete: O(n), same reason.

### Space

- O(n) because we store n elements in an array. Even though it can be bigger due to a larger capacity than the size, it is irrelevant: O(n+cn) = O(n).

## Linked List

### Time

- length: O(1) because it is stored in a variable.

Because we have to traverse the list:

- get: O(n)
- set: O(n)
- append: O(n) (Possible O(1): by keeping a reference to the last node)
- insert: O(n)
- delete: O(n)

### Space

- O(n) because for each element we store data and a pointer. O(2n) = O(n)

## Doubly Linked List

### Time

- length: O(1) because it is stored in a variable.

Same as in linked list, however in practice it is double as fast because we can traverse the list from both directions. O(n/2) = O(n)

- get: O(n)
- set: O(n):
- insert: O(n):
- delete: O(n):

- append: O(1) because we keep a reference to the tail

### Space

- O(n) because for each element we store data and 2 pointers. O(3n) = O(n)

## Stack
### Time
All operations are O(1) because we only access the top element.
### Space
O(n)

## Queue

### Time
All operations are O(1) because we maintain pointers to the head and tail.
### Space
O(n)

## Binary Tree

### Time
All except traversal are O(h) where h is the height of the tree. In the worst case h = n, so O(n). If the tree is balanced, h = log(n), so O(log(n)). A random tree on expectation will be balanced. Traversal is O(n) because we have to visit all nodes.
### Space
O(n)


