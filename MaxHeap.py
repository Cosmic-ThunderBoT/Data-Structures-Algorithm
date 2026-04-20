class MaxHeap:
    def __init__(self, cap):
        self.cap = cap
        self.heap = [0] * cap
        self.size = 0

    def insert(self, val):
        if self.size >= self.cap:
            return "No space"
        self.heap[self.size] = val
        self.swim(self.size)
        self.size += 1

    def swim(self, idx):
        while idx > 0:
            pr = (idx - 1) // 2
            if self.heap[pr] < self.heap[idx]:
                self.heap[pr], self.heap[idx] = self.heap[idx], self.heap[pr]
                idx = pr
            else:
                break

    def sink(self, idx):
        while 2 * idx + 1 < self.size:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = left

            if right < self.size and self.heap[right] > self.heap[left]:
                largest = right

            if self.heap[idx] >= self.heap[largest]:
                break

            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest

    def extractMax(self):
        if self.size == 0:
            return None
        max_val = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.sink(0)
        return max_val

    def get_array(self):
        return self.heap[:self.size]