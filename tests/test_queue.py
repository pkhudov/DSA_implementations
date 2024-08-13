from data_structures.queue import CircBufferQueue
import unittest

class TestQueue(unittest.TestCase):
    
    def test_push(self):
        self.queue = CircBufferQueue(3)
        self.queue.push(1)
        self.assertEqual(self.queue.size, 1)
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(self.queue.array, [1, 2, 3])
        self.assertEqual(self.queue.head, 0)
        self.queue.push(4)
        self.assertEqual(self.queue.array, [4, 2, 3])
        self.assertEqual(self.queue.head, 1)
        self.assertEqual(self.queue.size, 3)
        self.queue.push(5)
        self.assertEqual(self.queue.array, [4, 5, 3])
        self.queue.push(6)
        self.assertEqual(self.queue.array, [4, 5, 6])
        self.assertEqual(self.queue.head, 0)
        self.assertEqual(self.queue.tail, 0)
        self.queue.push(7)
        self.assertEqual(self.queue.array, [7, 5, 6])
        self.assertEqual(self.queue.head, 1)
        self.assertEqual(self.queue.tail, 1)

    def test_dequeue(self):
        self.queue = CircBufferQueue(3)
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.head, 1)
        self.assertEqual(self.queue.size, 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.head, 2)
        self.assertEqual(self.queue.size, 1)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.head, 0)
        self.assertEqual(self.queue.size, 0)
        with self.assertRaises(IndexError):
            self.queue.dequeue()      