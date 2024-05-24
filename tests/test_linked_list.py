import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_initialization(self):
        ll_empty = LinkedList()
        self.assertEqual(ll_empty.length, 0)
        self.assertIsNone(ll_empty.head)  # Adjusted this line

        ll_elements = LinkedList([1, 2, 3])
        self.assertEqual(ll_elements.length, 3)
        self.assertEqual(ll_elements.head.data, 1)
        self.assertEqual(ll_elements.head.next.data, 2)
        self.assertEqual(ll_elements.head.next.next.data, 3)

    def test_get(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(2), 3)
        with self.assertRaises(IndexError):
            ll.get(3)

    def test_set(self):
        ll = LinkedList([1, 2, 3])
        ll.set(10, 0)
        self.assertEqual(ll.get(0), 10)
        ll.set(20, 1)
        self.assertEqual(ll.get(1), 20)
        ll.set(30, 2)
        self.assertEqual(ll.get(2), 30)
        with self.assertRaises(IndexError):
            ll.set(40, 3)

    def test_insert(self):
        ll = LinkedList([1, 2, 3])
        ll.insert(5, 0)
        self.assertEqual(ll.get(0), 5)
        self.assertEqual(ll.get(1), 1)
        ll.insert(15, 2)
        self.assertEqual(ll.get(2), 15)
        self.assertEqual(ll.get(3), 2)
        ll.insert(35, 5)
        self.assertEqual(ll.get(5), 35)
        self.assertEqual(ll.get(4), 3)
        with self.assertRaises(IndexError):
            ll.insert(45, 7)

    def test_delete(self):
        ll = LinkedList([1, 2, 3])
        ll.delete(0)
        self.assertEqual(ll.get(0), 2)
        self.assertEqual(ll.get(1), 3)
        with self.assertRaises(IndexError):
            ll.delete(2)
        ll.delete(1)
        self.assertEqual(ll.get(0), 2)
        with self.assertRaises(IndexError):
            ll.get(1)
        with self.assertRaises(IndexError):
            ll.delete(5)

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.get(0), 1)
        ll.append(2)
        self.assertEqual(ll.get(1), 2)

        ll2 = LinkedList([1, 2, 3])
        ll2.append(4)
        self.assertEqual(ll2.get(3), 4)

    def test_traverse(self):
        ll_empty = LinkedList()
        ll_single = LinkedList([5])
        ll_multiple = LinkedList([1, 2, 3])

        self.assertEqual(str(ll_empty), "None")
        self.assertEqual(str(ll_single), "5->None")
        self.assertEqual(str(ll_multiple), "1->2->3->None")

if __name__ == '__main__':
    unittest.main()

# Tests are ChatGPT generated