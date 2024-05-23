# Complexity Analysis: Dynamic Array

## Time

- length: O(1) because it is stored in a variable.
- get: O(1) Because access is via index
- set: O(1)
- append: O(n) if resising is required, because we copy all elements to a new array. But amortized it is O(1). Proof via sum of geometric progression formula.
- insert: O(n), because if we insert in the beginning, we need to shift all elements.
- delete: O(n), same reason.

## Space

- O(n) because we store n elements in an array. Even though it can be bigger due to a larger capacity than the size, it is irrelevant: O(n+cn) = O(n).
