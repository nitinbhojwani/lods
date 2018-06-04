import unittest
from doubly_linked_list import doubly_linked_list


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.doubly_linked_list = doubly_linked_list.DoublyLinkedList()
        for i in range(5, 10):
            self.doubly_linked_list.insert(i, in_start=False)
        for i in range(4, -1, -1):
            self.doubly_linked_list.insert(i)

    def test_lookup(self):
        self.assertEqual(self.doubly_linked_list.lookup(0), 0)
        self.assertEqual(self.doubly_linked_list.lookup(9), 9)
        self.assertEqual(self.doubly_linked_list.lookup(5), 5)

    def test_remove(self):
        self.assertTrue(self.doubly_linked_list.remove(9))
        self.assertFalse(self.doubly_linked_list.remove(9))

    def test_insert_before(self):
        self.assertTrue(self.doubly_linked_list.insert_before(10, 9))

    def test_insert_after(self):
        self.assertTrue(self.doubly_linked_list.insert_after(10, 9))

    def tearDown(self):
        del self.doubly_linked_list
