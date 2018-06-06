import unittest
from min_heap import min_heap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.min_heap = min_heap.MinHeap(100)
        self.min_heap.heap = [i for i in range(10)]
        self.min_heap.heap_size = 10

    def test_get_min(self):
        self.assertEqual(self.min_heap.get_min(), 0)

    def test_insert(self):
        for i in range(10, 100):
            self.assertTrue(self.min_heap.insert(i))
        # overflow condition
        self.assertFalse(self.min_heap.insert(101))

    def test_pop_min(self):
        for i in range(10):
            x = self.min_heap.pop_min()
            self.assertEqual(x, i)
        self.assertEqual(self.min_heap.pop_min(), None)

    def test_remove(self):
        res = iter([
            [0, 3, 2, 7, 4, 5, 6, 9, 8],
            [0, 3, 5, 7, 4, 8, 6, 9],
            [0, 3, 5, 9, 4, 8, 6],
            [0, 3, 5, 9, 4, 6]
        ])
        for i in [1, 2, 3, 5]:
            self.assertTrue(self.min_heap.remove(i))
            self.assertEqual(self.min_heap.heap, next(res))

    def tearDown(self):
        del self.min_heap
