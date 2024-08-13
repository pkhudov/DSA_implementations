import unittest
from data_structures.doubly_linked_list import Doubly_Linked_List

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.empty_list = Doubly_Linked_List()
        self.single_item_list = Doubly_Linked_List([1])
        self.multi_item_list = Doubly_Linked_List([1, 2, 3, 4, 5])

    def test_initialization(self):
        self.assertIsNotNone(self.empty_list.head)
        self.assertIsNotNone(self.empty_list.tail)
        self.assertEqual(self.empty_list.length, 0)
        self.assertEqual(self.single_item_list.length, 1)
        self.assertEqual(self.single_item_list.head.data, 1)
        self.assertEqual(self.single_item_list.tail.data, 1)
        self.assertEqual(self.multi_item_list.length, 5)
        self.assertEqual(self.multi_item_list.head.data, 1)
        self.assertEqual(self.multi_item_list.tail.data, 5)

    def test_get(self):
        with self.assertRaises(IndexError):
            self.empty_list.get(0)
        self.assertEqual(self.single_item_list.get(0), 1)
        self.assertEqual(self.multi_item_list.get(0), 1)
        self.assertEqual(self.multi_item_list.get(2), 3)
        self.assertEqual(self.multi_item_list.get(4), 5)
        with self.assertRaises(IndexError):
            self.multi_item_list.get(5)

    def test_set(self):
        with self.assertRaises(IndexError):
            self.empty_list.set(10, 0)
        self.single_item_list.set(10, 0)
        self.assertEqual(self.single_item_list.get(0), 10)
        self.multi_item_list.set(10, 2)
        self.assertEqual(self.multi_item_list.get(2), 10)
        with self.assertRaises(IndexError):
            self.multi_item_list.set(10, 5)

    def test_append(self):
        self.empty_list.append(1)
        self.assertEqual(self.empty_list.length, 1)
        self.assertEqual(self.empty_list.get(0), 1)
        self.single_item_list.append(2)
        self.assertEqual(self.single_item_list.length, 2)
        self.assertEqual(self.single_item_list.get(1), 2)
        self.multi_item_list.append(6)
        self.assertEqual(self.multi_item_list.length, 6)
        self.assertEqual(self.multi_item_list.get(5), 6)

    def test_insert(self):
        with self.assertRaises(IndexError):
            self.empty_list.insert(1, 1)
        self.empty_list.insert(1, 0)
        self.assertEqual(self.empty_list.length, 1)
        self.assertEqual(self.empty_list.get(0), 1)
        self.single_item_list.insert(2, 1)
        self.assertEqual(self.single_item_list.length, 2)
        self.assertEqual(self.single_item_list.get(1), 2)
        self.multi_item_list.insert(10, 2)
        self.assertEqual(self.multi_item_list.length, 6)
        self.assertEqual(self.multi_item_list.get(2), 10)

    def test_delete(self):
        with self.assertRaises(IndexError):
            self.empty_list.delete(0)
        self.single_item_list.delete(0)
        self.assertEqual(self.single_item_list.length, 0)
        self.assertIsNone(self.single_item_list.head)
        self.multi_item_list.delete(2)
        self.assertEqual(self.multi_item_list.length, 4)
        self.assertEqual(self.multi_item_list.get(2), 4)
        self.multi_item_list.delete(0)  
        self.assertEqual(self.multi_item_list.length, 3)
        self.assertEqual(self.multi_item_list.get(0), 2)
        self.multi_item_list.delete(2)
        self.assertEqual(self.multi_item_list.length, 2)
        self.assertEqual(self.multi_item_list.get(1), 4)

    def test_traverse_forward(self):
        self.assertEqual(self.empty_list.traverse_forward(), 'None<->None')
        self.assertEqual(self.single_item_list.traverse_forward(), 'None<->1<->None')
        self.assertEqual(self.multi_item_list.traverse_forward(), 'None<->1<->2<->3<->4<->5<->None')

    def test_traverse_backward(self):
        self.assertEqual(self.empty_list.traverse_backward(), 'None<->None')
        self.assertEqual(self.single_item_list.traverse_backward(), 'None<->1<->None')
        self.assertEqual(self.multi_item_list.traverse_backward(), 'None<->5<->4<->3<->2<->1<->None')

if __name__ == '__main__':
    unittest.main()

# Tests are ChatGPT generated