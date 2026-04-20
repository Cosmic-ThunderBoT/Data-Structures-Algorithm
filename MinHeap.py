class MinHeap:
    def __init__(self, cap):
        self.cap = cap
        self.heap = [0] * cap
        self.size = 0

    def insert(self, val):
        if self.size >= self.cap:
            return "Heap is Full"
        self.heap[self.size] = val
        self.size += 1
        self.swim(self.size - 1)

    def swim(self, idx):
        while idx > 0:
            pr = (idx - 1) // 2
            if self.heap[pr] > self.heap[idx]:
                self.heap[pr], self.heap[idx] = self.heap[idx], self.heap[pr]
                idx = pr
            else:
                break

    def sink(self, idx):
        while 2 * idx + 1 < self.size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = left

            if right < self.size and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[idx] <= self.heap[smallest]:
                break

            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

    def extractMin(self):
        if self.size == 0:
            return None
        min_val = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.sink(0)
        return min_val

    def get_array(self):
        return self.heap[:self.size]