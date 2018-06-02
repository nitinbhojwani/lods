import unittest
from trie import trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = trie.Trie()
        self.trie.insert('python2')
        self.trie.insert('python3.7')

    def test_trie(self):
        self.assertTrue(self.trie.lookup('python2'))
        self.assertFalse(self.trie.lookup('python3'))
        self.assertFalse(self.trie.lookup('python'))
        self.assertTrue(self.trie.lookup('python3.7'))
