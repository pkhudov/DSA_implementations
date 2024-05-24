import unittest
from data_structures.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_initialization_with_capacity(self):
        array = DynamicArray(5)
        self.assertEqual(array.size, 0)
        self.assertEqual(array.capacity, 5)
        self.assertEqual(str(array), "[]")
    
    def test_get(self):
        array = DynamicArray([1, 2, 3])
        self.assertEqual(array.get(1), 2)

    def test_append(self):
        array = DynamicArray()
        array.append(10)
        self.assertEqual(array.size, 1)
        self.assertEqual(array.capacity, 3)
        self.assertEqual(str(array), "[10]")

    def test_insert(self):
        array = DynamicArray([1, 2, 3])
        array.insert(5, 1)
        self.assertEqual(array.size, 4)
        self.assertEqual(array.capacity, 6)
        self.assertEqual(str(array), "[1, 5, 2, 3]")
    
    def test_insert_last(self):
        array = DynamicArray([1, 2, 3])
        array.insert(5, 3)
        self.assertEqual(array.size, 4)
        self.assertEqual(array.capacity, 6)
        self.assertEqual(str(array), "[1, 2, 3, 5]")
    
    def test_insert_first(self):
        array = DynamicArray([1, 2, 3])
        array.insert(5, 0)
        self.assertEqual(array.size, 4)
        self.assertEqual(array.capacity, 6)
        self.assertEqual(str(array), "[5, 1, 2, 3]")

    def test_delete(self):
        array = DynamicArray([1, 2, 3, 4])
        array.delete(2)
        self.assertEqual(array.size, 3)
        self.assertEqual(array.capacity, 4)
        self.assertEqual(str(array), "[1, 2, 4]")
    
    def test_delete_last(self):
        array = DynamicArray([1, 2, 3, 4])
        array.delete(3)
        self.assertEqual(array.size, 3)
        self.assertEqual(array.capacity, 4)
        self.assertEqual(str(array), "[1, 2, 3]")
    
    def test_delete_first(self):
        array = DynamicArray([1, 2, 3, 4])
        array.delete(0)
        self.assertEqual(array.size, 3)
        self.assertEqual(array.capacity, 4)
        self.assertEqual(str(array), "[2, 3, 4]")

    def test_set(self):
        array = DynamicArray([1, 2, 3])
        array.set(99, 1)
        self.assertEqual(array.size, 3)
        self.assertEqual(str(array), "[1, 99, 3]")

    def test_resize(self):
        array = DynamicArray([1, 2, 3])
        array.append(4)
        self.assertEqual(array.size, 4)
        self.assertEqual(array.capacity, 6)
        self.assertEqual(len(array.array), array.capacity) 
        self.assertEqual(str(array), "[1, 2, 3, 4]")

if __name__ == '__main__':
    unittest.main()

# Tests are ChatGPT generated