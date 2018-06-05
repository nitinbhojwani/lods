from binary_tree import binary_tree


class BinarySearchTree(binary_tree.BinaryTree):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        node = Node(val)
        if root is None:
            self.root = node
        else:
            if root.val == val:
                return False
            elif root.val < val:
                if root.right is None:
                    root.right = node
                else:
                    return self.insert(root.right, val)
            else:
                if root.left is None:
                    root.left = node
                else:
                    return self.insert(root.left, val)
        return True

    def lookup(self, root, val):
        if root is None or root.val == val:
            return root
        if root.val < val:
            return self.lookup(root.right, val)
        return self.lookup(root.left, val)

    def remove(self, root, parent, val):
        if root is None:
            return False

        if root.val == val:
            if root.left is not None and root.right is not None:
                root.val = root.right._get_min().val
                return self.remove(root.right, root, root.val)
            elif root == parent.right:
                parent.right = root.right if root.left is None else root.left
            elif root == parent.left:
                parent.left = root.right if root.left is None else root.left
            return True
        elif root.val < val:
            return self.remove(root.right, root, val)
        else:
            return self.remove(root.left, root, val)


class Node(binary_tree.Node):
    def _get_min(self):
        if self.left is None:
            return self
        return self.left._get_min()
