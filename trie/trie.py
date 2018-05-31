class Node:
    def __init__(self, value=None):
        self.children = {}
        self.value = value
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr_node = self.root
        if not word:
            return
        for i in range(len(word)):
            if not word[i] in curr_node.children:
                curr_node.children[word[i]] = Node(word[i])
            curr_node = curr_node.children[word[i]]
        curr_node.is_leaf = True

    def look_up(self, word):
        curr_node = self.root
        if not word:
            return False
        for i in range(len(word)):
            if not word[i] in curr_node.children:
                return False
            curr_node = curr_node.children[word[i]]
        return curr_node.is_leaf
