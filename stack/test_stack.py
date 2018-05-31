import unittest
from stack import stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = stack.Stack()

    def test_queue(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
