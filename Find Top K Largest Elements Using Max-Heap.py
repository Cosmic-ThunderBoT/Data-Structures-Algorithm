def TopLargest(num, k):
    heap = MaxHeap(len(num))

    for x in num:
        heap.insert(x)

    output = []

    for i in range(k):
        output.append(heap.extractMax())

    return output