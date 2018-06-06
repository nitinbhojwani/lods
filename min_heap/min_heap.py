class MinHeap:
    def __init__(self, capacity=None):
        self.heap = []
        self.heap_size = 0
        self.capacity = capacity

    def _bubble_up(self, idx):
        while idx != 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.heap[self.parent(idx)], self.heap[idx] = \
                self.heap[idx], self.heap[self.parent(idx)]
            idx = self.parent(idx)
        return True

    def _decrease_key(self, idx, new_val):
        if not self.heap_size >= idx or new_val > self.heap[idx]:
            return False
        self.heap[idx] = new_val
        self._bubble_up(idx)

        return True

    def _min_heapify(self, idx):
        lc = self.left(idx)
        rc = self.right(idx)
        smallest = idx
        if lc < self.heap_size and self.heap[lc] < self.heap[idx]:
            smallest = lc
        if rc < self.heap_size and self.heap[rc] < self.heap[smallest]:
            smallest = rc
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = \
                self.heap[smallest], self.heap[idx]
            self._min_heapify(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def insert(self, val):
        if self.heap_size == self.capacity:
            # overflow
            return False
        idx = self.heap_size
        self.heap_size += 1
        self.heap.append(val)
        self._bubble_up(idx)
        return True

    def pop_min(self):
        if self.heap_size == 0:
            return None
        root = self.heap[0]
        self.heap_size -= 1
        if self.heap_size >= 1:
            self.heap[0] = self.heap[self.heap_size]
            self._min_heapify(0)
        self.heap.pop()

        return root

    def remove(self, idx):
        if self.heap_size <= idx:
            return False
        # assuming that -1 can be least possible value
        self._decrease_key(idx, -1)
        self.pop_min()
        return True

    @staticmethod
    def left(i):
        return (2 * i) + 1

    @staticmethod
    def parent(i):
        return (i-1) // 2

    @staticmethod
    def right(i):
        return (2 * i) + 2
