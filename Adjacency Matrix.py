class adjMatrixGraph:
    def __init__(self, num_vert):
        self.ver = num_vert
        self.matrix = [[0 for _ in range(num_vert)] for _ in range(num_vert)]

    def addEdge(self, src, dest, weight=1, direct=False):
        self.matrix[src][dest] = weight
        if not direct:
            self.matrix[dest][src] = weight