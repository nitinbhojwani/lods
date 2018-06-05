import unittest
from binary_tree import binary_tree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.binary_tree = binary_tree.BinaryTree()
        self.binary_tree.root = binary_tree.Node(5)
        self.binary_tree.root.left = binary_tree.Node(3)
        self.binary_tree.root.left.right = binary_tree.Node(4)
        self.binary_tree.root.left.left = binary_tree.Node(2)
        self.binary_tree.root.left.left.left = binary_tree.Node(1)
        self.binary_tree.root.right = binary_tree.Node(8)
        self.binary_tree.root.right.left = binary_tree.Node(7)
        self.binary_tree.root.right.right = binary_tree.Node(9)
        self.binary_tree.root.right.left.left = binary_tree.Node(6)
        self.binary_tree.root.right.right.right = binary_tree.Node(10)

    def test_traverse_inorder(self):
        ret_list = []
        self.binary_tree.traverse_inorder(self.binary_tree.root, ret_list)
        self.assertEqual(ret_list, [i for i in range(1, 11)])

    def test_traverse_postorder(self):
        ret_list = []
        self.binary_tree.traverse_postorder(self.binary_tree.root, ret_list)
        self.assertEqual(ret_list, [1, 2, 4, 3, 6, 7, 10, 9, 8, 5])

    def test_traverse_preorder(self):
        ret_list = []
        self.binary_tree.traverse_preorder(self.binary_tree.root, ret_list)
        self.assertEqual(ret_list, [5, 3, 2, 1, 4, 8, 7, 6, 9, 10])

    def tearDown(self):
        del self.binary_tree
