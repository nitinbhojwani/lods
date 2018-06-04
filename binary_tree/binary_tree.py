class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse_inorder(self, root, ret_list=None):
        if ret_list is None:
            ret_list = []
        if root is not None:
            self.traverse_inorder(root.left, ret_list)
            ret_list.append(root.val)
            self.traverse_inorder(root.right, ret_list)

    def traverse_preorder(self, root, ret_list=None):
        if ret_list is None:
            ret_list = []
        if root is not None:
            ret_list.append(root.val)
            self.traverse_preorder(root.left, ret_list)
            self.traverse_preorder(root.right, ret_list)

    def traverse_postorder(self, root, ret_list=None):
        if ret_list is None:
            ret_list = []
        if root is not None:
            self.traverse_postorder(root.left, ret_list)
            self.traverse_postorder(root.right, ret_list)
            ret_list.append(root.val)


class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right
