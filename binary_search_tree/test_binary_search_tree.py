import unittest
from binary_search_tree import binary_search_tree as bst


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = bst.BinarySearchTree()
        self.bst.root = bst.Node(5)
        self.bst.root.left = bst.Node(3)
        self.bst.root.left.right = bst.Node(4)
        self.bst.root.left.left = bst.Node(2)
        self.bst.root.left.left.left = bst.Node(1)

    def test_lookup(self):
        self.assertEqual(3, self.bst.lookup(self.bst.root, 3).val)

    def test_insert(self):
        for i in [8, 7, 6, 9, 10]:
            self.assertTrue(self.bst.insert(self.bst.root, i))
        self.assertFalse(self.bst.insert(self.bst.root, 10))

        ret_list = []
        self.bst.traverse_inorder(self.bst.root, ret_list)
        self.assertEqual(ret_list, [i for i in range(1, 11)])

    def test_remove(self):
        self.bst.root.right = bst.Node(8)
        self.bst.root.right.left = bst.Node(7)
        self.bst.root.right.right = bst.Node(9)
        self.bst.root.right.left.left = bst.Node(6)
        self.bst.root.right.right.right = bst.Node(10)

        for i in [1, 3, 5, 6, 8]:
            self.assertTrue(self.bst.remove(self.bst.root, None, i))
        self.assertFalse(self.bst.remove(self.bst.root, None, 8))

        ret_list = []
        self.bst.traverse_inorder(self.bst.root, ret_list)
        self.assertEqual(ret_list, [2, 4, 7, 9, 10])

    def tearDown(self):
        del self.bst
