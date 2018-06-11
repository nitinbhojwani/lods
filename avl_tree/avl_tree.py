from binary_search_tree import binary_search_tree


class AvlTree(binary_search_tree.BinarySearchTree):
    def __init__(self):
        self.root = None

    def _cal_height(self, root):
        if self._get_height(root) == 0:
            return 0
        else:
            return 1 + max(self._get_height(root.left),
                           self._get_height(root.right))

    def _get_balance(self, root):
        return self._get_height(root.left) - \
            self._get_height(root.right) if root else 0

    def _get_height(self, root):
        return root.height if root else 0

    def _insert(self, root, val):
        if not root:
            return Node(val)
        elif val == root.val:
            return root
        elif val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        root.height = self._cal_height(root)

        balance = self._get_balance(root)

        # Case 1 - Left Left
        if balance > 1 and val < root.left.val:
            return self._rotate_right(root)

        # Case 2 - Right Right
        if balance < -1 and val > root.right.val:
            return self._rotate_left(root)

        # Case 3 - Left Right
        if balance > 1 and val > root.left.val:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        # Case 4 - Right Left
        if balance < -1 and val < root.right.val:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

    def _remove(self, root, val):
        ret_list = []
        self.traverse_inorder(self.root, ret_list)
        if not root:
            return root
        elif val < root.val:
            root.left = self._remove(root.left, val)
            ret_list = []
            self.traverse_inorder(self.root, ret_list)
        elif val > root.val:
            root.right = self._remove(root.right, val)
            ret_list = []
            self.traverse_inorder(self.root, ret_list)
        else:
            if root.left and root.right:
                root.val = root.right._get_min().val
                root.right = self._remove(root.right, root.val)
            else:
                placeholder = root.left if root.left else root.right
                root = None
                return placeholder

        if root is None:
            return root

        root.height = self._cal_height(root)

        balance = self._get_balance(root)

        if balance > 1:
            # Case 1 - Left Left
            if self._get_balance(root.left) >= 0:
                return self._rotate_right(root)
            # Case 2 - Left Right
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)

        if balance < -1:
            # Case 3 - Right Right
            if self._get_balance(root.right) <= 0:
                return self._rotate_left(root)
            # Case 4 - Right Left
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _rotate_left(self, node):
        node_right = node.right
        node_right_left = node.right.left
        node.right = node_right_left
        node_right.left = node

        node.height = self._cal_height(node)
        node_right.height = self._cal_height(node_right)

        return node_right

    def _rotate_right(self, node):
        node_left = node.left
        node.left = node_left.right
        node_left.right = node

        node.height = self._cal_height(node)
        node_left.height = self._cal_height(node_left)

        return node_left

    def insert(self, val):
        return self._insert(self.root, val)

    def remove(self, val):
        self.root = self._remove(self.root, val)


class Node(binary_search_tree.Node):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

    def _get_min(self):
        if self.left is None:
            return self
        return self.left._get_min()
