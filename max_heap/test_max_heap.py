import unittest
from max_heap import max_heap


class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        self.max_heap = max_heap.MaxHeap(100)
        self.max_heap.heap = [i for i in range(100, 90, -1)]
        self.max_heap.heap_size = 10

    def test_get_max(self):
        self.assertEqual(self.max_heap.get_max(), 100)

    def test_insert(self):
        for i in range(90, 0, -1):
            self.assertTrue(self.max_heap.insert(i))
        # overflow condition
        self.assertFalse(self.max_heap.insert(0))

    def test_pop_max(self):
        for i in range(100, 90, -1):
            x = self.max_heap.pop_max()
            self.assertEqual(x, i)
        self.assertEqual(self.max_heap.pop_max(), None)

    def test_remove(self):
        res = iter([
            [100, 97, 98, 93, 96, 95, 94, 91, 92],
            [100, 97, 95, 93, 96, 92, 94, 91],
            [100, 97, 95, 91, 96, 92, 94],
            [100, 97, 95, 91, 96, 94]
        ])
        for i in [1, 2, 3, 5]:
            self.assertTrue(self.max_heap.remove(i))
            self.assertEqual(self.max_heap.heap, next(res))

    def tearDown(self):
        del self.max_heap
