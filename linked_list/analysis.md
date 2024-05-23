# Complexity Analysis: Linked List

## Time

- length: O(1) because it is stored in a variable.

Because we have to traverse the list:

- get: O(n)
- set: O(n)
- append: O(n) (Possible O(1): by keeping a reference to the last node)
- insert: O(n)
- delete: O(n)

## Space

- O(n) because for each element we store data and a pointer. O(2n) = O(n)
