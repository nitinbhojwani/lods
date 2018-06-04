import unittest
from linked_list import linked_list


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = linked_list.LinkedList()
        for i in range(5, 10):
            self.linked_list.insert(i, insert_in_start=False)
        for i in range(4, -1, -1):
            self.linked_list.insert(i)

    def test_lookup(self):
        self.assertEqual(self.linked_list.lookup(0), 0)
        self.assertEqual(self.linked_list.lookup(9), 9)
        self.assertEqual(self.linked_list.lookup(5), 5)

    def test_remove(self):
        self.assertTrue(self.linked_list.remove(9))
        self.assertFalse(self.linked_list.remove(9))

    def test_insert(self):
        self.assertTrue(self.linked_list.insert(10))
        self.assertFalse(self.linked_list.insert(10))

    def tearDown(self):
        del self.linked_list
