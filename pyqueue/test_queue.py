import unittest
from pyqueue import queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = queue.Queue()

    def test_queue(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
