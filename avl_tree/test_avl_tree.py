import unittest
from avl_tree import avl_tree


class TestAvlTree(unittest.TestCase):
    def setUp(self):
        self.avl_tree = avl_tree.AvlTree()
        self.avl_tree.root = avl_tree.Node(10)

        self.avl_tree.root.left = avl_tree.Node(8)
        self.avl_tree.root.right = avl_tree.Node(13)

        self.avl_tree.root.left.right = avl_tree.Node(9)
        self.avl_tree.root.left.left = avl_tree.Node(7)
        self.avl_tree.root.left.left.left = avl_tree.Node(6)

        self.avl_tree.root.right.left = avl_tree.Node(12)
        self.avl_tree.root.right.right = avl_tree.Node(14)
        self.avl_tree.root.right.left.left = avl_tree.Node(11)
        self.avl_tree.root.right.right.right = avl_tree.Node(15)

        self.avl_tree.root.height = 4
        self.avl_tree.root.left.height = 3
        self.avl_tree.root.left.left.height = 2
        self.avl_tree.root.right.height = 3
        self.avl_tree.root.right.left.height = 2
        self.avl_tree.root.right.right.height = 2

    def test_lookup(self):
        self.assertEqual(10, self.avl_tree.lookup(self.avl_tree.root, 10).val)
        self.assertTrue(self.avl_tree.lookup(self.avl_tree.root, 3) is None)

    def test_insert(self):
        # insert 1-5 and 16-20
        for i in [1, 5, 4, 3, 2, 16, 17, 18, 20, 19]:
            self.avl_tree.insert(i)
            self.assertEqual(self.avl_tree.lookup(
                self.avl_tree.root, i).val, i)

        # insert duplicates
        for i in range(1, 21):
            self.avl_tree.insert(i)

        ret_list = []
        self.avl_tree.traverse_inorder(self.avl_tree.root, ret_list)
        self.assertEqual(ret_list, [i for i in range(1, 21)])

        self.assertTrue(
            abs(self.avl_tree._get_balance(self.avl_tree.root)) <= 1)

    def test_remove(self):
        res = iter([
            [7, 8, 9, 10, 11, 12, 13, 14, 15],
            [7, 9, 10, 11, 12, 13, 14, 15],
            [7, 10, 11, 12, 13, 14, 15],
            [7, 10, 11, 12, 14, 15],
            [7, 10, 11, 12, 14]
        ])
        for i in [6, 8, 9, 13, 15]:
            self.avl_tree.remove(i)

            ret_list = []
            self.avl_tree.traverse_inorder(self.avl_tree.root, ret_list)
            self.assertEqual(ret_list, next(res))

            self.assertTrue(
                abs(self.avl_tree._get_balance(self.avl_tree.root)) <= 1)

    def tearDown(self):
        del self.avl_tree
