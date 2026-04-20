def assign_tasks(tasks, machines):
    heap = MinHeap(machines)

    for i in range(machines):
        heap.insert(0)

    for t in tasks:
        min_load = heap.extractMin()
        heap.insert(min_load + t)

    return heap.get_array()