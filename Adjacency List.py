class adjListGraph:
    def __init__(self, num_ver, max_edge):
        self.ver = num_ver
        self.max_edge = max_edge

        self.adjList = [[[0, 0] for _ in range(max_edge)] for _ in range(num_ver)]
        self.countEdge = [0] * num_ver

    def addEdge(self, src, dest, weight=1, direct=False):
        idx = self.countEdge[src]
        self.adjList[src][idx] = [dest, weight]
        self.countEdge[src] += 1

        if not direct:
            idx2 = self.countEdge[dest]
            self.adjList[dest][idx2] = [src, weight]
            self.countEdge[dest] += 1