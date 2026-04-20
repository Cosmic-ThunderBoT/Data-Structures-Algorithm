#for matrix
def undirectedMatrix(graph):
    size = len(graph)
    new_graph = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if graph[i][j] != 0:
                new_graph[i][j] = graph[i][j]
                new_graph[j][i] = graph[i][j]

    return new_graph
#for list
def undirectedList(adjList, max_edge):
    size = len(adjList)

    undirect = [[[0, 0] for _ in range(max_edge)] for _ in range(size)]
    countEdge = [0] * size

    for u in range(size):
        for j in range(len(adjList[u])):
            v = adjList[u][j][0]
            w = adjList[u][j][1]

            if v == 0 and w == 0:
                continue

            idx = countEdge[u]
            undirect[u][idx] = [v, w]
            countEdge[u] += 1

            idx2 = countEdge[v]
            undirect[v][idx2] = [u, w]
            countEdge[v] += 1

    return undirect